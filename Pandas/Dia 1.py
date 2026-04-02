import pandas as pd 



#observar datos
df= pd.read_csv("Pandas/muestra.csv")
"""
print(df.head())    #5 primeras filas

print(df.info())    #tipo de datos 

print(df.describe()) #estadísticas descriptivas

"""

#seleccionar y manipular datos
"""
print(df["fecha"])  #seleccionar columna
print(df[["fecha","id_transaccion"]]) #seleccionar varias columnas
print(df[df["fecha"]>"2026-01-20"]) #filtrar filas por fecha
"""
#Limpieza de datos

print(df)

print(df.isnull().sum()) #verificar valores nulos

df = df.dropna() #eliminar filas con valores nulos  

df = df.drop_duplicates() #eliminar filas duplicadas

#df["nombre_cliente"] = df["nombre_cliente"].str.lower().str.strip() #eliminar espacios en blanco    

