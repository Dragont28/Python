e0 = False
e = False
f = False
a = -1
d = input("Pon tu correo aqui ")
for i in d:
    if (i == "@"):
        e0 = True
    elif (i == ".") and (e0 == True ) :
        e = True
    if e == True:
        a = a + 1
        if a == 2:
            f = True
        if a > 3:
            f = False
if f == True:
    print("Correo bien escrito")
else:
    print("Correo mal escrito")
input()