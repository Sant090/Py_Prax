import joblib
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

df=pd.read_csv("Redes/p2.csv")
df = df[df["p"] > 0]

df["log_r"] = np.log(df["r"])
df["log_v"] = np.log(df["v"])
x = df[["log_r","log_v"]]

df["log_p"] = np.log(df["p"])
y = df[["log_p"]]

xt,xe,yt,ye = train_test_split(x,y,test_size=0.2,random_state=42)

scaler_x = StandardScaler()
scaler_y = StandardScaler()

xt = scaler_x.fit_transform(xt)
yt = scaler_y.fit_transform(yt)

xe=scaler_x.transform(xe)
ye=scaler_y.transform(ye)

xt = torch.tensor(xt, dtype=torch.float32)
yt = torch.tensor(yt, dtype=torch.float32)
xe = torch.tensor(xe, dtype=torch.float32)
ye = torch.tensor(ye, dtype=torch.float32)


modelo = nn.Sequential(
    nn.Linear(2,64),
    nn.SiLU(),
    nn.Linear(64,64),
    nn.SiLU(),
    nn.Linear(64,32),
    nn.SiLU(),
    nn.Linear(32,1)
)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(
    modelo.parameters(),
    lr=0.001
)


epochs = 300
for epoch in range(epochs):
    pred = modelo(xt)
    loss = loss_fn(pred,yt)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch%50==0:
        print(epoch,loss.item())



modelo.eval()
with torch.no_grad():
    pred_test = modelo(xe)
    loss_test = loss_fn(pred_test,ye)
print("Loss prueba:",loss_test.item())
pred_log = scaler_y.inverse_transform(
    pred_test.numpy()
)

real_log = scaler_y.inverse_transform(
    ye.numpy()
)

pred_real = np.exp(pred_log)
Y_real = np.exp(real_log)



print("Primeras predicciones:")
for real,pred in zip(Y_real[:10],pred_real[:10]):

    print(

        f"Real = {real[0]:8.2f}   "

        f"Predicho = {pred[0]:8.2f}"

        f"  error porcentual = {abs((real[0] - pred[0]) / real[0] * 100):8.2f}%"
    )




torch.save(

    modelo.state_dict(),

    "Redes/modelo.pt"

)

joblib.dump(

    scaler_x,

    "Redes/scaler_X.pkl"
    
)

joblib.dump(

    scaler_y,

    "Redes/scaler_Y.pkl"

)

print()

print("Modelo guardado correctamente.")