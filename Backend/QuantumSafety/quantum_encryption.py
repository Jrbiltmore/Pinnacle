
import logging
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

logging.basicConfig(level=logging.INFO)

class QuantumEncryptionError(Exception):
    pass

def generate_key_pair():
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )
        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(b'your-passphrase')
        )

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        logging.info("RSA key pair generated successfully")
        return private_pem, public_pem
    except Exception as e:
        logging.error(f"Error generating key pair: {str(e)}")
        raise QuantumEncryptionError(f"Key pair generation failed: {str(e)}")

def encrypt_message(public_key_pem, message):
    try:
        public_key = serialization.load_pem_public_key(public_key_pem)
        symmetric_key = urandom(32)
        iv = urandom(16)

        cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv))
        encryptor = cipher.encryptor()
        encrypted_message = encryptor.update(message.encode('utf-8')) + encryptor.finalize()

        encrypted_symmetric_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        logging.info("Message encrypted successfully")
        return encrypted_symmetric_key, iv, encrypted_message
    except Exception as e:
        logging.error(f"Error encrypting message: {str(e)}")
        raise QuantumEncryptionError(f"Encryption failed: {str(e)}")

def decrypt_message(private_key_pem, encrypted_symmetric_key, iv, encrypted_message):
    try:
        private_key = serialization.load_pem_private_key(private_key_pem, password=b'your-passphrase')
        symmetric_key = private_key.decrypt(
            encrypted_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv))
        decryptor = cipher.decryptor()
        decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

        logging.info("Message decrypted successfully")
        return decrypted_message.decode('utf-8')
    except Exception as e:
        logging.error(f"Error decrypting message: {str(e)}")
        raise QuantumEncryptionError(f"Decryption failed: {str(e)}")
