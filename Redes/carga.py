import torch
import torch.nn as nn
import numpy as np
import joblib

# Cargar scalers
scaler_x = joblib.load("Redes/scaler_x.pkl")
scaler_y = joblib.load("Redes/scaler_y.pkl")

# Crear modelo
modelo = nn.Sequential(
    nn.Linear(2,64),
    nn.SiLU(),
    nn.Linear(64,64),
    nn.SiLU(),
    nn.Linear(64,32),
    nn.SiLU(),
    nn.Linear(32,1)
)

# Cargar pesos
modelo.load_state_dict(torch.load("Redes/modelo.pt"))
modelo.eval()

# Datos nuevos
R = 500
V = 220


# Preprocesamiento
entrada = np.array([[np.log(R), np.log(V)]])
entrada = scaler_x.transform(entrada)
entrada = torch.tensor(entrada, dtype=torch.float32)

# Predicción
with torch.no_grad():
    pred = modelo(entrada)

# Deshacer transformaciones
pred_log = scaler_y.inverse_transform(pred.numpy())
potencia = np.exp(pred_log)

print(f"Potencia estimada = {potencia[0,0]:.2f} W")
print(f"Potencia real = {V**2/R:.2f} W")
print(f"  error porcentual = {abs((V**2/R - potencia[0,0]) / (V**2/R) * 100):8.2f}%")