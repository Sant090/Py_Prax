import numpy as np

t=np.linspace(0,10,1000)

X = []
y = []

for a in range(100):
    ruido = np.random.normal(0, 0.2, len(t))
    senal = np.sin(2*np.pi*60*t) + ruido

    X.append(senal)
    y.append(0)  # normal

for a in range(100):
    ruido = np.random.normal(0, 0.8, len(t))
    senal = np.sin(2*np.pi*60*t) + ruido

    X.append(senal)
    y.append(1)  # falla

X = np.array(X)
y = np.array(y)


features = []

for senal in X:
    f = [
        np.mean(senal),
        np.var(senal),
        np.max(senal)
    ]
    features.append(f)

X_features = np.array(features)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X_features, y, test_size=0.2
)

# modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)


from sklearn.metrics import accuracy_score

y_pred = modelo.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# nueva señal
ruido = np.random.normal(0, 0, len(t))
nueva = np.sin(2*np.pi*60*t) + ruido

# extraer features
f_nueva = np.array([[
    np.mean(nueva),
    np.var(nueva),
    np.max(nueva)
]])

pred = modelo.predict(f_nueva)

print("¿Falla?", pred)