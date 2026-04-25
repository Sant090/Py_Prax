
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


import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Datos
X = np.array([[1,110], [2,120], [3,130], [4,140]])
y = np.array([100, 150, 200, 250])

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modelo
modelo = LinearRegression()
modelo.fit(X_scaled, y)

# Predicción
nuevo = scaler.transform([[5,150]])
pred = modelo.predict(nuevo)

print(pred)

"""revision github prueba"""