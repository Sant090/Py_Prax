
"""
repaso basico
"""
print("hello")
x=10    #entero
y=10.5  #float

if x > 5 :  #condiciones
    print("numero mayor a 5")


for i in range(5):  #bucles
    print(i+1)

while x > 13:
    print(1)


def cuadrado(x):
    return x**2

"""
ejercicio, funcion que calcule resistencia y potencia maxima
"""

def resistencia(v,i):
    return v*i , v/i










"""
Funcion de potencia electrica promedio
"""
def Pel(V,I):
    if len(V) == (I):
        temp=0
        for i in range(len(V)):
            temp+=V[i]*I[i]
        return temp/len(V)
    else:
        return "Por cada voltaje no hay una corriente"
