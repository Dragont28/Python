from mod import factorial # Puedo poner en vez de factorial un from mod import * para importar todo el codigo

while True:
    try:
        print(factorial(int(input("Factorial de ----> "))))
        print("")
    except:
        print("")
        print("Ha habido un error intentalo de nuevo")
        print("")