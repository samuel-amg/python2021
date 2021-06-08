from modulos.mongo import update, getAll, delete, create

def list_toppings(toppings):
    for i, topping in enumerate(toppings):
        print(f'{i + 1}. {topping["name"]} - {topping["value"]}$')

    input('Presione Enter para continuar...')

def create_topping():
    while True:
        name, value = "", -1
        print("**** NUEVO INGREDIENTE ****\n")

        while name == "":
            name = input("Nombre del ingrediente: ")
            if name == "":
                print("No puede introducir un nombre vacio.")

        while value < 0:
            value = float(input('Precio: '))
            if value < 0:
                print("EL precio debe ser positivo")

        try:
            return create("toppings", {"name": name, "value": value})
        except Exception as e:
            option = input(f"{e}. Desea reintentar? [S/n]: ")
            if option.upper() == 'N':
                return

def update_topping(toppings):
    print("**** ACTUALIZAR INGREDIENTE ****")

    if len(toppings):
        while True:
            print('Introduzca el numero del ingrediente a actualizar:')
            for i, topping in enumerate(toppings):
                print(f'{i + 1}. {topping["name"]}')
            option = input('-> ')

            try:
                option_num = int(option)

                while True:
                    name, value = "", -1
                    choose = input('Que desea cambiar?\n1. Nombre\n2. Valor\n3. Ambos\n4. Atras\n-> ')
                    if choose == '1':
                        while name == "":
                            name = input("Nombre del ingrediente: ")
                            if name == "":
                                print("No puede introducir un nombre vacio.")

                        return update("toppings", str(toppings[option_num - 1]["_id"]), {"name":name})
                    elif choose == '2':
                        while value < 0:
                            value = float(input('Precio: '))
                            if value < 0:
                                print("EL precio debe ser positivo")

                        return update("toppings", str(toppings[option_num - 1]["_id"]), {"value":value})
                    elif choose == '3':
                        while name == "":
                            name = input("Nombre del ingrediente: ")
                            if name == "":
                                print("No puede introducir un nombre vacio.")

                        while value < 0:
                            value = float(input('Precio: '))
                            if value < 0:
                                print("EL precio debe ser positivo")

                        return update("toppings", str(toppings[option_num - 1]["_id"]), {"value":value, "name": name})
                    elif choose == '4':
                        return
                    else:
                        print("Opcion invalida. Intente de nuevo\n")
            except Exception:
                print("Opcion invalida. Intente de nuevo\n")
    else:
        input('Sin ingredientes. Presione cualquier tecla para continuar...')

def delete_topping(toppings):
    print("**** ELIMINAR INGREDIENTE ****")

    if len(toppings):
        while True:
            print('Introduzca el numero del ingrediente a eliminar:')
            for i, topping in enumerate(toppings):
                print(f'{i + 1}. {topping["name"]}')
            option = input('-> ')

            try:
                option_num = int(option)
                return delete("toppings", str(toppings[option_num - 1]["_id"]))
            except Exception:
                print("Opcion invalida. Intente de nuevo\n")
    else:
        input('Sin ingredientes. Presione cualquier tecla para continuar...')

def toppings_main_menu(user):
    print('**** GESTION DE INGREDIENTESS ****\n')

    while True:
        option = ""

        while option == '':
            toppings = getAll("toppings", {})

            option = input(f'Bienvenid@, {user["username"]}, que desea hacer?\n1. Ver ingredientes actuales\n2. Crear nuevo ingrediente\n3. Cambiar informacion de ingrediente\n4. Eliminar ingrediente\n5. Atras\n-> ')

            if option == '1':
                list_toppings(toppings)
            elif option == '2':
                create_topping()
            elif option == '3':
                update_topping(toppings)
            elif option == '4':
                delete_topping(toppings)
            elif option == '5':
                return
            else:
                print('Opcion invalida. Intente de nuevo\n')