from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypting data
encrypted_data = cipher_suite.encrypt(b"Sensitive data")

# Decrypting data
decrypted_data = cipher_suite.decrypt(encrypted_data)
