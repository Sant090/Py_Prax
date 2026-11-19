import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


df = pd.read_csv("datasets/Fallas.csv")

x=df[["horas de estudio"]]
y=df["aprobado"]

x_e, x_p, y_e, y_p = train_test_split(x, y, test_size=0.3, random_state=42)



"""Regresion Logistica
modelo = LogisticRegression()
modelo.fit(x_e, y_e)

predicciones = modelo.predict(x_p)
print("Exactitud del modelo:", accuracy_score(y_p, predicciones))

print("\nMatriz de Confusión:\n", confusion_matrix(y_p, predicciones))
print("\nReporte de Clasificación:\n", classification_report(y_p, predicciones))

"""



modelo=RandomForestClassifier(n_estimators=100, random_state=42)

modelo.fit(x_e, y_e)

predicciones = modelo.predict(x_p)
print("Exactitud del modelo:", accuracy_score(y_p, predicciones))

print("\nMatriz de Confusión:\n", confusion_matrix(y_p, predicciones))
print("\nReporte de Clasificación:\n", classification_report(y_p, predicciones))


print("Prediccion para 0 horas de estudio:", modelo.predict([[2.2]]))