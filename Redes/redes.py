import torch as th
import torch.nn as nn    

x= th.tensor([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]])

"""x= es un tensor de 6 filas y 1 columna, que contiene los valores del 1 al 6. Este tensor se utilizará 
como entrada para un modelo de red neuronal lineal, que se definirá a continuación. El modelo tomará este tensor como entrada y 
generará predicciones basadas en los pesos y sesgos aprendidos durante el entrenamiento."""

y= th.tensor([[10.0], [20.0], [30.0], [40.0], [50.0], [60.0]])

"""y= es un tensor de 6 filas y 1 columna, que contiene los valores del 10 al 60. Este tensor se utilizará 
como salida esperada para el modelo de red neuronal lineal, que se definirá a continuación. El modelo tomará este tensor 
como referencia para ajustar sus pesos y sesgos durante el entrenamiento, con el objetivo de minimizar la diferencia entre las 
predicciones generadas por el modelo y los valores reales de y."""

modelo = nn.Linear(1, 1)
"""modelo= es un objeto de la clase nn.Linear, que representa un modelo de red neuronal lineal con una sola capa
y un solo nodo de salida. Este modelo tomará un tensor de entrada de 1 dimensión y generará un tensor de salida de 1 dimensión, aplicando una función lineal definida por los pesos y sesgos del modelo."""

predicciones = modelo(x)
print(predicciones)
"""imprime las predicciones generadas por el modelo de red neuronal lineal para los valores de entrada x. 
Estas predicciones son el resultado de aplicar la función lineal definida por los pesos y sesgos del modelo a los valores de x. 
Dado que el modelo aún no ha sido entrenado, las predicciones iniciales pueden no ser precisas y pueden diferir significativamente 
de los valores reales de y."""


# no da nada coherente 


"""funcion de perdida = nn.MSELoss()"""
loss_fn = nn.MSELoss()
loss = loss_fn(predicciones,y)
print(loss)

"""imprime el valor de la función de pérdida calculada entre las predicciones generadas por el modelo y los 
valores reales de y. La función de pérdida utilizada es la pérdida cuadrática media (MSE), que mide la diferencia promedio 
al cuadrado entre las predicciones y los valores reales. Un valor de pérdida más bajo indica que el modelo está haciendo 
predicciones más precisas, mientras que un valor de pérdida más alto indica que hay una mayor discrepancia entre las predicciones 
y los valores reales."""



"""optimizador hace que el modelo aprenda de los errores y mejore sus predicciones"""
optimizer = th.optim.Adam(modelo.parameters(), lr=0.005)
#lr=0.01 es la tasa de aprendizaje, que determina qué tan rápido o lento el modelo ajusta sus pesos y sesgos durante el entrenamiento.

"""entrenamiento del modelo 1000 veces, ajustando los pesos y sesgos del modelo para minimizar la función de pérdida 
entre las predicciones y los valores reales de y."""
for i in range(1000):

    predicciones = modelo(x)

    loss = loss_fn(predicciones,y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()



print(modelo.weight)
print(modelo.bias)


predicciones = modelo(x)
print(predicciones)
print(loss)


"""capas"""
# ya no se usa nn.Linear(1,1)
"""se usa modelo = nn.Sequential(

    nn.Linear(4,16),

    nn.ReLU(),

    nn.Linear(16,8),

    nn.ReLU(),

    nn.Linear(8,1)

)
"""