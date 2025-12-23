#with open("datos.txt","w") as elemento:
#   elemento.write("1\n26\na\nasd\n58\n5.9\n9.5")
def validacion(a):
    if not len(a)==0:
        lista=[]
        with open(f"{a}","r") as y:
            archivo=y.readlines()
        for x in archivo:
            try:     
                lista.append(float(x))
            except ValueError:
                None
        print(lista)
        return lista
    else:
        return None
    
def analisis(a):
    if not len(a)==0:
        prom=0
        min=0
        max=0
        orden=validacion(a)
        for x in orden:
            prom+=x
        prom/=len(orden)
        orden.sort()
        min=orden[0]
        max=orden[-1]
        resultado=dict(promedio=prom,minimo=min,maximo=max)
        return resultado
    else: 
        None
        
def guardar(a,nombre):
    with open(f"{nombre}{".txt"}","w") as x:
        x.write(f"Promedio: {a["promedio"]}\nMaximo: {a["maximo"]}\n Minimo: {a["minimo"]}")
       
       
listas=analisis("datos.txt") 
guardar(listas,"resultados")