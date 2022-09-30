import mod

while True:
    while True:
        while True:
            try:
                print("")
                print(mod.factorial(int(input("Factorial de -----> "))))
                break
            except:
                print("Ha habido un error, vuelvelo a intentar")
        a = input("Si quieres usar la función elevar pon /elevar/ sin barra inclinada, si no pon otra cosa ----> ")
        if a == "elevar":
            break
        else:
            pass
    while True:
        while True:
            try:
                input("\nSiguiente...")
                print("\nFuncion Elevar / Pon la base y el exponente ")
                c = int(input("Base ---> "))
                d = int(input("Exponente ---> "))
                print(mod.elevar(c,d))
                break
            except:
                print("Ha habido un error, vuelvelo a intentar")
                pass
        b = input("Si quieres usar la función factorial pon /factorial/ sin barra inclinada, si no pon otra cosa ----> ")
        if b == "factorial":
            print("")
            break
        else:
            pass
        
                
        
    

