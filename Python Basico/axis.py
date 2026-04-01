import numpy as np
"""
sensores = np.array([
    [110, 112, 111],
    [113, 114, 112],
    [150, 113, 114]
])

prom_sensor = np.mean(sensores, axis=1)
print(prom_sensor)
"""
ar=np.array([[13,14,11,10,11],[10,11,14,13,11],[11,13,9,8,11]])
"""
print(ar)
print(np.shape(ar))
print(ar[2,:])
print(ar[:,3])

"""

print(np.mean(ar,1))# la sumatoria de los elementos de cada valor de cada sensor y la division por la cantidad de elementos

print(np.mean(ar,0))# la sumatiria de todos los elementos en una posicion x de cada una de los array y division por cantidad de elementos


print(np.max(ar,1))

print(np.max(ar,0))


print(np.mean(ar))
print(ar[ar>np.mean(ar)])
print((ar-np.min(ar))/((np.max(ar))-(np.min(ar))))


)