# Keylogger with Encrypted Gmail Credentials

This project demonstrates how to implement a keylogger that stores encrypted Gmail credentials. The project includes multiple files for generating encrypted credentials and utilizing them in a secure manner.

## Prerequisites

Before running the script, follow these steps to generate an app password for Gmail and encrypt your credentials.

### 1. Generate a Gmail App Password
To securely use Gmail with the script, you must first generate an app password. Follow these steps:
1. Navigate to your [Gmail settings](https://mail.google.com/mail/u/0/#settings/accounts).
2. Search for **App Passwords**.
3. Enable **Two-Factor Authentication** (2FA) if not already enabled.
4. After enabling 2FA, you can generate an app password.
5. Save the generated app password, as you will use it later for the encryption process.

### 2. Generate Encryption Key

1. Run the `Generatefernetkey.py` file to generate a key for your encryption.
   - This key will be used to securely encrypt and decrypt your Gmail credentials.
   - The script will generate and print the encryption key, which you should store securely.

## Step 3: Encrypt Your Gmail Credentials
1.Open the Encryptcredential.py file.
2.Enter your Gmail email address and the app password you generated in Step 1.
3.Run the file to encrypt your credentials. 
4.The script will generate an encrypted version of your Gmail email and app password, which will be used in the main script (script.py).

## Step 4: Running the Keylogger
1.Once your credentials are encrypted, you are ready to run the keylogger:
2.Open script.py and replace the placeholders with the encrypted credentials generated in Step 3.
3.Run the script.py file. The keylogger will start and begin capturing keystrokes and sending the same through mail.


