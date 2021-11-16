import requests  # Librería que nos va a permitir hacer la petición con la API

# Pedimos al usuario la especie que desea buscar
print("Por favor, indique la especie que desea buscar: ") # Una especie válida sería human
especie = input()

# Informamos al usuario de que estamos contactando con la API y de que debe esperar a que finalicemos el proceso
print("Contactando con la API")
print("Un momento, por favor...") 

# URL a la que realizaremos la petición, contiene la especie introducida por el usuario
URL = 'https://rickandmortyapi.com/api/character/?species='+str(especie) #configuramos la url

#solicitamos la información y guardamos la respuesta en la variable data
data = requests.get(URL) 

data = data.json() # Convertimos la respuesta recibida en un diccionario

try:
    print("\nListado de personajes de la especie " + str(especie) + ":")
    for element in data["results"]: #iteramos sobre data
        print(element['name']) #Accedemos a sus valores
except:
    print("No se han encontrado personajes de la especie " + str(especie))