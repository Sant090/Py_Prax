
"""
import numpy as np
import matplotlib as plt
a=np.array([1,1,1])
b=np.array([5,1,3])

print(np.dot(a,b))

v = np.array([120, 125, 130])
i = np.array([2, 2.1, 2.2])

print(v*i)

t=np.linspace(0,1,1000)
np.sin(2*np.pi*50*t)

plt.plot(t,v)
plt.ylabel("voltaje")
plt.xlabel("tiempo")
plt.title("graph")
plt.shot()


"""


from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Features: [frecuencia, amplitud]
X = np.array([
    [50, 1],
    [60, 1.2],
    [50, 0.9],
    [200, 3]
])

# 0 = normal, 1 = anomalía
y = np.array([0, 0, 0, 1])

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

pred = modelo.predict([[6000, 5000]])

print("Predicción:", pred)


"""revision git"""