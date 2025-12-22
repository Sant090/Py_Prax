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


    