def edad(a):
    if a < 0:
        raise ValueError ("La edad no puede ser negativa")  # Crear un error y meterlo en otro error, puedes ponerle un msg
    elif a < 10:
        return("Eres muy joven")
    elif a < 20:
        return("Eres joven")
    elif a < 30:
        return("Eres un adulto")
    elif a < 40:
        return("Eres maduro")
    elif a < 50:
        return("Eres muy maduro")
    elif a < 140:
        return("Eres anciano")
    elif a >= 140:
        raise ValueError ("No puedes estar vivo")

while True:
    try:
        print(edad(int(input("Pon aqui tu edad -----> "))))
        print("El programa ha finalizado \n" + 100*("-"))
    except:
        print("Ha habido un error, el programa ha finalizado\n" + 100*("-"))