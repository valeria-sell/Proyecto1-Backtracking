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

def validacion(solucion, restricciones):
    for i in restricciones:
        mismas_cartas = set(solucion) & set(i)
        if(len(mismas_cartas)>1):
            return False
    return True

def fuerzaBruta(solucion):
    respuesta = ['']*5
    for i in sospechoso:
        respuesta[0] = i
        for j in arma:
            respuesta[1] = j
            for k in motivo:
                respuesta[2] = k
                for l in parteCuerpo:
                    respuesta[3] = l
                    for m in lugar:
                        respuesta[4] = m
                        if(respuesta == solucion):
                            return respuesta

sol = solucion()
print(sol)
#print(restricciones(3))
print(fuerzaBruta(sol))