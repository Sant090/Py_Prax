import torch as th
import numpy as np

""
arreglo1 = np.array([[1, 2, 3], [4, 5, 6]])

tensor1 = th.tensor(arreglo1)

print(tensor1)

print(tensor1.device)
print(tensor1.shape)
""