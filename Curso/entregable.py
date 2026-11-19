
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


from sklearn.metrics import r2_score, mean_absolute_error


#Limpieza de datos y ordenamiento

df=pd.read_csv("datasets/GeneracionEspinalOrdenado.csv")

df2=pd.read_csv("datasets/ClimaEspinal.csv")
print(df2)

df3=pd.DataFrame({"Fecha y hora":df["FechaHora"],"Generacion":df["Valor"],"Irradiacion":df2["Irradiancia_Wm2"],"Temperatura":df2["Temperatura_C"],"Humedad":df2["Humedad_Relativa_%"]})
df3["Fecha y hora"] = pd.to_datetime(df3["Fecha y hora"])
df3['Fecha'] = df3['Fecha y hora'].dt.date
df3['Hora'] = df3["Fecha y hora"].dt.hour + df3["Fecha y hora"].dt.minute / 60.0

df3.info()

print(df3.isna().sum())

df3 = df3.dropna()

print(df3)


#modelo ml

Entradas = ['Irradiacion', 'Temperatura', 'Humedad',"Hora"]
x = df3[Entradas]

y = df3[['Generacion']]

x_e,x_p,y_e,y_p = train_test_split(x,y,test_size=0.2,random_state=67)

scalerx = MinMaxScaler()
scalery = MinMaxScaler()

scalerx_e = scalerx.fit_transform(x_e)
scalerx_p = scalerx.transform(x_p)
scalery_e = scalery.fit_transform(y_e)
scalery_p = scalery.transform(y_p)

modelo = LinearRegression()
modelo.fit(scalerx_e, scalery_e)

predicciones_escaladas = modelo.predict(scalerx_p)

predicciones_reales = scalery.inverse_transform(predicciones_escaladas)

"""

Entradas = ["Irradiacion", "Temperatura", "Humedad"]
x = df3[Entradas]
y = df3["Generacion"]

x_e, x_p, y_e, y_p = train_test_split(x, y, test_size=0.2, random_state=67)

modelo_rf = RandomForestRegressor(n_estimators=200, random_state=67, n_jobs=None)
modelo_rf.fit(x_e, y_e)
"""
pred_rf = modelo.predict(scalerx_p)
print(f"R²: {r2_score(scalery_p, pred_rf)}")
print(f"MAE: {mean_absolute_error(scalery_p, pred_rf)}")
