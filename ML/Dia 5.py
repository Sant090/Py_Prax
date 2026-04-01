
"""
import numpy as np

y_real = np.array([100, 120, 130])
y_pred = np.array([90, 110, 140])

error = np.mean((y_real - y_pred)**2)

print(error)

"""

import numpy as np
from sklearn.linear_model import LinearRegression

# datos
X = np.array([[10], [20], [30], [40]])
y = np.array([101, 202, 303, 404])

# modelo
modelo = LinearRegression()

# entrenamiento
modelo.fit(X, y)

# predicción
pred = modelo.predict([[1]]) #valor a predecir resultado

print(pred)