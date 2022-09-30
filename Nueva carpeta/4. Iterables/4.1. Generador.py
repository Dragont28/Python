def ciudades(): 
    for i in ["Madrid","Barcelona","Badajoz","Huelva"]:
        yield i

while True:       
    for i in ciudades():
        print(i)
        input()