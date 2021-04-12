import random
from itertools import chain
from sources.data import sospechoso, arma, motivo, parteCuerpo, lugar, grupo
#-------------------------------Variables Globales--------------

SOLUCION = []
RESTRICCIONES = []
SOL_BACKTRACKING = []
COUNT = 0
TIP0 = 0
CARTA = 0
TEMPORAL = 0
NIVEL = 0

#-------------------------------Algoritmos de la Solucion--------------
def genera_solucion():
    solucion = [sospechoso[random.randint(0,len(sospechoso)-1)], arma[random.randint(0,len(arma)-1)], motivo[random.randint(0,len(motivo)-1)], parteCuerpo[random.randint(0,len(parteCuerpo)-1)], lugar[random.randint(0,len(lugar)-1)]]
    return solucion

def genera_restricciones(cantidad):
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

#-------------------------------Algoritmo Fuerza Bruta--------------

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


#-------------------------------Algoritmo Backtracking--------------

def is_valid(item):
    #revisa las restricciones
    #retorna true si es valido, false si no lo es
    if (item in chain(*RESTRICCIONES)):
        #si está esto retorna true
        #hace el brete de iteracion
        for i in RESTRICCIONES:
            if item in RESTRICCIONES[i]:
                if (RESTRICCIONES.index(item)==0):
                    if (RESTRICCIONES[1] in SOL_BACKTRACKING):
                        return False
                elif (RESTRICCIONES.index(item)==1):
                    if (RESTRICCIONES[0] in SOL_BACKTRACKING):
                        return False
    else:
        return True

def check_sol():
    global SOL_BACKTRACKING, TIP0, CARTA, COUNT, TEMPORAL, NIVEL
    if (SOL_BACKTRACKING == SOLUCION):
        return True
    else:
        TIP0 -= 1
        if (TEMPORAL < (len(grupo[TIP0])-1)):
            TEMPORAL += 1
            CARTA = TEMPORAL
            del SOL_BACKTRACKING[4-(COUNT-NIVEL):5]
        else:
            COUNT += 1         
            TIP0 -= COUNT
            #se usa item para encontrar el indice de la carta que entró a SOL_BACKTRACKING en ese tipo
            item = SOL_BACKTRACKING[TIP0]
            CARTA = SOL_BACKTRACKING[TIP0].index(item) + 1
            NIVEL += 1
            del SOL_BACKTRACKING[4-COUNT:5]
        print (TIP0, CARTA)
        
        solve()

def solve():
    #los datos son una lista de listas
    #se sabe que llegamos a un punto incorrecto cuando topamos con una restriccion que aplica
    #o llegamos al final de los tipos de cartas y la sol no es la correcta
    #se asume que siempre va a haber solucion, el asunto es llegar a ella
    #la sol se va creando paso a paso, inicia como una lista vacía

    #tipo corresponde al tipo de carta, para así usar una de cada tipo 
    global TIP0, CARTA, SOL_BACKTRACKING, TEMPORAL
    while (TIP0 < 5):
        if (is_valid(grupo[TIP0][CARTA])):
            SOL_BACKTRACKING.append(grupo[TIP0][CARTA])
            TEMPORAL = CARTA
            CARTA = 0
            TIP0 += 1
        else:
            CARTA += 1
    print (SOL_BACKTRACKING)
    check_sol()
    
        
