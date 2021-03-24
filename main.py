import random
from algoritmos import genera_solucion, genera_restricciones, fuerzaBruta

solucion = genera_solucion()
restricciones = genera_restricciones(3)  

print(solucion)
print(restricciones)
print(fuerzaBruta(solucion))