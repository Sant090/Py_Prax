import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Cargar el modelo guardado previamente (no se vuelve a entrenar)
model = tf.keras.models.load_model("modelo.keras")

# Datos de prueba de ejemplo
# Ajusta las dimensiones según lo que reciba tu red
x_prueba = np.array([[100]], dtype=np.float32)

# Probar la red
predicciones = model.predict(x_prueba)
print("Resultado de la predicción:", predicciones)

