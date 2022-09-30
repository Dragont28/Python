def factorial(x):
    for i in range(int(x)):
        if i == 0:
            a = 1
        if i > 0:
            a = a * (i + 1)
    if int(x) < 0:
        a = "No hay función en factoriales negativos "
    return a   