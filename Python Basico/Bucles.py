#ejemplo basico con bucles

print("Bievenido a la lista de estudiantes")
estudiantes=[]

num_estudiantes=input("cuantos estudiantes deseas agregar: ")
for i in range(int(num_estudiantes)):
    estudiantes.append(input(f"Nombre del estudiante numero {i+1}: "))
print("La lista de todos lo estudiantes es:")
contador=0
for j in estudiantes:
    contador+=1
    print(f"{contador}. Estudiante: {j}")
    
    
    """add"""

