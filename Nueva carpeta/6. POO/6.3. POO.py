class persona():
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def datos(self):
        print("Nombre -----> ",self.nombre)
        
class empleado(persona):
    
    def __init__(self, nombre_persona, salario):
        super().__init__(nombre_persona)
        self.salario = salario
        
class pro(persona):
    
    def __init__(self, nombre_persona, rango):
        super().__init__(nombre_persona)
        self.rango = rango
        
class jugador_pro(pro,empleado):
    
    def __init__(self, nombre, rango, salario):
        self.nombre = nombre
        self.rango = rango
        self.salario = salario
        
    def datos(self):
        super().datos()
        print("Salario -----> ", self.salario,"\nRango ------> ",self.rango)
        
yo = jugador_pro("Ismael",6000,"Radiant")
yo.datos()

        
