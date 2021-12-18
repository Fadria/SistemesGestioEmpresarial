import random

def realitzaTirada(pPie, pPap, pTij):
    # Si no tenemos unas probablidades iguales a 100 no continuaremos
    if pPie + pPap + pTij == 100:
        numAleatorio = random.randint(0, 100)
        limite = pPie

        if(numAleatorio < limite):
            return 0 # Valor para piedra
        else:
            limite += pPap
            if(numAleatorio < limite):
                return 1 # Valor para papel
            else:
                return 2 # Valor para tijera
    else:
        print("Las probabilidades no suman 100 en total")

def jugaNPartides(n):

    ganadas = 0
    perdidas = 0
    empates = 0

    while n > 0:
        opcionJugador1 = realitzaTirada(30,30,40)
        opcionJugador2 = realitzaTirada(30,30,40)

        if(opcionJugador1 == opcionJugador2):
            empates += 1
            
        if(opcionJugador1 == 0 and opcionJugador2 == 1): perdidas += 1
        if(opcionJugador1 == 0 and opcionJugador2 == 2): ganadas += 1
        if(opcionJugador1 == 1 and opcionJugador2 == 0): ganadas += 1
        if(opcionJugador1 == 1 and opcionJugador2 == 2): perdidas += 1
        if(opcionJugador1 == 2 and opcionJugador2 == 0): perdidas += 1
        if(opcionJugador1 == 2 and opcionJugador2 == 1): ganadas += 1
        n = n -1

    return "Jugador1 " + str(ganadas) + " Jugador2 " + str(perdidas) + " Empates " + str(empates)

def comprobaProbabilitat(pPie, pPap, pTij, n):
    contPie = 0
    contPap = 0
    contTij = 0

    probRealPie = 0
    probRealPap = 0
    probRealTij = 0

    contador = n
    while contador > 0:
        if(realitzaTirada(pPie, pPap, pTij) == 0):
            contPie += 1
        else:
            if(realitzaTirada(pPie, pPap, pTij) == 1):
                contPap += 1
            else:
                contTij += 1
        contador = contador -1 
    
    probRealPie = contPie * 100 / n
    probRealPap = contPap * 100 / n
    probRealTij = contTij * 100 / n
    print("Porcentaje aportado: Piedra: " + str(pPie) + " Papel: " + str(pPap) + " Tijera: " + str(pTij))
    print("Porcentaje real: Piedra: " + str(probRealPie) + " Papel: " + str(probRealPap) + " Tijera: " + str(probRealTij))

print(realitzaTirada(30,30,40))
print(jugaNPartides(50))
comprobaProbabilitat(30, 30, 40, 5)