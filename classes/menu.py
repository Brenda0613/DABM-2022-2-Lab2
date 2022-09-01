class Menu:
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio
        
    def ver (self):
        print ("Bienvenido al sistema".center(50,"*"))
        print ("Laboratorio:"+self.laboratorio)
        print ("1. Tecnicos")
        print ("2. Estudiantes")
        print ("3. Salir")
        op = input (">>>")
        return op 
    
class MenuTecnicos:
    def ver (self):
        print ("Menú técnicos de laboratorio".center(20,"*"))
        print ("Laboratorio:"+self.laboratorio)
        print ("1. Registrar equipos")
        print ("2. Registrar prestamo")
        op = input (">>>")
          
if __name__ == '_main_' :
    m = Menu("xxx")
    m.ver()
        

