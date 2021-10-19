import hashlib # Importamos la librería que nos va a permitir cambiar la contraseña a formato Hash

listaValores = [] # Lista que almacenará los valores
diccionarioValores = {} # Diccionario que almacenará los valores

# Almacenamos los usuarios con sus respectivas contraseñas en la lista
listaValores.append(["usuario1", hashlib.new("sha1", b"pass1")]) # Añadimos una lista que contiene el usuario y la contraseña Hash
listaValores.append(["usuario2", hashlib.new("sha1", b"pass2")])
listaValores.append(["usuario3", hashlib.new("sha1", b"pass3")])
listaValores.append(["usuario4", hashlib.new("sha1", b"pass4")])
listaValores.append(["usuario5", hashlib.new("sha1", b"pass5")])

# Almacenamos los usuarios con sus respectivas contraseñas en el diccionario
diccionarioValores.setdefault("usuario1", hashlib.new("sha1", b"pass1")) # Añadimos la clave(nombre del usuario) con el valor (contraseña Hash)
diccionarioValores.setdefault("usuario2", hashlib.new("sha1", b"pass2"))
diccionarioValores.setdefault("usuario3", hashlib.new("sha1", b"pass3"))
diccionarioValores.setdefault("usuario4", hashlib.new("sha1", b"pass4"))
diccionarioValores.setdefault("usuario5", hashlib.new("sha1", b"pass5"))

# Imprimos dos valores de la lista y dos del diccionario
print("Valores de la lista: ")
print(listaValores[0])
print(listaValores[1])

print("\n") # Imprimimos un salto de línea para poder visualizar de una forma más clara los valores

print("Valores del diccionario: ")
print("usuario1 -> " + str(diccionarioValores.get("usuario1")))
print("usuario2 -> " + str(diccionarioValores.get("usuario2")))