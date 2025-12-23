with open("datos.txt","w") as elemento:
    elemento.write("1\n25\nasd\nd\n5.9\n5.2\n9.1")


with open("datos.txt","r") as y:
    archivo=y.readlines()
for x in archivo:
    print(x)
    