class Notes(object):
    
    def __init__(self, notas):
        self.notas = notas

    def mitjana(self):
        suma = 0
        for nota in self.notas:
            suma += self.notas[nota]
        return suma / len(self.notas)

    def mitjanaSenseNoms(self, listaProhibidos):
        suma = 0
        cont = 0
        for nota in self.notas:
            if nota not in listaProhibidos:
                suma += self.notas[nota]
                cont += 1
        return suma / cont        
        
    @staticmethod
    def numElementos(dicElementos):
        cont = 0
        for elemento in dicElementos:
            cont += 1
        return cont

dic = {"Pepito": 5, "Marcelo": 3, "Rafa": 7}
notas1 = Notes(dic)
lista1 = ["Pepito"]
print(notas1.mitjana())
print(notas1.mitjanaSenseNoms(lista1))
print(Notes.numElementos(dic))