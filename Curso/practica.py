import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


df = pd.read_csv("datasets/gta_sa_vehicle_stats.csv")

#tomamos los datos que nos interesan 
masas=df["mass_(kg)"]
aceleraciones=df["acceleration(ms^2)"]



#hacemos otro df para tener solo los datos que nos interesan
df2=pd.DataFrame({"Nombre del Vehiculo":df["identifier"],"masa":masas,"aceleracion":aceleraciones})


print(df2)

x=df2[["masa"]]
y=df2[["aceleracion"]]

#separamos los datos en entrenamiento y prueba
Xe, Xa, ye, ya = train_test_split(
    x, y, test_size=0.2, random_state=67
)


#los escalamos
scaler1 = MinMaxScaler()
scaler2 = MinMaxScaler()

df2["masa"] = scaler1.fit_transform(df2[["masa"]])
df2["aceleracion"] = scaler2.fit_transform(df2[["aceleracion"]])

poly=PolynomialFeatures(degree=2)
X_poly=poly.fit_transform(x)


modelo=LinearRegression()
modelo.fit(X_poly,y)

y_pred = modelo.predict(X_poly)
print("Coeficientes encontrados:", modelo.coef_)
print("Intercepto:", modelo.intercept_)
print("Precisión del modelo (R^2):", r2_score(y, y_pred))

