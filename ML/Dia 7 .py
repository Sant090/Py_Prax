import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# datos simulados
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([100, 150, 200, 250, 300])

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

plt.scatter(X, y)
plt.plot(X, y_pred)
plt.show()



modelo = LogisticRegression()
modelo.fit(X, y)

pred = modelo.predict(X)

plt.scatter(X, y)
plt.plot(X, pred)
plt.show()


modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

pred = modelo.predict(X)

plt.scatter(X, y)
plt.plot(X, pred)
plt.show()