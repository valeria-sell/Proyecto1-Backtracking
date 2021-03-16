import random

sospechoso = ['mejor amigo/a', 'novio/a', 'vecino/a', 'mensajero/a', 'extranio/a', 'hermanastro/a', 'colega del trabajo']
arma = ['pistola', 'cuchillo', 'machete', 'pala', 'bate', 'botella', 'tubo', 'cuerda']
motivo = ['venganza', 'celos', 'dinero', 'accidente', 'drogas', 'robo']
parteCuerpo = ['cabeza', 'pecho', 'abdomen', 'espalda', 'pierna', 'brazo']
lugar = ['sala', 'comedor', 'banio', 'terraza', 'cuarto', 'garage', 'patio', 'balcon', 'cocina']

grupo = [sospechoso, arma, motivo, parteCuerpo, lugar]

def solucion():
    sol = [sospechoso[random.randint(0,len(sospechoso)-1)], arma[random.randint(0,len(arma)-1)], motivo[random.randint(0,len(motivo)-1)], parteCuerpo[random.randint(0,len(parteCuerpo)-1)], lugar[random.randint(0,len(lugar)-1)]]
    return sol

def restricciones(cantidad):
    restr = ['']*cantidad
    i=0
    while (i<cantidad):
        cero,uno = random.randint(0,len(grupo)-1), random.randint(0,len(grupo)-1)
        if cero != uno:
            dos = grupo[cero][random.randint(0,len(grupo[cero])-1)]
            tres = grupo[uno][random.randint(0,len(grupo[uno])-1)]
            restr[i] = [dos,tres]
            i+=1
        else:
            i-=1
    return restr

print(solucion())
print(restricciones(3))