import numpy as np

#print(np.__version__)

a = np.array([10, 12, 14, 16, 18])

print(a.mean())
print(a.std())
print(a.max())
print(a.min())

v = np.array([110, 112, 111, 113, 150, 114])

def filtrar(a):
    lista=[]
    prom=np.mean(a)
    print(f"primer promedio {prom}")
    for x in a:
        if x > prom:
             lista.append(x)
             print(x)
        else:
            None
        
        y=np.array(lista)
        
    return y


x = np.array([50, 55, 60, 65, 70])

def normalizar(a):
    return (a-np.min(a))/(np.max(a)-np.min(a))
#print(normalizar(x))

ar=np.random.uniform(110, 120, 100)
print(ar)
print(ar.mean)
print(ar.max)
print(ar.std)

