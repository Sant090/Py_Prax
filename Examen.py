"""reciba un número n

imprima "positivo" si n > 0

"negativo" si n < 0

"cero" si n == 0
"""
"""
n=int(input("escriba el numero:"))

if n>0:
    print("positivo")
elif n<0:
    print("negativo")
elif n==0:
    print("cero")
else:
    None
"""

"""
Escribe una función llamada promedio(lista) que:

reciba una lista de números

devuelva el promedio

maneje el caso de lista vacía
"""
"""
def promedio():
    lista=[]
    repeticiones=int(input("Digite la cantidad de numeros a ingresar: "))
    if repeticiones<=0:
        print("ingrese un valor valido")
    else:
        prom=0
        contador=repeticiones
        while not contador==0:
            contador-=1
            valor=int(input("Ingrese el valor: "))
            lista.append(valor) 
        for num in lista:
            prom+=num
        prom=prom/repeticiones
        print(f"el promedio de la lista es equivale a: {prom}")

promedio()
"""
"""
mediciones = {
    "sensor1": [1.2, 1.3, 1.1],
    "sensor2": [0.9, 1.0, 1.1]
}


sensor1=mediciones.get("sensor1")
prom1,prom2=0,0
for x in sensor1:
    prom1+=x
    

prom1/=3
print(f"promedio del sensor 1 es {prom1}")

sensor2=mediciones.get("sensor2")

for x in sensor2:
    prom2+=x

prom2/=3
print(f"promedio del sensor 2 es {prom2}")"""


datos = [2.3, 2.5, 2.4, 5.8, 2.6]
datos_corregidos=[]
for x in datos:
    if x<4:
        datos_corregidos.append(x)
        print(datos_corregidos)
    else: None
prom=0
for num in datos_corregidos:
        print=(prom)
        prom+=num
prom=prom/4
print(f"el promedio de la lista es equivale a: {prom}")
