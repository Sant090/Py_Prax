import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  


"""organiza los datos de cada uno de los mercados por fecha """

df=pd.read_csv("Datos/PronosticoYDemanda.csv")
mercados=df["MercadoComercializacionOperativo"].unique()

for i in mercados:
    dff=pd.read_csv(f"Datos/DatosProcesados/{i}.csv")
    dff["Fecha"] = pd.to_datetime(dff["Fecha"])
    dff = dff.sort_values(by='Fecha') 

    dff.to_csv(f"Datos/DatosProcesados/OrganizadosFecha/{i}.csv", index=False)



