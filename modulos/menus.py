import time
from modulos.clear import clear
# Cabecera del menu
def header():
	 	print("**************************\n"\
		  "*    SANDWICHES UCAB     *\n"\
		  "**************************\n")


# Imprimir ingredientes

def imprimirIngredientes(ingredientes):
    clear()
    header()
    print("\nIngredientes:")

    for index, ingrediente in enumerate(ingredientes):
        print(f'{ ingrediente["name"] }\t({ index })')
    print("Volver al menu anterior (e)")
    print()

# Menu para seleccionar el tamaño del sandwich

def pedirSandwich(precioActual, precioTotal, cont):
    # Ciclo para preguntar el tamaño del sandwich
	# En caso de error, se repite
	while True:
		clear()
		header()
		print(f'Sandwich número {cont + 1}\nMonto actual a pagar: {precioTotal}')
		print('Opciones:')
		tam = input(f'\nTamaños:  Triple ( t ) Doble ( d ) Individual ( i ): ')

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
			input('=> Debe seleccionar el tamaño correcto!! Ingrese cualquier tecla para continuar')
			continue
		
		return([precioActual, tam])