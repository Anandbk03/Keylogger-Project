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

   ```bash
   python Generatefernetkey.py
