from io import open

archivo = open("ae.txt","w") # Write/ sobreescribe
archivo.write("Prueba\nP2")
archivo.close

archivo = open("ae.txt","r") # Read/ lectura
lineas = archivo.readlines()
archivo.close()

archivo = open("ae.txt","a") # Append/ agrega
archivo.write("\nP3")
archivo.close

archivo = open("ae.txt","r")
lineas_2 = archivo.readlines() # Readline sin s lee una linea
print(lineas)
print(lineas_2)
archivo.close()