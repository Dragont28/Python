from io import open

archivo = open("ae.txt","r+")  #r+ para lectura y escritura
archivo.write("Arroz\nPaella\nKiwi\nPera")
archivo.seek(7)  # Pone el cursor del ratón 7 posiciones adelante desde el 0
print(archivo.read(11)) # Lee 11 carácteres 