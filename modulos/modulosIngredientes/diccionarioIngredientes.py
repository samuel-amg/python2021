# Definimos el diccionario de datos con los ingredientes del archivo .txt
ingredientes = {}

with open("modulos/modulosIngredientes/listaIngredientes.txt", encoding="utf-8") as f:
    for line in f:
        (abv,precio,nombre) = line.strip().split(",")
        ingredientes[str(abv)] = { 'precio': float(precio), 'nombre': str(nombre)}
