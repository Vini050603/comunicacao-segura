from Crypto.Cipher import DES, AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from funcoes_criptografadas import DES, AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

import base64

# ----- DES com CBC -----
def encrypt_des(message):
    key = get_random_bytes(8)
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_text = pad(message.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext.hex(), key.hex(), iv.hex()


def decrypt_des(ciphertext_hex, key_hex, iv_hex):
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_message = cipher.decrypt(ciphertext)
    message = unpad(padded_message, DES.block_size).decode()
    return message


# ----- AES com CBC -----
def encrypt_aes(message):
    key = get_random_bytes(16)  # 16 bytes = 128 bits
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(message.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext.hex(), key.hex(), iv.hex()


def decrypt_aes(ciphertext_hex, key_hex, iv_hex):
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = cipher.decrypt(ciphertext)
    message = unpad(padded_message, AES.block_size).decode()
    return message


# ----- RSA com chave pública e privada -----
def encrypt_rsa(message):
    key = RSA.generate(2048)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    cipher = PKCS1_OAEP.new(key.publickey())
    ciphertext = cipher.encrypt(message.encode())
    return (
        base64.b64encode(ciphertext).decode(),
        public_key,
        private_key
    )


def decrypt_rsa(ciphertext_b64, private_key_str):
    ciphertext = base64.b64decode(ciphertext_b64)
    private_key = RSA.import_key(private_key_str)
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(ciphertext).decode()
