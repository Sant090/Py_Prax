import tensorflow as tf
import numpy as np  

print(np.__version__)
print(tf.__version__)


celcius= np.array([10.0, 20.0, 30.0, 40.0], dtype=float)
farenheit= np.array([50.0, 68.0, 86.0, 104.0], dtype=float)

capa= tf.keras.layers.Dense(units=1, input_shape=[1])
"""Capas densas = posee conexiones con todas las neuronas de la capa anterior.

units = cantidad de neuronas que tendra la capa
input_shape = cantidad de entradas que tendra la capa
"""

#capa secuencial = es una pila de capas lineales, donde la salida de una capa es la entrada de la siguiente capa.
modelo = tf.keras.Sequential([capa])


modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1),
loss='mean_squared_error')

"adam= es un algoritmo de optimizacion que ajusta los pesos de la red neuronal para minimizar la funcion de perdida."
"loss= es una funcion que mide la diferencia entre la salida de la red neuronal y la salida esperada."
"mean_squared_error= es una funcion de perdida que mide la diferencia entre la salida de la red neuronal y la salida esperada, y la eleva al cuadrado."

print("Comenzando entrenamiento...")

historial = modelo.fit(celcius, farenheit, epochs=1000, verbose=False)
"""
epochs= cantidad de veces que se entrenara la red neuronal
verbose= es un parametro que indica si se mostrara el progreso del entrenamiento en la consola.
"""
print("termino el entrenamiento")

import matplotlib.pyplot as plt 
plt.xlabel('Epochs')
plt.ylabel('Loss Magnitude')
plt.plot(historial.history['loss'])
plt.show()



resultado = modelo.predict([100.0])
print("El resultado es: " + str(resultado) + " farenheit")