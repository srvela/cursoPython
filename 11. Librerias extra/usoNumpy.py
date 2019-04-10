# http://www.numpy.org/

import numpy as np

# Crea una matriz de 3 renglones con 5 columnas 
# con los numeros del 0 al 14
a = np.arange(15).reshape(3, 5)

# Genera una sucecion de numeros del 0 al 2 con paso de 0.3
a = np.arange( 0, 2, 0.3 ) 

# Genera una sucecion de 9 numeros del 0 al 2
a = np.linspace( 0, 2, 9 )

# Se pueden realizar operaciones con las matrices 
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )

# Producto elemento por elemento 
A * B

# Producto matricial
A @ B 
A.dot(B)