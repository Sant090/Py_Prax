#basico de funciones 

"""
def suma_de_elementos1(x,y):
    print("caso 1")

print(suma_de_elementos1(5,7))#retorna none


def suma_de_elementos(x,y):
    print("caso 2")
    return x+y




print(suma_de_elementos(5,7))#retorna la suma 

"""
"""
#Ambito LEGB 
#local
def numeros():
    numero1=1
    return numero1

print(numeros)#retorno numero 1
print(numero1)#error, variable local de la funcion afuera 

"""
"""
#ambito envolvente (funcion entre funcion)

def suma_de_elemento():
    elemento=10

    def imprimir_elemento():
        print(elemento)

    imprimir_elemento()

suma_de_elemento()
"""
