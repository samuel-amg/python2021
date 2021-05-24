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
