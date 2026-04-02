import pandas as pd

df= pd.read_excel("Datos/Demanda_Energia_SIN_2025.xlsx")

print(df.head())   

df.to_csv("Datos/Practica.csv", index=False)