# Función usada para cambiar cada valor por 0
def devolver0(num):
    return 0
# Función usada para contar las minas adyacentes en cada posición del array
def contandoMinas(miCampo):


    for i in range(len(miCampo)): # Cada línea del buscaminas
        for j in range(len(miCampo[i])): # Cada valor de la línea
            if miCampo[i][j] != -1:

                # Hay una mina en la parte superior izquierda
                if i > 0 and j > 0:
                    if miCampo[i-1][j-1] == -1:
                        miCampo[i][j] += 1
                
                # Hay una mina en la parte superior
                if i > 0:
                    if miCampo[i-1][j] == -1:
                        miCampo[i][j] += 1

                # Hay una mina en la parte izquierda
                if j > 0:
                    if miCampo[i][j-1] == -1:
                        miCampo[i][j] += 1

                '''
                    Hay una mina en la parte inferior izquierda.
                    Comprobamos que i+1 es menor a la longitud del campo para poder comprobar si es la última fila
                '''
                if i+1 < len(miCampo) and j > 0 and miCampo[i+1][j-1] == -1:
                    miCampo[i][j] += 1

                # Hay una mina en la parte inferior
                if i+1 < len(miCampo) and miCampo[i+1][j] == -1:
                    miCampo[i][j] += 1

                '''
                    Hay una mina en la parte superior derecha.
                    Comprobamos hay campos tanto arriba como a la derecha de la posición.
                '''
                if i>0 and j+1 < len(miCampo) and miCampo[i-1][j+1] == -1:
                    miCampo[i][j] += 1

                # Hay una mina en la parte derecha
                if j+1 < len(miCampo[i]) and miCampo[i][j+1] == -1:
                    miCampo[i][j] += 1

                # Hay una mina en la parte inferior derecha
                if i+1 < len(miCampo) and j+1 < len(miCampo[i]) and miCampo[i+1][j+1] == -1:
                    miCampo[i][j] += 1
    return miCampo

# Array que contiene nuestro buscaminas, los valores -1 nos indican que en esa posición, tendríamos una mina
arrayBidimensional = [[0, 0, -1, 0], [0, -1, -1, 0]]

arrayResultado = contandoMinas(arrayBidimensional)
print(arrayResultado)