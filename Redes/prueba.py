import pandas as pd 
import torch as th
import torch.nn as nn  
import numpy as np


df = pd.read_csv("Redes/p1.csv")


print(df)


X=df[["v","i","freq","temp"]]


Y= df[["pot"]]

# 3. ESCALADO DE DATOS (Crucial para que la red no explote)
X = X/ np.array([250.0, 50.0, 100.0, 100.0])
Y = Y / 5000.0



X = th.tensor(
    X.values,
    dtype=th.float32
)

Y = th.tensor(
    Y.values,
    dtype=th.float32
)


modelo=nn.Sequential(

    nn.Linear(4,16),

    nn.ReLU(),

    nn.Linear(16,8),

    nn.ReLU(),

    nn.Linear(8,1)

)

predicciones = modelo(X)
print(predicciones)


loss_fn = nn.MSELoss()
loss = loss_fn(predicciones, Y)
print(loss)

optimizer = th.optim.Adam(modelo.parameters(), lr=0.005)
#lr=0.01 es la tasa de aprendizaje, que determina qué tan rápido o lento el modelo ajusta sus pesos y sesgos durante el entrenamiento.





for i in range(1000):

    predicciones = modelo(X)

    loss = loss_fn(predicciones, Y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
predicciones = modelo(X)



# 7. Evaluar resultados des-escalados (Escala real)
predicciones_escaladas = modelo(X)
predicciones_reales = predicciones_escaladas.detach().numpy() * 5000.0

print("\n--- Resultados Finales ---")
print("Predicción (W):", predicciones_reales)
print("Valor Real (W):", Y)
print("Pérdida final (MSE escalado):", loss.item())


th.save(
    modelo.state_dict(),
    "modelo.pt"
)


modelo.load_state_dict(
    th.load("modelo.pt")
)