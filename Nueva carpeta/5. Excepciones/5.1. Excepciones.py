def division(a,b):
    return a/b
        
while True:

    while True:
        try:
            n1 = int(input(" Dividendo "))
            n2 = int(input(" Divisor "))
            break
        except ValueError:
            print(" Eso no es un número ")
            print(" Programa finalizado \n")

    try:
        print(" " + str(division(n1,n2)))
    except ZeroDivisionError: # Si uso el except si el error engloba todos los posibles errores y finally 
        print(" No se puede dividir entre 0")  # si quiero que pase lo que pase se ejecute cierta orden
    print(" Programa finalizado \n")
