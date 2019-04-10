# Funcion que no devuelve nada, solo realiza operaciones
def funcion(parametro):
    print("Se recibio el parametro: "+ str(parametro))

# Funcion que devuelve un valor
def funcion2(parametro):
    return str(parametro) + " Texto agregado."

#Funcion que devuelve multiples valores
def funcion3():
    a = 1
    b = 2
    c = 3
    return a, b, c

funcion("hola")

print(funcion2(1234))

a, _ , b = funcion3()