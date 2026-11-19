import pandas as pd

df=pd.read_csv("datasets/GeneracionEspinal.csv")

df = df.drop_duplicates(subset=["FechaHora"], keep="first").reset_index(drop=True)

df = df.sort_values(by='FechaHora', ascending=True)


#para guardar el df
df.to_csv("datasets/GeneracionEspinalOrdenado.csv", index=False)
