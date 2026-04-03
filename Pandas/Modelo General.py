import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  

"""extrae los datos por cada uno de los mercados y los separa de forma individual en archivos csv"""


df=pd.read_csv("Datos/PronosticoYDemanda.csv")
mercados=df["MercadoComercializacionOperativo"].unique()

for i in mercados:
    dff=df[df["MercadoComercializacionOperativo"] == i]
    dff.to_csv(f"Datos/DatosProcesados/{i}.csv", index=False)







"""organiza los datos de cada uno de los mercados por fecha """

df=pd.read_csv("Datos/PronosticoYDemanda.csv")
mercados=df["MercadoComercializacionOperativo"].unique()

for i in mercados:
    dff=pd.read_csv(f"Datos/DatosProcesados/{i}.csv")
    dff["Fecha"] = pd.to_datetime(dff["Fecha"])
    dff = dff.sort_values(by='Fecha') 

    dff.to_csv(f"Datos/DatosProcesados/OrganizadosFecha/{i}.csv", index=False)







"""organiza los datos de cada uno de los mercados por fecha y periodo, para que se pueda graficar la demanda a lo largo del tiempo"""

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

