"""
recibir una lista de números (mediciones)

recibir un valor mínimo y máximo

devolver una nueva lista solo con los valores válidos

NO imprimir nada

NO usar input()

mediciones = [110, 115, 500, 112, 0, 118]
filtradas = filtrar_mediciones(mediciones, 100, 130)
"""
"""
mediciones_dadas = [110, 115, 500, 112, 0, 118]
medicione_finales=[]

def filtrado(mediciones,v_min,v_max):
    for x in mediciones:
        if not x < v_min or x >v_max:
            medicione_finales.append(x)
    return medicione_finales

filtro=filtrado(mediciones_dadas,100,130)
"""
"""
La función debe:

devolver el promedio de la lista

si la lista está vacía, devolver None

NO imprimir

NO pedir input

"""

"""
def promedio(lista):
    prom=0
    if not len(lista)==0:
        for x in lista:
            prom+=x
        return prom/len(lista)
    else: 

        return print("Lista vacia")

"""
"""

Escribe código que:

Defina una lista de mediciones

Use filtrar_mediciones

Use promedio_seguro

Imprima el resultado final
"""
def promedio(lista):
    prom=0
    if not len(lista)==0:
        for x in lista:
            prom+=x
        return prom/len(lista)
    else: 

        return None
    

def filtrado(mediciones,v_min,v_max):
    medicione_finales=[]
    for x in mediciones:
        if not x < v_min or not x >v_max:
            medicione_finales.append(x)
    return medicione_finales



lista=[]
repet=int(input("Ingrese la cantidad de mediciones"))
while not repet ==0:
    repet-=1
    valor=int(input("ingrese la medicion: "))
    lista.append(valor)

print(lista)
print(promedio(lista))
print(filtrado(lista,100,200))