from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import base64

# Helper method to convert bytes to strings
def utf8(s: bytes):
    return str(s, 'utf-8')

# Load private key from external file
def load_private_key(file_name):
    with open(file_name, 'rb') as file:
        private_key_data = file.read()
        private_key = serialization.load_pem_private_key(private_key_data, password=None, backend=default_backend())
    return private_key

# Helper method to decrypt a message with a given key
def decrypt_message(msg, key):
    decrypted_msg = key.decrypt(
        base64.b64decode(msg), 
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted_msg

def main():
    # Load the private key
    private_key = load_private_key('my_private_key.pem')

    # Open the encrypted message from the external file
    with open('encrypted_message.bin', 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the message with the private key
    decrypted_msg = decrypt_message(encrypted_data, private_key)
    print(f'Decrypted message:\n{utf8(decrypted_msg)}\n\n')
    

    pass

if __name__ == "__main__":
    main()