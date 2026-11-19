import pandas as pd
from pathlib import Path

df = pd.read_csv(Path("datasets/gta_sa_vehicle_stats.csv"))


#mirar tamaño columnas tipos
#df.info()

#cantidad de columnas
#print(df.columns.size)

#cantidad de valores nulos por columna
#print(df.isna().sum())

#cantidad de filas repetidas
#print(df.duplicated().sum())

#cantidad promedio max min cuatiles 
#print(df.describe())

#valores unicos por columna
#print(df['mass_(kg)'].value_counts())