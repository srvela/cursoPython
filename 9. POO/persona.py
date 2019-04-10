# Clase mas basica.
class Clase:
    pass


#clase principal
class Persona:
    #Constructor de la clase
    def __init__(self, identificacion, nombre, apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    def datos(self):
        return " {}: {}, {}".format(str(self.identificacion), self.apellido, self.nombre)

# Clase que hereda la clase persona
class Alumno(Persona):

    def __init__(self, identificacion, nombre, apellido, control):
        "Constructor de AlumnoFIUBA"
        # llamamos al constructor de Persona
        super().__init__(identificacion, nombre, apellido)
        # agregamos el nuevo atributo
        self.control = control
    def datos(self):
        return " {}: {}, {}".format(str(self.control), self.nombre, self.apellido)
    
"""
# Creamos un objeto Alumnos y lo imprimimos
a = Alumno(1234,"abelardo", "barron", 14141085)
print(a.datos())
""" 





