"""
normalizacion
"""

import numpy as np
from sklearn.linear_model import LinearRegression


# modelo
modelo = LinearRegression()

# entrenamiento
modelo.fit(X, y)

scaler = StandardScaler()   #predeterminado
X_scaled = scaler.fit_transform(X)  #todos los datos poseen una misma importancia


#convierte casos en probabilidad (0 a 1)

modelo = LogisticRegression()
modelo.fit(X, y)

pred = modelo.predict(X)


#clasificacion por vecinos

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

pred = modelo.predict(X)