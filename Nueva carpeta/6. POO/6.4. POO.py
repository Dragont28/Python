class coche():
    def __init__(self):
        self.ruedas = 4
        
    def desplazamiento(self):
        print("Tengo ",self.ruedas," ruedas")
        
class moto():
    def __init__(self):
        self.ruedas = 2
        
    def desplazamiento(self):
        print("Tengo ",self.ruedas," ruedas")
        
class camion():
    def __init__(self):
        self.ruedas = 6
        
    def desplazamiento(self):
        print("Tengo ",self.ruedas," ruedas")
        
def polimorfismo(argument):
    if(isinstance(argument,moto)):
        print("Soy una moto")
        argument.desplazamiento()
        input()
        argument = coche()
        print("Ahora soy un coche")
        argument.desplazamiento()
        input()
        argument = camion()
        print("Ahora soy un camion")
        argument.desplazamiento()
        input()
    elif(isinstance(argument,camion)):
        print("Soy un camion")
        argument.desplazamiento()
        input()
        argument = moto()
        print("Ahora soy una moto")
        argument.desplazamiento()
        input()
        argument = coche()
        print("Ahora soy un coche")
        argument.desplazamiento()
        input()
    elif(isinstance(argument,coche)):
        print("Soy un coche")
        argument.desplazamiento()
        input()
        argument = moto()
        print("Ahora soy una moto")
        argument.desplazamiento()
        input()
        argument = camion()
        print("Ahora soy un camion")
        argument.desplazamiento
        input()
        
micoche = camion()
polimorfismo(micoche)

