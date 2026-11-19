import pandas as pd
from pathlib import Path


df = pd.read_csv(Path("datasets/GeneracionPractica.csv"))


#se interpola los valores nulos de la columna GeneracionReal y se guarda en la columna generacionInterpolada
#df["GeneracionInterpolada"] = df["GeneracionReal"].interpolate(method="linear")
#df["GeneracionInterpolada"] = df["GeneracionReal"].interpolate(method="polynomial", order=2)




#eliminar las filas
#df = df.dropna()



#rellenar con la media o la mediana

#media=df["GeneracionReal"].mean()
#print(media )
#print(df.fillna(media))

#mediana=df["GeneracionReal"].median()
#print(mediana)
#print(df.fillna(mediana))

