import hashlib, subprocess
from sys import exit
from time import sleep


def cls():
    
    subprocess.run("cls",shell=True)
    
def error(txt):
    
    cls()
    print(f"{txt}")
    sleep(2.5)
    cls()
    
def comprobacion_leng():
    arg_hexdigest = True
    x = False
    if (leng % 2) != 0:
        error("\nEl número tiene que ser par")
    else:
        x = True
        
def salir():
    exit()
    
    

while True:
    
    cls()
    arg_hexdigest = False
    c = True
    x = False
    data = input("Pon la información a la que sacar el hash: ")
    
    while True:
        
        try:
            
            txt_fhash = ("Selecciona el número de la función hash:\n1 - sha1\n2 - sha224\n3 - sha256\n4 - sha384\n5 - sha512\n6 - blake2b\n7 - blake2s\n8 - md5\n9 - sha3_224\n10 - sha3_256\n11 - sha3_384\n12 - sha3_512\n13 - shake_128\n14 - shake_256\n15 - Cambiar los datos\n16 - Salir\n")
            in_fhash = input(f"{txt_fhash}")
            in_fhash = int(in_fhash)
            
            if in_fhash == 1:
                fhash = "sha1"
            elif in_fhash == 2:
                fhash = "sha224"
            elif in_fhash == 3:
                fhash = "sha256"
            elif in_fhash == 4:
                fhash = "sha384"
            elif in_fhash == 5:
                fhash = "sha512"
            elif in_fhash == 6:
                fhash = "blake2b"
            elif in_fhash == 7:
                fhash = "blake2s"
            elif in_fhash == 8:
                fhash = "md5"
            elif in_fhash == 9:
                fhash = "sha3_224"
            elif in_fhash == 10:
                fhash = "sha3_256"
            elif in_fhash == 11:
                fhash = "sha3_384"
            elif in_fhash == 12:
                fhash = "sha3_512"
            elif in_fhash == 13:
                fhash = "shake128"
                while True:
                    leng = int(input("\n¿Cuántos carácteres quiere que tenga? "))
                    comprobacion_leng()
                    if x == True:
                        break
            elif in_fhash == 14:
                fhash = "shake256"
                while True:
                    leng = int(input("¿Cuántos carácteres quieres que tenga? "))
                    comprobacion_leng()
                    if x == True:
                        break
            elif in_fhash == 15:
                c = False
                cls()
                break
            elif in_fhash == 16:
                salir()
            elif in_fhash < 1 or in_fhash > 17:
                error("Esa opción no está contemplada")
            break
                           
        except ZeroDivisionError:
            
            error("Esa opción no está contemplada")
            
    if c == True:
        if arg_hexdigest == False:
            print("")
            print(hashlib.new(f"{fhash}",bytes(f"{data}","utf-8")).hexdigest())
        if arg_hexdigest == True:
            print("")
            print(hashlib.new(f"{fhash}",bytes(f"{data}","utf-8")).hexdigest(leng))
        input("\nPresiona cualquier tecla para continuar")
    
    while True:
        try:
            fin = int(input("\nSelecciona una opción\n1 - Volver a empezar\n2 - Salir\n"))
            if fin == 1:
                break
            if fin == 2:
                salir()
            if fin < 1 or fin > 2:
                error("Esa opción no está contemplada")
        except ValueError:
            error("Esa opción no está contemplada")