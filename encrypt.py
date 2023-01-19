import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class AES256:
    def __init__(self, password):
        self.password = password
        self.salt = b'\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(self.kdf.derive(password))
        self.cipher = Fernet(self.key)

    def encrypt(self, message):
        return self.cipher.encrypt(message)

    def decrypt(self, message):
        return self.cipher.decrypt(message)

# decorators
def encrypt_decorator(password):
    def decorator(func):
        def wrapper(text):
            aes = AES256(password)
            try:
                encrypted_text = aes.encrypt(text.encode()).decode()
                return func(encrypted_text)
            except:
                return func(text)
        return wrapper
    return decorator

def decrypt_decorator(password):
    def decorator(func):
        def wrapper(text):
            aes = AES256(password)
            try:
                decrypted_text = aes.decrypt(text.encode()).decode()
                return func(decrypted_text)
            except:
                return func(text)
        return wrapper
    return decorator

@encrypt_decorator(b'password123')
def encrypt_output(text):
    return text

@decrypt_decorator(b'password123')
def decrypt_input(text):
    return text

if __name__ == '__main__':

    

    # text = encrypt_output('hello world again')
    # print(text)
    # print(decrypt_input(text))

    aes = AES256(b"Secret")
    encrypted_text = aes.encrypt("textToMatch".encode()).decode()
    print(encrypted_text)

    decrypted_text = aes.decrypt(encrypted_text.encode()).decode()
    print(decrypted_text)

