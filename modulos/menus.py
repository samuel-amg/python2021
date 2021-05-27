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

    for i in ingredientes:
        print(f'{ ingredientes[i]["nombre"] }\t({ i })')
    print("Volver al menu anterior (e)")
    print()

# Menu para seleccionar el tamaño del sandwich

def pedirSandwich(precioActual, precioTotal):
    # Ciclo para preguntar el tamaño del sandwich
	# En caso de error, se repite
	while True:
		clear()
		header()
		tam = input(f'Monto actual a pagar: {precioTotal} \nTamaños:  Triple ( t ) Doble ( d ) Individual ( i ): ')

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