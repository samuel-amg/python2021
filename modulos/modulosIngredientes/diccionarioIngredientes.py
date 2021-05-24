# Definimos el diccionario de datos con los ingredientes del archivo .txt
ingredientes = {}
entrada=""

# Esta funcion toma un mensaje en el primer argumento que se va a mostrar en bucle hasta que se ingrese una de las opciones tomadas en el segundo argumento
# Retorna la opción ingresada, tomando en cuenta que ya fué validada
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

# Función para validar que un número ingresado sea float
def validarFloat(numero):
    try:
        float(numero)
        if float(numero)<0:
            print("\nEl precio que ingresó es negativo")
            return 1
        else:
            return 0
    
    except ValueError:
        print("\nEl precio que ingresó no es un número válido") 
        return 1  

def importarDiccionario():
    with open("modulos/modulosIngredientes/listaIngredientes.txt", encoding="utf-8") as f:
        for line in f:
            (abv,precio,nombre) = line.strip().split(",")
            ingredientes[str(abv)] = { 'precio': float(precio), 'nombre': str(nombre)}
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

            if abv=="guardar":
                with open("modulos/modulosIngredientes/listaIngredientes.txt", "w", encoding="utf-8") as file:
                    for i in ingredientes:
                        linea=f"{ i },{ ingredientes[i]['precio'] },{ ingredientes[i]['nombre'] }"
                        file.write(linea+"\n")
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
                            print(f"Usted está modificando la abreviacion de ({ abv }): { ingredientes[abv]['nombre'] }. Ingrese la nueva abreviacion o ingrese [n] para volver al inicio.")
                            entrada=input()
                            # Asegura que la entrada no sea n. Si es n se sale.
                            if entrada!='n':
                                ingredientes[entrada]=ingredientes.pop(abv)
                                entrada=""
                            else:
                                entrada=""
                                continue

                        case "nombre":
                            print(f"Usted está modificando el nombre de ({ abv }): { ingredientes[abv]['nombre'] }. Ingrese el nuevo nombre o ingrese [n] para volver al inicio.")
                            entrada=input()
                            # Asegura que la entrada no sea n. Si es n se sale.
                            if entrada!='n':
                                ingredientes[abv]['nombre']=entrada
                                entrada=""
                            else:
                                entrada=""
                                continue

                        case "precio":
                            while True:
                                print(f"Usted está modificando el precio de ({ abv }): { ingredientes[abv]['nombre'] }, que actualmente es { ingredientes[abv]['precio'] }. Ingrese el nuevo precio o ingrese [n] para volver al inicio.")
                                entrada=input()
                                if entrada!='n':
                                    # Se ingresó un float válido
                                    if validarFloat(entrada)==0:
                                        ingredientes[abv]['precio']=float(entrada)
                                        break
                                    # Se ingresó un valor no válido    
                                    else:
                                        print('Se ingresó un numero inválido. Intente de nuevo.')
                                        continue
                                # Se ingresó n por lo que el programa regresa al inicio
                                else:
                                    entrada=""
                                    continue

                        case "borrar":
                            if validarEntrada(f"Usted está a punto de eliminar del registro a ({ abv }): { ingredientes[abv]['nombre'] }. Esta acción no puedes deshacerse. Está seguro? [s/n]",("s","n"))\
                                =="s":
                                # Elimina el ingrediente del diccionario
                                del ingredientes[abv]  
                            else:
                                entrada=""
                                print("Regresando al inicio...")
                                continue

                        case "n":
                            continue

                else:
                    break
                
            # Si es un ingrediente nuevo
            else:

                #Loop para ingresar nombre de ingrediente nuevo
                while True:
                    print(f"\nIngrese el nombre del nuevo ingrediente ({ abv }):")
                    nombre=input()

                    # Si sí desea continuar con el nombre ingresado
                    if validarEntrada(f"Seguro que desea continuar con el nombre: ({ abv }) { nombre }? [s/n]",("s","n"))\
                        =="s":

                        # Loop para ingresar precio
                        while True:
                            print(f"Ingrese el precio del nuevo ingrediente ({ abv }) { nombre } (Solo numeros reales positivos)")
                            precio=input()

                            # Validar que el precio sea valido
                            if validarFloat(precio)==0:

                                # Confirmacion aceptada de todos los datos nuevos
                                if validarEntrada(f"Seguro que desea continuar con los siguientes datos?: ({ abv }) {nombre}: {precio} [s/n]",("s","n"))\
                                    =="s":
                                    ingredientes[str(abv)] = { 'precio': float(precio), 'nombre': str(nombre)}
                                    print("Ingrediente nuevo agregado. Lista actual: ")
                                    break
                                
                                # Negada la confirmación de todos los datos nuevos
                                else:

                                    # Si se desea ingresar otro precio
                                    if validarEntrada("Desea ingresar otro precio? [n] regresará a la pantalla inicial. [s/n]",("s","n"))\
                                        =="s":
                                        continue
                                    # No se desea ingresar otro precio
                                    else:
                                        break
                            # El precio no es válido        
                            else:
                                continue
                            
                    # Si no desea continuar con el nombre ingresado
                    else:
                        if validarEntrada(f"Desea ingresar otro nombre? [n] regresará a la pantalla inicial. [s/n]",("s","n"))\
                        =="s":
                        
                            continue
                        # Si se elige no, se sale del loop y regresa a la pantalla inicial 
                        else:
                            break
                    break

