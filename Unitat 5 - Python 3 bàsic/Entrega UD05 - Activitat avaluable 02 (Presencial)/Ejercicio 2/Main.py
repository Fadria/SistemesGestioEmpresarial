# Función para validar un sudoku
def esSudokuCorrecto(miArrayBi):
    for i in range(9): # 9 porque son los valores por fila y columna del sudoku
        valor = miArrayBi[i][i] # Guardamos cada valor en diagonal
        
        # Comparamos el valor de izquierda a derecha y de arriba a abajo
        for j in range(9):
            if(j != i): # Comprobamos que no comparemos el número consigo mismo

                # Repetimos números en la misma columna o fila, el sudoku es incorrecto
                if valor == miArrayBi[j][i] or valor == miArrayBi[i][j]:
                    return False # Devolvemos false
    # Si recorremos todo el Sudoku y no hemos detectado repeticiones indicamos que es válido
    return True

'''
    Bucle doble, comparamos la posición 0 0 con 1 0 - 2 0, etc
'''

listaBidimensional = [] # Variable donde almacenaremos nuestro sudoku en forma de lista bidimensional

'''
    En el directorio del ejercicio disponemos de otro fichero con un sudoku incorrecto que nos
    ha servido para comprobar el correcto funcionamiento del ejercicio.
'''
fichero = open("Sudoku.in") # Abrimos el fichero que contiene el sudoku
for linea in fichero:
    linea = linea.replace("\n", "") # Eliminamos el salto de línea de la cadena
    listaBidimensional.append(list(linea.split(" "))) # Añadimos la linea como una cadena de números

print("El Sudoku validado es: " + str(esSudokuCorrecto(listaBidimensional))) # True