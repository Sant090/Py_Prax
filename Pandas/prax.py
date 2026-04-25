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



df=pd.read_csv("Datos/PronosticoYDemanda.csv")
mercados=df["MercadoComercializacionOperativo"].unique()

print("Proceso iniciado")


for i in mercados:

    dff=pd.read_csv(f"Datos/DatosProcesados/OrganizadosFecha/{i}.csv")

    final=pd.DataFrame()
    x=0
    for j in range(8760):
        df=dff.iloc[(x+0):(x+24)]
        df= df.sort_values(by="Periodo")
        final=pd.concat([final, df], ignore_index=True)
        x+=24
        df=0

    final.to_csv(f"Datos/Final/{i}.csv", index=False)
    print(F"Proceso completado para {i}")


print("Proceso completado")


"""

df=pd.read_csv("Datos/Final/MC-Antioquia.csv")


y=df["DemandaAtendida"]

print(y.describe())

t=np.arange(len(y))

plt.plot(t,y)
plt.xlabel("Tiempo")
plt.ylabel("Generación kWh")
plt.title("Generación de energía a lo largo del tiempo") 
plt.show()
