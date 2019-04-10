def opcion1():
    print("Opcion 1 en funcion")

def switch(argument):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: opcion1(),
        12: "Diciembre"
    }
    fun = switcher.get(argument, "Dato Invalido")
    return fun



switch(11)