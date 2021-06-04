import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv
from mongo import *

load_dotenv()

def register(credentials):
    fernet = Fernet(os.getenv('KEY_SECRET'))
    new_credentials = credentials.copy()
    new_credentials['password'] = fernet.encrypt(new_credentials['password'].encode()).decode()
    user_id = create("users", new_credentials)
    return get("users", user_id)

def login(credentials):
    fernet = Fernet(os.getenv('KEY_SECRET'))
    user = list(getAll("users", {"username": credentials['username']}))

    if len(user) != 0:
        decrypted_password = fernet.decrypt(user[0]['password'].encode()).decode()
        if decrypted_password == credentials['password']:
            user[0]['password'] = decrypted_password
            return user[0]
        else:
            return "Nombre de Usuario o contraseña incorrecta"
    else:
        return "Nombre de Usuario o contraseña incorrecta"

def change_password(user_id, new_password):
    fernet = Fernet(os.getenv('KEY_SECRET'))
    encripted_password = fernet.encrypt(new_password.encode()).decode()
    update('users', user_id, {'password': encripted_password})
