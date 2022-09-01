from classes.menu import Menu, MenuTecnicos 

if __name__== '_main_':
    menu = Menu("Escuela de ingeniería")
    op = menu.ver ()
    if op =="1":
        menu2= MenuTecnicos ('Escuela de Ingeniería')
        op2 = menu2.ver()
        if op2 == "1":
            

