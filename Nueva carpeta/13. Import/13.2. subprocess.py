import subprocess

while True:
    
    b = input("Pon aqui la web para probar la conexion -----> ")
    a =  (f"ping {b} -4 -n 3")
    print(a)
    subprocess.run(a, shell=True)
    
    while True:
        
        c = input("\nPara continuar 1\nPara limpiar consola 2\n\n")
        c = int(c)
        
        if c == 1:
            print("")
            break
        if c == 2:
            subprocess.run("cls", shell=True)
            break
        else:
            print("\nSu respuesta no esta contemplada\n")
        
    

    
    
    