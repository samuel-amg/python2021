from cryptography.fernet import Fernet
from dotenv import dotenv_values
from mongo import *

config = dotenv_values(".env")

def register(credentials):
    fernet = Fernet(config['KEY_SECRET'])
    new_credentials = credentials.copy()
    new_credentials['password'] = fernet.encrypt(new_credentials['password'].encode()).decode()
    return create("users", new_credentials)

def login(credentials):
    fernet = Fernet(config['KEY_SECRET'])
    user = list(getAll("users", {"username": credentials['username']}))

    if len(user) != 0:
        print(credentials['password'])
        decrypted_password = fernet.decrypt(user[0]['password'].encode()).decode()
        print(decrypted_password)
        if decrypted_password == credentials['password']:
            user[0]['password'] = decrypted_password
            return user[0]
        else:
            return "Nombre de Usuario o contraseña incorrecta"
    else:
        return "Nombre de Usuario o contraseña incorrecta"
