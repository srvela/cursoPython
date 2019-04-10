# https://docs.sympy.org/latest/index.html

from sympy import *
x, y, z, t = symbols('x y z t')

# Derivar
derivada = diff(cos(x), x)
print(derivada)

# Integrar
integral = integrate(cos(x),x)

# Calcular limites
limite = limit(sin(x)/x, x, 0)