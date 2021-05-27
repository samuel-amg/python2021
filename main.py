import time
from modulos.menus import pedirSandwich, imprimirIngredientes
from modulos.clear import clear
from modulos.modulosIngredientes.diccionarioIngredientes import importarDiccionario

# Inicializamos variables
precioTotal = 0
cont = 0
ingredientes=importarDiccionario()

# Ciclo While principal
while True:
	precioActual = 0
	aux = pedirSandwich(precioActual, precioTotal, cont)
	precioActual = aux[0]
	tam = aux[1]

	# Aca se almacenará el ingrediente seleccionado
	ing = 'ingredientes'

	# Acá armamos el string de la orden
	orden = 'sándwich ' + tam + ' con '

	# Bandera para saber si se escoge algún ingrediente
	banIng = False

	# Ciclo que se encarga de pedir ingredientes hasta presionar enter
	while ing != '':
		imprimirIngredientes(ingredientes)
		print(f'Subtotal a pagar por un sandwich { tam }: { precioActual }')
		ing = input("Indique ingrediente (enter para terminar): ")

		# En caso de ingresar (e) la pantalla vuelve al menu anterior y despues 
		# de seleccionar el sandwich continua al menu de imprimir cliente
		if ing == 'e':
			precioActual = 0
			aux = pedirSandwich(precioActual, precioTotal, cont)
			precioActual = aux[0]
			tam = aux[1]
			continue
		# Ingreso normal de ingredientes
		elif ing in ingredientes:
			precioActual += ingredientes[ing]["precio"]
			orden += ingredientes[ing]["nombre"] + ", "
			banIng = True
		# Validación de ingrediente ingresado
		elif ing != '':
			clear()
			input("Por favor ingrese un ingrediente válido, asegurese de ingresar la etiqueta de \n"\
				"dos letra provista dentro del parentesis en la lista. Ingrese cualquier tecla para continuar.")
			continue
		
		

	# Acá se quita la coma del string si se seleccionarion ingredientes
	# Si no, se añade que solo es de Queso
	if banIng:
		orden = orden[:-2]
	else:
		orden += 'Queso'

	# Se suma el precio del sandwich individual al total
	precioTotal += precioActual

	# Imprimir orden
	print(f'\nUsted seleccionó un { orden } \n')
	print(f'Total a pagar: { precioTotal }\n')
	print('**************************')

	continuar = input('¿Desea continuar [s/n]?: ')

	# Si se presiona 'n', se muestra el total y termina el programa
	if continuar == 'n':
		print('**************************')
		print(f'El pedido tiene un total de { cont + 1 } sandwich(es) por un monto de { precioTotal }\n')
		print('Gracias por su compra, regrese pronto.')
		break

	cont += 1
