import numpy as np
import matplotlib.pyplot as pl

"""
uso basico de numpy y matplot
"""

v=np.array([1,2,3]) #vectores
print(v*2,v+1)

i=np.array([4,5,6])

print(np.dot(v,i))  #producto punto

#np.array([4,5,6],[1,2,3],[2,4,6]) #matriz 3x3



"""
ejercicio simular señal con y sin ruido
"""

t=np.linspace(0,10,1000)
signal=10*np.sin(2*np.pi*60*t)

pl.plot(t,signal)
pl.title("señal limpia")
pl.xlabel("tiempo")
pl.ylabel("voltaje")
pl.show()

SignalRuido=signal+1*np.sin(2*np.pi*1000*t)

pl.plot(t,SignalRuido)
pl.title("señal no limpia")
pl.xlabel("tiempo")
pl.ylabel("voltaje")
pl.show()