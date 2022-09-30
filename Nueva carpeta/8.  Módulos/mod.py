def factorial(x):
    x = int(x)
    for i in range((x)):
        if i == 0:
            a = 1
        if i > 0:
            a = a * (i + 1)
    if x < 0:
        a = "No hay función en factoriales negativos "
    return a   
def elevar(x,y):
    return x**y