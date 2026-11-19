import torch 
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df=pd.read_csv("datasets/gta_sa_vehicle_stats.csv")
df2=pd.DataFrame({"Nombre del Vehiculo":df["identifier"],"velocidad_maxima(km/h)":df["max_velocity(km/h)"],"valor_monetario($)":df["monetary_value_($)"]})

x=df2[["valor_monetario($)"]]
y=df2[["velocidad_maxima(km/h)"]]

x_e, x_p, y_e, y_p = train_test_split(x, y, test_size=0.2, random_state=42)

scalex=StandardScaler()
scaley=StandardScaler()
x_scaled=scalex.fit_transform(x_e)
y_scaled=scaley.fit_transform(y_e)

tensorXe=torch.FloatTensor(x_scaled)
tensorYe=torch.FloatTensor(y_scaled)

tensorXp=torch.FloatTensor(scalex.transform(x_p))
tensorYp=torch.FloatTensor(scaley.transform(y_p))

#shuffle=True para mezclar los datos (entrenamiento) y shuffle=False para no mezclarlos (prueba)
train_loader=DataLoader(TensorDataset(tensorXe,tensorYe),batch_size=8,shuffle=True)
test_loader=DataLoader(TensorDataset(tensorXp,tensorYp),batch_size=8,shuffle=False)


# 5. Definir la Red Neuronal aplicando ReLU (o Tanh)
class RedVelocidad(nn.Module):
    def __init__(self):
        super().__init__()
        self.red = nn.Sequential(
            nn.Linear(1, 16),   # Entradas: 1 característica (valor monetario) -> 32 neuronas
            nn.ReLU(),          
            nn.Linear(16, 8),  
            nn.ReLU(),          
            nn.Linear(8, 1)    
        )
    #se define el método forward para pasar los datos a través de la red
    def forward(self, x):
        return self.red(x)



modelo = RedVelocidad()
criterio = nn.MSELoss()  # Error Cuadrático Medio (estándar para regresión)

#descenso de gradiente estocástico con Adam
#lr para la tasa de aprendizaje 
optimizador = torch.optim.Adam(modelo.parameters(), lr=0.01)

# 6. Entrenamiento
for epoch in range(150):
    modelo.train()
    for batch_x, batch_y in train_loader:
        optimizador.zero_grad()
        pred = modelo(batch_x)
        loss = criterio(pred, batch_y)
        loss.backward()
        optimizador.step()

# 7. Evaluación y vuelta a unidades reales (km/h)
modelo.eval()
with torch.no_grad():
    pred_escalada = modelo(tensorXp)
    # Invertir el escalado para ver la velocidad real en km/h
    pred_kmh = scaley.inverse_transform(pred_escalada.numpy())
    real_kmh = y_p.values

    for real, pred in zip(real_kmh[:5], pred_kmh[:5]):
        print(f"Real: {real[0]:.1f} km/h | Predicho: {pred[0]:.1f} km/h")
