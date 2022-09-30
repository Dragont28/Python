class vehiculos():
    
    def __init__(self,marca):
        self.marca = marca
        self.encendido = False
        self.acelerando = False
        self.frenando = False
        
    def encender(self):
        self.encendido = True
        
    def acelerar(self):
        
        if self.encendido == True:
            self.frenando = False
            self.acelerando = True
        else:
            print("El coche no esta encendido")
        
    def frenar(self,):
        
        if self.encendido == True:
            self.acelerando = False
            self.frenando = True
        else:
            print("El coche no esta encendido")
        
    def estado(self):
        print("Encendido -----> ",self.encendido)
        print("Marca ------> ",self.marca)
        print("Acelerando -----> ",self.acelerando)
        print("Frenando -------> ",self.frenando)
        
class coche(vehiculos):
    
    def __init__(self, descapotao, marca_coche):
        
        super().__init__(marca_coche)      # El super con esa sintax dentro del init de la primera generacion de herencia 
        self.ruedas = 4
        self.descapotao = descapotao
          
    
    def estado(self):
        super().estado()      # Ese super se pone para poder usar funciones de la primera generación de herencia
        print("Ruedas -----> ",self.ruedas,"\nEs un descapotable -------> ",self.descapotao)
    
        
elcoche = coche(True,"BMW")

while True:
    elcoche.encender()
    elcoche.acelerar()
    elcoche.estado()
    print("El objeto elcoche pertenece a la clase vehiculo ------> ",isinstance(elcoche, vehiculos))
    input("")


