import json

# Definimos la direccion del archivo json
direccionJson="modulos/modulosIngredientes/listaIngredientes.json"
entrada=""

# Esta funcion toma un mensaje en el primer argumento que se va a mostrar en bucle hasta que se ingrese una de las opciones tomadas en el segundo argumento
# Retorna la opción válida ingresada
# El uso es en un if, comparando el resultado de la función con lo que se quiera hacer en el if
def validarEntrada(mensaje,opciones):
    while True:
        print(mensaje)
        opc=""
        for i in opciones:
            opc += i+"/"
        opc=opc[:-1]
        # Validar que entrada este en las opciones provistas
        entrada=input()
        if entrada not in opciones:
            print(f"Ingrese una opción válida [{ opc }]")
            continue
        else:
            break 
    return entrada

def validarFloat(mensaje, salida=0):
    while True:
        print(mensaje)
        numero=input()
        if salida==1 and numero=='n':
            return False
        try:
            float(numero)
            if float(numero)<0:
                print("\nEl precio que ingresó es negativo")
                continue
            else:
                if validarEntrada(f"Usted ingreso el precio { numero }. Desea continuar con este precio? [s/n]",['s','n'])=='s':
                    return numero
                else:
                    continue

        except ValueError:
            print("\nEl precio que ingresó no es un número válido. Ingrese un numero real.") 
            continue

# Funcion que toma un mensaje y lo imprime, pide una entrada y pide al usuario confirmar si la entrada es correcta
# Si no es correcta se repite. Si si es correcta retorna la entrada ingresada. 
# Si la entrada es 'n' se rompe el loop y retorna False.
def manejoString(mensaje,*args):
    while True:
        print(mensaje)
        nombre=input()
        if nombre=='n':
            return False
        else:
            x=validarEntrada(f"Seguro que desea continuar con '{ nombre }'? [s/n].",['s','n'])
            if x=='s':
                return nombre
            else:
                continue

def importarDiccionario():
    with open(direccionJson, encoding="utf-8") as archivoJson:
        ingredientes=json.load(archivoJson)
    return ingredientes

ingredientes=importarDiccionario()

def main():
    pass

if __name__=="__main__":
    while True:
        abv=""
        while abv=="": 
            for i in ingredientes:
                print(f'{ ingredientes[i]["nombre"] }\t({ i }) \t { ingredientes [i]["precio"] }')  
            print("\nIngrese la abreviacion de el ingrediente que desee modificar, o ingrese una nueva \n"\
                "abreviación para agregar un ingrediente nuevo. Para guardar sus cambios, ingrese [guardar]")  
            abv=input()

            ### Guardar diccionario como json

            if abv=="guardar":
                with open(direccionJson, "w", encoding="utf-8") as archivoJson:
                    json.dump(ingredientes,archivoJson)
                    print("Sus cambios han sido guardados")

            # Si es un ingrediente existente
            elif abv in ingredientes:
                print(f"Ha seleccionado el ingrediente ({ abv }): { ingredientes[abv]['nombre'] } { ingredientes[abv]['precio'] }")
                if validarEntrada(f"Es este el ingrediente que deseas modificar? [s/n]",("s","n"))\
                    =="s":

                    # Se confirmo que es este el ingrediente a modificar
                    match validarEntrada("Que valor desea modificar?\n abv = abreviacion\n nombre = nombre\n precio = precio\n borrar = eliminar el ingrediente (no se puede deshacer!)\n n = volver al inicio"\
                        ,("abv","nombre","precio","borrar","n")):
                        case "abv":
                            entrada=manejoString(f"Usted está modificando la abreviacion de ({ abv }): { ingredientes[abv]['nombre'] }. Ingrese la nueva abreviacion o ingrese [n] para volver al inicio.")
                            # Asegura que la entrada no sea n. Si es n se sale.
                            if entrada!=False:
                                ingredientes[entrada]=ingredientes.pop(abv)
                            else:
                                continue

                        case "nombre":
                            entrada=manejoString(f"Usted está modificando el nombre de ({ abv }): { ingredientes[abv]['nombre'] }. Ingrese el nuevo nombre o ingrese [n] para volver al inicio.")
                            # Asegura que la entrada no sea n. Si es n se sale.
                            if entrada!=False:
                                ingredientes[abv]['nombre']=entrada
                            else:
                                continue

                        case "precio":
                            entrada=validarFloat(f"Usted está modificando el precio de ({ abv }): { ingredientes[abv]['nombre'] }, que actualmente es { ingredientes[abv]['precio'] }. Ingrese el nuevo precio o ingrese [n] para volver al inicio.",1)
                            if entrada!=False:
                                ingredientes[abv]['precio']=float(entrada)
                            else:
                                continue
                        
                        case "borrar":
                            if validarEntrada(f"Usted está a punto de eliminar del registro a ({ abv }): { ingredientes[abv]['nombre'] }. Esta acción no puede deshacerse. Está seguro? [s/n]",("s","n"))\
                                =="s":
                                # Elimina el ingrediente del diccionario
                                del ingredientes[abv]  
                            else:
                                print("Regresando al inicio...")
                                continue

                        case "n":
                            continue
                
            # Si es un ingrediente nuevo
            else:

                #Ingresar nombre de ingrediente nuevo
                nombre=manejoString(f"\nIngrese el nombre del nuevo ingrediente ({ abv }) o ingrese [n] para regresar a la pantalla inicial.")
                if nombre!=False:

                    # Validar que el precio sea valido
                    precio=validarFloat(f"Ingrese el precio del nuevo ingrediente ({ abv }) { nombre } (solo numeros reales positivos) o ingrese [n] para regresar a la pantalla inicial.",1)
                    if precio!=False:

                        # Confirmacion aceptada de todos los datos nuevos
                        if validarEntrada(f"Seguro que desea continuar con los siguientes datos?: ({ abv }) {nombre}: {precio}. [n] Regresará a la pantalla principal. [s/n]",("s","n"))\
                            =="s":
                            ingredientes[str(abv)] = { 'precio': float(precio), 'nombre': str(nombre)}
                            print("Ingrediente nuevo agregado. Lista actual: ")

