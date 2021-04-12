import random
from algoritmos import *

SOLUCION = genera_solucion()
RESTRICCIONES = genera_restricciones(5)

print(SOLUCION) 
print(RESTRICCIONES)

print(fuerzaBruta(SOLUCION))
solve()
