import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# SHA-256
text = "Hello"
hash_object = hashlib.sha256(text.encode())
print("SHA-256:", hash_object.hexdigest())

# AES шифрування
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
data = b"Secret Message"
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)
print("AES encrypted:", ciphertext)
