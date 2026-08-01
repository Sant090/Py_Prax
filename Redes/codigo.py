import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("Redes/p1.csv")

x = df[["v","i","freq"]]
y= df[["pot"]]


xt,xe,yt,ye = train_test_split(x,y,test_size=0.2,random_state=42)


scaler_x = StandardScaler()
scaler_y= StandardScaler()


xe=scaler_x.fit_transform(xe)
ye=scaler_y.fit_transform(ye)

xt = scaler_x.transform(xt)
yt = scaler_y.transform(yt)

xe = torch.tensor(
    xe,
    dtype=torch.float32
)

ye = torch.tensor(
    ye,
    dtype=torch.float32
)
xt = torch.tensor(
    xt,
    dtype=torch.float32
)

yt = torch.tensor(
    yt,
    dtype=torch.float32
)


modelo = nn.Sequential(

    nn.Linear(3,16),

    nn.ReLU(),

    nn.Linear(16,8),

    nn.ReLU(),

    nn.Linear(8,1)

)


#para prediccion

loss_fn = nn.MSELoss()

optimizer = torch.optim.Adam(

    modelo.parameters(),

    lr=0.001

)


#entrenamiento

epochs = 500

for epoch in range(epochs):

    pred = modelo(xt)

    loss = loss_fn(pred,yt)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if epoch%50==0:

        print(epoch,loss.item())



#evalua

modelo.eval()

with torch.no_grad():

    pred_test = modelo(xt)

    loss_test = loss_fn(pred_test,yt)

print()

print("Loss prueba:",loss_test.item())


#normaliza

pred_real = scaler_y.inverse_transform(

    pred_test.numpy()

)

Y_real = scaler_y.inverse_transform(

    yt.numpy()

)

print()

print("Primeras predicciones:")

for real,pred in zip(Y_real[:10],pred_real[:10]):

    print(

        f"Real = {real[0]:8.2f}   "

        f"Predicho = {pred[0]:8.2f}"

    )



#guardar

torch.save(

    modelo.state_dict(),

    "modelo.pt"

)

joblib.dump(

    scaler_x,

    "scaler_X.pkl"

)

joblib.dump(

    scaler_y,

    "scaler_Y.pkl"

)

print()

print("Modelo guardado correctamente.")