lista = []

lista = [1,2,3,4, "hola",[12,34]]

# Recorrer por su elemento
for a in lista:
    print(a)

# Recorrer por su indice
for indice in range(0,len(lista)):
    print(lista[indice])

# al final de la lista
lista.append("dato")

# En el indice especificado
lista.insert(0,"Dato 2")

# Eliminia el primer elemento que
lista.remove(1)

# Elimina el itmen dado su indice y devuelve ese valor
a = lista.pop()

# Devuelve el indice del valor dado
lista.index(4)

# Cuenta las coincidencias del parametro
lista.count(1)

# Ordena los elementos de la lista
lista.sort()

# Invierte los items de la lista
lista.reverse()

# Crea una copia de la lista 
a = lista.copy()
a = lista[:]

# Limpia la lista eliminando todos sus datos
lista.clear()










