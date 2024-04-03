from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import base64

# Helper method to convert bytes to strings
def utf8(s: bytes):
    return str(s, 'utf-8')

# Load public key from external file
def load_public_key(file_name):
    with open(file_name, 'rb') as file:
        public_key_data = file.read()
        public_key = serialization.load_pem_public_key(public_key_data, backend=default_backend())
    return public_key

# Helper method to encrypt message
def encrypt_message(msg, key):
    encrypted_msg = base64.b64encode(key.encrypt(
        msg, 
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ))
    return encrypted_msg # Returns the bytes


def main():
    # Obtain the value of the public key
    public_key = load_public_key('my_public_key.pem')

    # Create a secret message and print it to the screen

    # Encrypt your message

    # Write the encrypted message to a file

    pass

if __name__ == "__main__":
    main()