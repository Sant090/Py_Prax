#repaso en proyecto de elementos basicos de py
def palabras(palabra):
    if palabra.find(" ") == -1:
        print(f"La palabra '{palabra}' tiene {len(palabra)} letras")
    else:
        print("La palabra posee un espacio, quite el espacio")
        return

def verificacion_edad(age):
    if age>=18:
        return True
    elif age<18:
        print("No eres apto para este programa")
        return False
    else:
        print("ingreso un valor no numerico")
        return False
    

def main():
        
        edad=input("ingrese su edad: \n")
        if verificacion_edad(int(edad)) != False: 
            nombre=input("ingrese su nombre: \n")
            palabra=input("Ingrese la palabra a evaluar: \n")  
            palabras(palabra)
        else:    
            return 
            

main()
