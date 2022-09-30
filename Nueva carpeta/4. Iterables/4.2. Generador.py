def ciudades(): 
    for i in ["Madrid","Barcelona","Badajoz","Huelva"]:
        yield from i # Al tener el from coge subelementos del elemento / en este caso los subelementos de "Madrid" son sun carácteres

while True:       
    for i in ciudades():
        print(i)
        input()