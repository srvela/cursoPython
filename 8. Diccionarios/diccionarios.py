# Definir un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = dict(nombre="Juan", edad=15)

# Obtener valores por su clave
diccionario["a"]

# En caso de ingresar una key que no se encuentre generara un error
diccionario["d"]

# Mejo usar el metodo get
diccionario.get("d")

# Recorrer un diccionario
for dato in diccionario:
    print(dato, ": ",diccionario[dato])

for llave, valor in diccionario.items():
    print(llave, ": ",valor)

# Devuelve una lista con tuplas que contienen clave y valor del diccionario
diccionario.items()

# Devuelve una lista con los keys del diccionario
diccionario.keys()

# Verificar si una key se encuentra dentro del diccionario
"a" in diccionario

# Añade un nuevo elemento al diccionario
diccionario.setdefault('f', 5)

# Elimina el valor de la key introducida y lo elimnina
diccionario.pop("a")

# Actualiza el valor de la key o en caso contrario crea una nueva key con su valor
diccionario.update({'c':4})

# Verifica si el valor se encuentra dentro del diccionario
2 in diccionario.values()

# Genera un diccionario con 2 objetos iteables del mismo tamño
dict(zip('abcd',[1,2,3,4]))

# Crea una copia del diccionario
copia = diccionario.copy()

# Limpia el diccionario
diccionario.clear()