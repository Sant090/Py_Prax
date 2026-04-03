import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  

"""extrae los datos por cada uno de los mercados y los separa de forma individual en archivos csv"""


df=pd.read_csv("Datos/PronosticoYDemanda.csv")
mercados=df["MercadoComercializacionOperativo"].unique()

for i in mercados:
    dff=df[df["MercadoComercializacionOperativo"] == i]
    dff.to_csv(f"Datos/DatosProcesados/{i}.csv", index=False)