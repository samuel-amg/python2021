from modulos.clear import clear
from modulos.modulosIngredientes.diccionarioIngredientes import ingredientes

# Inicializamos variables
precioTotal = 0
cont = 0

# Ciclo While principal
while True:

	clear()

	print("**************************\n"\
		  "*    SANDWICHES UCAB     *\n"\
		  "**************************\n")

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
	def imprimirIngredientes():
		print("\nIngredientes:")

		for i in ingredientes:
			print(f'{ ingredientes[i]["nombre"] }\t({ i })')
		
		print()

	imprimirIngredientes()

	# Aca se almacenará el ingrediente seleccionado
	ing = 'ingredientes'

	# Acá armamos el string de la orden
	orden = 'sándwich ' + tam + ' con '

	# Bandera para saber si se escoge algún ingrediente
	banIng = False

	# Ciclo que se encarga de pedir ingredientes hasta presionar enter
	while ing != '':
		ing = input("Indique ingrediente (enter para terminar): ")

		if ing in ingredientes:
			precioActual += ingredientes[ing]["precio"]
			orden += ingredientes[ing]["nombre"] + ", "
			banIng = True
		# Validación de ingrediente ingresado
		else:
			clear()
			print("Por favor ingrese un ingrediente válido, asegurese de ingresar la etiqueta de \n"\
				"dos letra provista dentro del parentesis en la lista.")
			imprimirIngredientes()
		
		

	# Acá se quita la coma del string si se seleccionarion ingredientes
	# Si no, se añade que solo es de Queso
	if banIng:
		orden = orden[:-2]
	else:
		orden += 'Queso'

	# Imprimir orden
	print(f'\nUsted seleccionó un { orden } \n')
	print(f'Subtotal a pagar por un sandwich { tam }: { precioActual }\n')
	print('**************************')

	# Se suma el precio del sandwich individual al total
	precioTotal += precioActual

	continuar = input('¿Desea continuar [s/n]?: ')

	# Si se presiona 'n', se muestra el total y termina el programa
	if continuar == 'n':
		print('**************************')
		print(f'El pedido tiene un total de { cont + 1 } sandwich(es) por un monto de { precioTotal }\n')
		print('Gracias por su compra, regrese pronto.')
		break

	cont += 1
