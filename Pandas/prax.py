import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  

"""
df= pd.read_excel("Datos/Demanda_Energia_SIN_2025.xlsx")

print(df.head())   

df.to_csv("Datos/Practica.csv", index=False)


df = pd.read_excel("Datos/Demanda_Energia_SIN_2025.xlsx", header=3)
print(df.head())

print(df["Generación kWh"].describe())

y=df["Generación kWh"]

t=np.arange(len(y))

plt.plot(t,y)
plt.xlabel("Tiempo")
plt.ylabel("Generación kWh")
plt.title("Generación de energía a lo largo del tiempo") 
plt.show()

"""
dff=pd.read_csv("Datos/PronosticoYDemanda.csv")

print(dff.head())
mercados=dff["MercadoComercializacionOperativo"].unique()


for i in mercados:
    df=dff[dff["MercadoComercializacionOperativo"] == i]
    df.to_csv(f"Datos/finalizados/{i}.csv", index=False)

