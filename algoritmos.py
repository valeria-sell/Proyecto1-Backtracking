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

#-------------------------------Algoritmos para la Solucion--------------
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

SOLUCION = genera_solucion()
RESTRICCIONES = genera_restricciones(40)

print(SOLUCION) 
print(RESTRICCIONES)

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
    try:
        #retorna true si es valido, false si no lo es
        for i in range(0, len(RESTRICCIONES)):
            if (item in RESTRICCIONES[i]):
                if (RESTRICCIONES.index(item)==0):
                    if (RESTRICCIONES[1] in SOL_BACKTRACKING):
                        print("RESTRICCION ENCONTRADA")
                        return False
                elif (RESTRICCIONES.index(item)==1):
                    if (RESTRICCIONES[0] in SOL_BACKTRACKING):
                        print("RESTRICCION ENCONTRADA")
                        return False
    except:
        return True
    return True

def index_jump(item_in_sol):
    global CARTA, TIP0, SOL_BACKTRACKING
    #se encarga de poner el indice en la siguiente opción correcta para el backtracking 
    #revisa del final hacia adelante, los itemes de SOL_BACKTRACKING
    #al entrar sabemos que el item de SOL_BACKTRACKING[4] es el ultimo item de grupo[lugar]
    #va a revisar un total de 4 veces maximo. 
    item_in_sol -= 1
    if (is_end(item_in_sol)):
        index_jump(item_in_sol)
    else:
        #se usa item para encontrar el indice de la carta del tipo a avanzar
        item = SOL_BACKTRACKING[item_in_sol]
        CARTA = (grupo[item_in_sol].index(item) + 1)
        TIP0 = item_in_sol
        del SOL_BACKTRACKING[item_in_sol:]

def is_end(index_check):
    check_len = len(grupo[index_check]) - 1
    item = SOL_BACKTRACKING[index_check]
    item_index = grupo[index_check].index(item)
    if (item_index == check_len):
        return True
    else:
        return False

def check_sol(long_solback):
    global TEMPORAL, CARTA, TIP0, SOL_BACKTRACKING
    #@param item_in_sol es nuestra posición en el conjunto solución, para comparar con las listas de datos
    item_in_sol = long_solback-1
    if (SOL_BACKTRACKING == SOLUCION):
        return True  
    else:
        #revisa si TEMPORAL está al final de la lista
        if (is_end(item_in_sol)): 
            #está al final de la lista, requiere salto de indice
            #procede a revisar las listas previas para así revisar cual requiere salto de indice
            index_jump(item_in_sol)
            solve()
        else:
            #no está al final de la lista, solo necesita avanzar al siguiente item
            TEMPORAL += 1
            CARTA = TEMPORAL
            TIP0 -=1 
            #borra el ultimo item de SOL_BACKTRACKING
            del SOL_BACKTRACKING[4:]
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
    check_sol(len(SOL_BACKTRACKING))