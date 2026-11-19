def f(x):
    return x**2 + 3*x**3 - 2

def error(xa,xb):
    return abs(xa - xb) / abs(xa)


def biseccion(a, b, tolerancia, ite):


    if f(a) * f(b) >= 0:
        return None

    for i in range(1, ite + 1):

        c = (a + b) / 2
        fc = f(c)

        print(f"Iteración {i}")
        print(f"a = {a}")
        print(f"b = {b}")
        print(f"c = {c}")
        print(f"f(c) = {fc}")
        print(f"Error = {error(c, a)}")
        print("-" * 40)

        if fc == 0:
            return c
        if abs(b - a) / 2 < tolerancia:
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return c

a = 0
b = 5
tolerancia = 0.001
iteraciones = 100

raiz = biseccion(a, b, tolerancia, iteraciones)

print("Raíz aproximada:", raiz)