from tabulate import tabulate
# -*- coding: utf-8 -*-
#crear datos en un archivo csv
#abrir el archivo 
#modos de apertura w,r,a,b 
file = open ('datos.csv','w')#abrir el archivo. Si el archivo no existe "w" lo crea  
#file.write ("Hola,este es mi primer archivo")#escribir datos 
equipo = "Impresora 3d; general electric ;2;30;2022-08-20" #tener cuidaddo como separo los datos el punto y coma ; separa los datos por columnas en el excel resultante 
file.write(equipo+"\n") 
#file.write (equipo+ "\n") para que los muestre con salto de linea 
equipo2= "Sensor cardiaco;xxxx;10;15;2022-07-30" 
file.write(equipo2 +"\n" )

file.close()#cerrar el archivo

#pasos almacenamiento: 1. abrir el archivo 2. crear datos 3.  cerrar 

file = open ('datos.csv','a')
equipo = "multimetro; general electric; 10;20;2022-08-20"
file.write(equipo + "\n")
file.close()

#lectura de archivos 
archivo = open ('datos.csv','r')
lineas = archivo.readlines()
#sale en renglones
#for l in lineas:
    #print (l)
    
encabezado = ["Nombre","Proveedor","Cantidad","Ciclo","Fum"]


datos = []

for l in lineas:
    l = l.replace("\n","")#reemplazar "x" por "y"
    l = l.split (";")#consultar la función split 
    datos.append (l)
    
    
print (tabulate(datos,encabezado,tablefmt = "grid"))
