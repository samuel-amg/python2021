# Importación para saber en qué sistema operativo se está
from os import system, name

# Función para limpiar pantalla en consola
def clear():
  
    # Limpiar consola para Windows
    if name == 'nt':
        _ = system('cls')
  
    # Limpiar consola para Linux y Mac
    else:
        _ = system('clear')


print("""**************************
*    SANDWICHES UCAB     *
**************************\n""")

# Definimos el diccionario de datos con los ingredientes
ingredientes = {
	'ja': { 'precio': 40, 'nombre': 'Jamón'},
	'ch': { 'precio': 35, 'nombre': 'Champiñones'},
	'pi': { 'precio': 30, 'nombre': 'Pimentón'},
	'dq': { 'precio': 40, 'nombre': 'Doble Queso'},
	'ac': { 'precio': 57.5, 'nombre': 'Aceitunas'},
	'pp': { 'precio': 38.5, 'nombre': 'Pepperoni'},
	'sa': { 'precio': 62.5, 'nombre': 'Salchichon'},
}

# Inicializamos variables
precioTotal = 0
cont = 0

# Ciclo While principal
while True:

	clear()

	precioActual = 0

	print(f'Sandwich número {cont + 1}\n')
	print('Opciones:')

	# Ciclo para preguntar el tamaño del sandwich
	# En caso de error, se repite
	while True:
		tam = input('Tamaños:  Triple ( t ) Doble ( d ) Individual ( i ): ')

		if tam == 't':
			precioActual += 580
			tam = 'Triple'
		elif tam == 'd':
			precioActual += 430
			tam = 'Doble'
		elif tam == 'i':
			precioActual += 280
			tam = 'Individual'
		else:
			print('=> Debe seleccionar el tamaño correcto!!')
			continue

		break


	# Imprimir ingredientes
	print("\nIngredientes:")

	for ingrediente in ingredientes:
		print(f'{ ingredientes[ingrediente]["nombre"] }\t({ ingrediente })')
	
	print()

	# Aca se alamcenará el ingrediente seleccionado
	ing = 'ingredientes'

	# Acá armamos el string de la orden
	orden = 'sándwich ' + tam + ' con '

	# Bandera para saber si se escoge algún ingrediente
	banIng = False

	# Ciclo que se encarga de pedir ingredientes hasta precionar enter
	# SE NECESITA VALIDAR QUE SE INTRODUZCAN INGREDIENTES VÁLIDOS
	while ing != '':
		ing = input("Indique ingrediente (enter para terminar): ")

		if ing:
			precioActual += ingredientes[ing]["precio"]
			orden += ingredientes[ing]["nombre"] + ", "
			banIng = True

	# Acá se quita la coma del string si se seleccionarion ingredientes
	# Si no, se añade que solo es de Queso
	if banIng:
		orden = orden[:-2]
	else:
		orden += 'Queso'

	# Imprimir orden
	print(f'\nUsted seleccionó un { orden } \n')
	print(f'Subtotal a pagar por un { orden }: { precioActual }\n')
	print('*******************')

	# Se suma el precio del sandwich individual al total
	precioTotal += precioActual

	continuar = input('¿Desea continuar [s/n]?: ')

	# Si se presiona 'n', se muestra el total y termina el programa
	if continuar == 'n':
		print('*******************')
		print(f'EL pedido tiene un total de { cont + 1 } sandwich(es) por un monto de { precioTotal }\n')
		print('Gracias por su compra, regrese pronto.')
		break

	cont += 1
