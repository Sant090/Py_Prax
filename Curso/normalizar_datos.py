import pandas as pd
from pathlib import Path

#importamos la libreria para normalizar los datos
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

#cargamos datos
df=pd.read_csv(Path("datasets/Normalizacion.csv"))

#activador para normalizar los datos
scaler = MinMaxScaler()
df["normalizado"] = scaler.fit_transform(df[["Viento"]])

#activador 2 para estandarizar los datos
scaler2 = StandardScaler()
df["estadarizado"] = scaler2.fit_transform(df[["Viento"]])

#activador 3 para escalar datos
scaler3 = RobustScaler()
df["escalado"] = scaler3.fit_transform(df[["Viento"]])

print(df)

#revertir 

df["revertido"] = scaler.inverse_transform(df[["normalizado"]])
df["revertido2"] = scaler2.inverse_transform(df[["estadarizado"]])
df["revertido3"] = scaler3.inverse_transform(df[["escalado"]])

print(df)