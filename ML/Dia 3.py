import pandas as pd 

"""
revision basica de pandas
"""
#crear datos
datos1=[[20,10,20],[20,10,20],[20,10,20]]   #matriz
dff=pd.DataFrame(datos1)                    #conformacion de matriz
dff.to_csv("datos1.cvs",index=False)        #guardado



df=pd.read_csv('datos1.cvs')

print(df.head())

print(df.describe())

print(df.dropna())