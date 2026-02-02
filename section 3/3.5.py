import bcrypt
import jwt
import datetime

# bcrypt хешування
password = b"mypassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print("Hashed:", hashed)

# JWT токен
payload = {"user": "admin", "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}
token = jwt.encode(payload, "secret_key", algorithm="HS256")
print("JWT:", token)

# Декодування
decoded = jwt.decode(token, "secret_key", algorithms=["HS256"])
print("Decoded:", decoded)
