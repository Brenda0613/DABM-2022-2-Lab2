# -*- coding: utf-8 -*-
from tabulate import tabulate 
class Equipo:
    #variable de clase:algo interno a la aplicacion, utiles para ciertos parametros,datos que no le interesan al usuario pero necesarias para el funcionamiento "file= 'database/equipos.csv'
    
    def __int__(self,nombre,proveedor,cantidad,referencia,ciclo,fum=""):#fecha ultimo mantenimiento: esta predispuesta a vacío (fum= "")por ello, si no se agrega no arroja error 
        self.nombre = nombre
        self.proveedor = proveedor 
        self.cantidad = cantidad 
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum
        
    def verDatos (self):
        header = ["Nombre","Referencia","Cantidad","Proveedor","Ciclo","Fum"]
        datos = [[self.nombre,self.referencia,self.cantidad,self.proveedor,self.ciclo,self.fum]]
        print (tabulate(datos,header,tablefmt="grid"))
    
    def save(self):
        f = open(self.file, 'a')
        linea = ";".join([self.nombre,self.proveedor, self.referencia, self.cantidad, self.ciclo, self.fum])
        f.write(linea +"\n")
        f.close()
        
    
        
def crearEquipo ():
    print ("Registrar nuevo equipo")
    nombre = input ("Nombre:")
    proveedor =input ("Proveedor:")
    referencia = input ("Referencia:")
    ciclo = input ("Ciclo de mantenimiento (días):")
    cantidad = input ("Cantidad:")
    fum = input ("Fecha de último mantenimiento")
    e = Equipo(nombre,proveedor,cantidad,referencia,ciclo,fum)
    
    return e 

def consultarEquipo ():
    print ("Consulta de equipos")
    nombre = input ("Nombre de equipo:")

#creacion, lectura, prestamo y eliminación de los equipos
    
def mantenimiento (e):
    litaEquipos = getAllEquipos ()
    #print (listaEquipos)
    eq = input ("¿Qué equipo desea consultar?")
    fum = input ("Fecha de último mantenimiento:")
    pos = 0
    for e in listaEquipos:
        #print (e)
        if eq in e: 
            datosEquipo= e.split (";")
            #print (datosEquipo)
            datosEquipo [5] = fum + "\n"
            listaEquipos [pos] = ";".join(datosEquipo)
        pos = pos + 1
    saveAllEquipos (listaEquipos)
                
    
def saveAllEquipos (equipos):
    a = open("database/equipos.csv","w")
    for e in equipos:
        a.write(e)
        a.close()
        
def getAllEquipos():
    a = open ("database/equipos.csv","r")
    datos = a.readlines()
    return datos 

def registroEntrega ():
    pass 
