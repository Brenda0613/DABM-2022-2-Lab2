# -*- coding: utf-8 -*-
class Prestamo: 
    file = "database/prestamos.csv"#variable de clase 
    def __init__ (self,nombre, carnet, equipo, fechap, fechae):
        self.nombre = nombre
        self.carnet = carnet
        self.equipo = equipo
        self.fechap = fechap 
        self.fechae = fechae
    
    def save (self):
        f = open (self.file, 'a')
        linea = ";".join([self.nombre, self.carnet,self.equipo,self.fechap, self.fechae])
        f.write(linea +"\n")
        f.close ()
        
def crearPrestamo ():
    print ("Registrar préstamo")
    nombre = input ("Nombre:")
    carnet = input ("Carnet:")
    equipo = input ("Equipo que solicita: ")
    fechap = input ("Fecha de prestamo (yyyy-mm-dd):")
    fechae = input ("Fecha de entrega (yyyy-mm-dd):")
    p = Prestamo (nombre, carnet, equipo, fechap, fechae)
    return p 

def verPrestamos (carnet,equipo):
    for p in Prestamo:
        if carnet in p:
            print ("Usted realizó un préstamo del siguiente equipo",equipo)
    


    


