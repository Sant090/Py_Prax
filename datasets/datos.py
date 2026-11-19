import json
import urllib.request
import pandas as pd

url = (
    "https://archive-api.open-meteo.com/v1/archive?"
    "latitude=4.149&longitude=-74.884&"
    "start_date=2026-01-01&end_date=2026-11-10&"
    "hourly=temperature_2m,relative_humidity_2m,shortwave_radiation&"
    "timezone=America%2FBogota"
)

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

df_clima = pd.DataFrame({
    "FechaHora": pd.to_datetime(data["hourly"]["time"]),
    "Temperatura_C": data["hourly"]["temperature_2m"],
    "Humedad_Relativa_%": data["hourly"]["relative_humidity_2m"],
    "Irradiancia_Wm2": data["hourly"]["shortwave_radiation"],
})

# Separar Fecha y Hora para cruzar con GeneracionEspinalOrdenado.csv
df_clima["Fecha"] = df_clima["FechaHora"].dt.date
df_clima["Hora"] = df_clima["FechaHora"].dt.time
df_clima = df_clima[["Fecha", "Hora", "Temperatura_C", "Humedad_Relativa_%", "Irradiancia_Wm2"]]

df_clima.to_csv("datasets/ClimaEspinal.csv", index=False)
print(df_clima.iloc[10:16])  # Muestra horas del mediodía para verificar irradiancia > 0
print(f"Total registros: {len(df_clima)} | Nulos:\n{df_clima.isna().sum()}")