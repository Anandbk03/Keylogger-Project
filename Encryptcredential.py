from cryptography.fernet import Fernet

# Replace with your generated Fernet key
key = b'ENTER THE KEY GENERATED HERE'
fernet = Fernet(key)

# Replace with your email and password
email = "your_email@gmail.com"
password = "your_password"

# Encrypt email and password
encrypted_email = fernet.encrypt(email.encode())
encrypted_password = fernet.encrypt(password.encode())

# Print the encrypted values
print("Encrypted Email:", encrypted_email)
print("Encrypted Password:", encrypted_password)
