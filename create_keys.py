from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    return private_key

def generate_public_key(private_key):
    public_key = private_key.public_key()
    return public_key

# Helper method to convert bytes to strings
def utf8(s: bytes):
    return str(s, 'utf-8')

# Write private key to file
def write_private_key_to_file(file_name, private_key):
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open(file_name, 'wb') as file:
        file.write(private_pem)

# Write public key to file
def write_public_key_to_file(file_name, public_key):
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(file_name, 'wb') as file:
        file.write(public_pem)


def main():
    # Generate a new private key

    # Generate a new public key tied to the private key

    # Print the private key to the screen

    # Write the private key to a file

    # Write the public key to a file

    pass

if __name__ == "__main__":
    main()