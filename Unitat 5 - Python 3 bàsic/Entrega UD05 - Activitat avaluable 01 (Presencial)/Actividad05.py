import sys

# Comando ejecutado -> python.exe .\Actividad05.py HolaPython BuenasTardes
print("Parámetros consola -> " + str(sys.argv) + "\n\n") # ['.\\Actividad05.py', 'HolaPython', 'BuenasTardes']

def leerParametros(*args):
    print("Parámetros función -> " + str(args))

# Enviamos diferentes parámetros a la función
leerParametros(1, 2, 3, 4, 5, ["5", "6"], "HolaPython") # Muestra cada parámetro
leerParametros() # No muestra nada y no da error