"""recibe una lista con cualquier tipo de datos

intenta convertir cada elemento a float

ignora los inválidos

devuelve una lista solo con los valores válidos

NO imprime

NO usa input()
datos = ["1.2", "a", 3, None, "4.5"]
def listas(a):
    b=[]
    for valor in a:
        try:
            b.append(float(valor))
        except TypeError:
            None
        except ValueError:
            None
    return b
           
lista=listas(datos)
print(lista)"""

def listas(a):
    b=[]
    for valor in a:
        try:
            b.append(float(valor))
        except TypeError:
            None
        except ValueError:
            None
    return b

def seguro(a):
    temp=listas(a)
    sorted(temp)
    return temp[-1]

def promedio(a):
    y=0
    for x in a:
        y+=x
    return y/len(a)
    
    
def programa(a):
    resultado=dict(promedio=promedio(a),maximo=seguro(a))
    return resultado

lista=[]
contador=0
while True:
    try:
        largo=int(input("cuantos elementos va a agregar a la lista: "))
        break
    except ValueError:
        print("el valor ingresado es erroneo, solo ingrese un valor numerico")

while not largo == contador:
    try:
        temp=int(input(f"agregue el valor del elemento {contador+1}: "))
        lista.append(temp)
        contador+=1
    except ValueError:
        print("el valor ingresado es erroneo, solo ingrese un valor numerico")
        
print(programa(lista))
