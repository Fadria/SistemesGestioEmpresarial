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

'''
    Al realizar la petición a la API, obtenemos un número total de páginas. Esto se hace para no devolver 1000 personajes de golpe,
    por ejemplo. Por ello, haremos un bucle for que realice la petición para obtener los personajes de cada página y los mostraremos.
'''
numeroPaginas = data["info"]["pages"]


print("\nListado de personajes de la especie " + str(especie) + ":")

for i in range(1, numeroPaginas+1): # Mostraremos desde la página 1 hasta la última + 1, que correspondería a la última disponible
    data = requests.get(URL + "&page=" + str(i)) # Obtenemos la tira de personajes que corresponda en cada itineración
    data = data.json() # Convertimos la respuesta recibida en un diccionario

    try:
        for element in data["results"]: # Obtenemos el apartado results dentro de la respuesta de la API
            print(element['name']) #Accedemos a sus valores
    except:
        print("Se ha producido un error")