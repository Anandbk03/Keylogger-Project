from cryptography.fernet import Fernet

# Generate a Fernet key
key = Fernet.generate_key()

# Save the key securely
print("Your Fernet Key:")
print(key.decode())
