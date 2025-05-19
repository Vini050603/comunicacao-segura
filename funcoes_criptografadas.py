from Crypto.Cipher import DES, AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64


def pad(text, block_size):
    pad_len = block_size - len(text) % block_size
    return text + chr(pad_len) * pad_len


def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]


# ----- DES com CBC -----
def encrypt_des(message):
    key = get_random_bytes(8)  # DES = 64 bits
    iv = get_random_bytes(8)   # IV = 64 bits
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_text = pad(message, 8)
    ciphertext = cipher.encrypt(padded_text.encode())

    # Retorna texto cifrado + chave + IV codificados
    return (
        base64.b64encode(ciphertext).decode(),
        base64.b64encode(key).decode(),
        base64.b64encode(iv).decode()
    )


def decrypt_des(ciphertext_b64, key_b64, iv_b64):
    ciphertext = base64.b64decode(ciphertext_b64)
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_text = cipher.decrypt(ciphertext).decode()
    return unpad(padded_text)


# ----- AES com CBC -----
def encrypt_aes(message):
    key = get_random_bytes(16)  # AES = 128 bits
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(message, 16)
    ciphertext = cipher.encrypt(padded_text.encode())
    return (
        base64.b64encode(ciphertext).decode(),
        base64.b64encode(key).decode(),
        base64.b64encode(iv).decode()
    )


def decrypt_aes(ciphertext_b64, key_b64, iv_b64):
    ciphertext = base64.b64decode(ciphertext_b64)
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = cipher.decrypt(ciphertext).decode()
    return unpad(padded_text)


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
