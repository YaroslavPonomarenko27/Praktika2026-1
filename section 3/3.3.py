from dotenv import load_dotenv
import os

load_dotenv()  # Завантажити змінні з файлу .env

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

print("User:", DB_USER)
print("Password:", DB_PASS)

DB_USER=admin 
DB_PASS=12345
