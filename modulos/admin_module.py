from authentication import login, register, change_password
from mongo import update
import clear

def login_menu():
    credentials = {'username': "", 'password': ""}

    while True:
        clear.clear()
        print('**** INICIO DE SESION ****\n')
        while credentials['username'] == "":
            credentials['username'] = input('Username: ')
            if credentials['username'] == "":
                print('No puede introducir un usuario vacio.\n')

        while credentials['password'] == "":
            credentials['password'] = input('Password: ')
            if credentials['password'] == "":
                print('No puede introducir una contraseña vacia.\n')

        try:
            user = login(credentials)
            if type(user) == dict:
                return user
            raise Exception(user)
        except Exception as e:
            print(e, '.\nDesea continuar? [S/n]:')
            option = input()
            option = option.upper()
            if option == 'S':
                credentials['username'] = ''
                credentials['password'] = ''
            else:
                break

    return None

def register_menu():
    credentials = {'username': "", 'password': "", 'full_name': ""}

    print("**** REGISTRO DE USUARIO ****")

    while credentials['full_name'] == "":
        credentials['full_name'] = input('Nombre completo: ')
        if credentials['full_name'] == "":
            print('No puede introducir un nombre vacio.\n')

    while credentials['username'] == "":
        credentials['username'] = input('Nombre de Usuario: ')
        if credentials['username'] == "":
            print('No puede introducir un usuario vacio.\n')

    while credentials['password'] == "":
        credentials['password'] = input('Contrase;a: ')
        if credentials['password'] == "":
            print('No puede introducir una contraseña vacia.\n')

    try:
        user = register(credentials)
        if type(user) == dict:
            user['_id'] = user['_id'].to_string()
            return user
        raise Exception('Hubo un error al crear el usuario')
    except Exception as e:
        print(e)

    return None

def change_user_full_name(user_id):
    full_name, option = "", "S"
    while option == 'S':
        print('**** CAMBIO DE NOMBRE ****')

        while full_name == "":
            full_name = input('Nombre Completo: ')
            if full_name == "":
                print('No puede introducir un nombre vacio.')
        try:
            update('users', user_id, {'full_name': full_name})
            return full_name
        except Exception as e:
            option = input('Ha ocurrido un error. Desea intentar nuevamente? [S/n]: ')
            option = option.upper()
            if option != 'S':
                return None
            full_name = ""

def change_user_username(user_id):
    username, option = "", "S"
    while option == 'S':
        print('**** CAMBIO DE NOMBRE DE USUARIO ****')

        while username == "":
            username = input('Nombre de Usuario: ')
            if username == "":
                print('No puede introducir un nombre vacio.')
        try:
            update('users', user_id, {'username': username})
            return username
        except Exception as e:
            option = input('Ha ocurrido un error. Desea intentar nuevamente? [S/n]: ')
            option = option.upper()
            if option != 'S':
                return None
            username = ""

def change_user_password(user_id):
    password, repeat_password, option = "", "S"
    while option == 'S':
        print('**** CAMBIO DE CONTRASENA ****')

        while password == "":
            password = input('Contrasena: ')
            if password == "":
                print('No puede introducir una contrasena vacio.')


        while repeat_password == "":
            repeat_password = input('Repita contrase;a: ')
            if repeat_password == "":
                print('No puede introducir una contrasena vacio.')

        if password != repeat_password:
            print('La contrase;as no coinciden. ', end='')
        else:
            try:
                change_password(user_id, password)
                return password
            except Exception:
                print('Ha ocurrido un error. ', end="")
        option = input('Desea intentar nuevamente? [S/n]: ')
        option = option.upper()
        if option != 'S':
            return None
        password = ""
        repeat_password = ""

def show_account_data(user):
    print('**** DATOS DE CUENTA ****\n')

    print(f'Nombre Completo: {user["full_name"]}')
    print(f'Nombre de Usuario: {user["username"]}')
    print(f'Contrasena: {user["password"]}\n')

    input('Presione Enter para continuar...')

def credentials_menu_selection():
    while True:
        option = input('Seleccione una opcion:\n1. Iniciar Sesion\n2. Registrar nuevo admin\n-> ')

        if option == '1':
            return login_menu()
        elif option == '2':
            return register_menu()
        elif option == '3':
            return
        else:
            print('La opcion es invalida. Intente de nuevo.\n')


def my_account_menu(user):
    while True:
        print('**** MI CUENTA ****')

        option = input(f'Hola, {user["username"]}! Que desea hacer?\n1. Ver datos de cuenta\n2. Cambiar nombre\n3. Cambiar nombre de usuario\n4. Cambiar contrasena\n5. Atras\n-> ')

        if option == '1':
            show_account_data(user)
        elif option == '2':
            new_name = change_user_full_name(user['_id'])
            if new_name != None:
                user['full_name'] = new_name
        elif option == '3':
            new_username = change_user_username(user['_id'])
            if new_username != None:
                user['username'] = new_username
        elif option == '4':
            new_password = change_user_password(user['_id'])
            if new_password != None:
                user['password']: new_password
        elif option == '5':
            return
        else:
            print('La opcion es invalida. Intente de nuevo.\n')

def main_menu(user):
    while True:
        print('*** Bienvenid@, ', user['username'], ' ****\n')
        option = input('Que desea hacer?\n1. Gestionar Ingredientes\n2. Gestionar cuenta\n3. Cerrar Sesion\n-> ')
        if option == '1':
            return
        elif option == '2':
            my_account_menu(user)
        elif option == '3':
            return
        else:
            print('La opcion es invalida. Intente de nuevo.\n')

def admin_main():
    user = credentials_menu_selection()
    if user != None:
        main_menu(user)
