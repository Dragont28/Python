class moto():
    
    def __init__(self):      # Constructor inicial / Para crear propiedades iniciales
        self.largo = 500
        self.ancho = 80
        self.alto = 180
        self.ruedas= 2                    # Propiedad encapsulada / No puedes modificar el número de ruedas desde fuera de la clase
        self.en_marcha = False
        self.__faros_encendidos = False
        self.gasolina = 0.5
        self.presion = 0.6
        
    
    def arrancar(self):               # Puedes crear un parametro para los method: def arrancar(self,parametro):
        if self.__check == True:
            self.en_marcha = True
        elif (((self.__check())[1]) == False) and (((self.__check())[2]) == False):
            print("No se ha podido arrancar el coche porque hay poca gasolina y la presion de las llantas esta mal")
        elif (self.__check())[1] == False:
            print("No se ha podido arrancar porque la presión de las llantas esta mal")
        elif (self.__check())[2] == False:
            print("No se ha podido arrancar porque hay muy poca gasolina")
    
    def encender(self):
        if(self.en_marcha):
            self.__faros_encendidos = True
        
    def estado(self):
        print("El coche esta arrancado: ",self.en_marcha)
        print("Las luces estan encendidas: ",self.__faros_encendidos)
        
    def __check(self):
        
        gasolina_ok = False
        presion_ok = False
        
        if self.gasolina > 2:
            gasolina_ok = True
        if 2.2 < self.presion < 3:
            presion_ok = True
        if(gasolina_ok and presion_ok):
            return True
        else:
            return (False,gasolina_ok,presion_ok)
                    
mimoto = moto()

mimoto.arrancar()
mimoto.encender()
mimoto.estado()

input()