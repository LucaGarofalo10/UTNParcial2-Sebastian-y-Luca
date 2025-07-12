import os
from outputs import *

def ta_te_ti():
    tablero = [["1","2","3"],["4","5","6"],["7","8","9"]]
    turno=0
    precentacion_ta_te_ti(tablero)
    tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
    while True:
        turno+=1
        
        turno_jugador(tablero)
        resultado,marca=verificar_victoria(tablero)
        if resultado:
            resultado_ta_te_ti(tablero,marca)
            ganador=True
            break
        
        if turno>=5:
            resultado_ta_te_ti(tablero,"")
            ganador=None
            break
        
        turno_maquina(tablero)
        resultado,marca=verificar_victoria(tablero)
        if resultado:
            resultado_ta_te_ti(tablero,marca)
            ganador=False
            break
        
    return ganador

def turno_jugador(tablero):
    mensaje=""
    while mensaje!="ok":
        os.system('cls')
        mostrar_ta_te_ti(tablero)
        seleccion=obtener_posicion()
        
        fila,columna=calcular_fila_columna(seleccion)
        
        mensaje=validar_ta_te_ti(seleccion,fila,columna,tablero) 
        if mensaje == "ok":
            tablero[fila][columna]="X"
        else:
            print(mensaje)
            os.system('pause')
    return tablero

def turno_maquina(tablero):
    mensaje=""
    while mensaje!="ok":
        seleccion=random.randint(1,9)
        
        fila,columna=calcular_fila_columna(seleccion)
        
        mensaje=validar_ta_te_ti(seleccion,fila,columna,tablero) 
        if mensaje == "ok":
            tablero[fila][columna]="O"
    return tablero

def verificar_victoria(tablero):
    #revisar filas
    for i in range(0,3):
        resultado,marca=comprobacion_recursiva(tablero,[i,0],0,1,"",0)
        if resultado:
            return resultado,marca
    
    #revisar columnas
    for i in range(0,3):
        resultado,marca=comprobacion_recursiva(tablero,[0,i],1,0,"",0)
        if resultado:
            return resultado,marca
    
    #revisar diagonales
    for i in range(0,3,2):
        resultado,marca=comprobacion_recursiva(tablero,[0,i],1,1-i,"",0)
        if resultado:
            return resultado,marca
    
    return False,""

def precentacion_ta_te_ti(tablero):
    os.system('cls')
    print("Parece que te has desviado del camino, pero si le ganas este ta-te-ti a un vagabundo te guiara de vuelta al camino\n")
    mostrar_ta_te_ti(tablero)
    print("\n\nSolo tienes que ingresar la casilla donde queres seleccionar, y luego el vagabundo eligira")
    os.system('pause')

def mostrar_ta_te_ti(tablero):
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero[1])):
            print(f" {tablero[i][j]}",end="")
            if j<2:
                print(" |",end="")
        if i<2:
            print("\n-----------")

def mensaje_resultado(marca):
    match marca:
        case "X":
            print(f"\n\n{Fore.GREEN}Ganaste vos{Style.RESET_ALL}. Por lo que podras seguir jugando")
        case "O":
            print(f"\n\n{Fore.RED}Gano el vagabundo{Style.RESET_ALL}. Empieza de 0 :c")
        case "":
            print(f"\n\nEmpataste con el vagabundo. Vuelve a intentarlo")
    os.system('pause')

def resultado_ta_te_ti(tablero,marca):
    os.system('cls')
    mostrar_ta_te_ti(tablero)
    mensaje_resultado(marca)

#-----------------------datos-----------------------#
def validar_ta_te_ti(seleccion,fila,columna,tablero):
    retorno=""
    if type(seleccion) == int and seleccion >=1 and seleccion <= 9:
        if tablero[fila][columna] != "X" and tablero[fila][columna] != "O":
            retorno = "ok"
        else:
            retorno = "La casilla ya está ocupada, elija otra."
    else:
        retorno = "ingreso invalido, ingrese un numero del 1 al 9"
    
    return retorno

def calcular_fila_columna(seleccion):
    fila = (seleccion - 1) // 3
    columna = (seleccion - 1) % 3
    return fila,columna

def comprobacion_recursiva(tablero,inicio,x,y,anterior,iteracion):
    retorno=False,"0"
    siguiente=[inicio[0]+x,inicio[1]+y]
    if iteracion < 3:
        if iteracion == 0 or tablero[inicio[0]][inicio[1]] == anterior and tablero[inicio[0]][inicio[1]] != " ":
            retorno = comprobacion_recursiva(tablero,siguiente,x,y,tablero[inicio[0]][inicio[1]],iteracion+1)  # <--- ACA
        else:
            retorno=False,"0"
    else:
        retorno=True,anterior
    return retorno

def obtener_posicion():
    while True:
        seleccion=input("\n\n")
        if len(seleccion)==1:
            if es_numero(seleccion):
                break
            else:
                print("ingrese un numero")
        else:
            print("ingrese solo un numero del 1 al 9")
    return int(seleccion)