def validar_posicion():
    while True:
        seleccion=input("a: ")
        if len(seleccion)==1:
            if ord(seleccion) > ord('0') and ord(seleccion) < ord('9'):
                break
            else:
                print("ingrese un numero")
        else:
            print("ingrese solo un numero del 1 al 9")
    return int(seleccion)
print (validar_posicion())