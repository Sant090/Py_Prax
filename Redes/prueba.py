import numpy as np
import pandas as pd

# 1. Semilla para asegurar resultados reproducibles
np.random.seed(42)
n_samples = 200000

# 2. Generar valores con distribución uniforme en escala logarítmica
# (Esto asegura buena densidad de datos tanto para valores pequeños como grandes)
r = np.exp(np.random.uniform(np.log(0.5), np.log(2000), n_samples))
v = np.exp(np.random.uniform(np.log(1.5), np.log(500), n_samples))

# 3. Calcular potencia exacta p = v^2 / r
p = (v**2) / r

# 4. Crear DataFrame y redondear a 2 decimales
df_grande = pd.DataFrame(
    {"r": np.round(r, 2), "v": np.round(v, 2), "p": np.round(p, 2)}
)

# 5. Guardar en el CSV (reemplaza o crea el archivo)
df_grande.to_csv("Redes/p2.csv", index=False)
print(f"✅ Dataset guardado exitosamente con {len(df_grande)} filas en 'Redes/p2.csv'")

