import os
from outputs import *
import random

#============================================================ JUEGO ============================================================#
def comprobar_victoria(puntos, categoria, dificultad, aciertos, rondas, ronda, tiempo_partida, perfil):
    victoria=False
    
    if ronda>=rondas:
        mensaje_victoria(puntos, categoria, dificultad, aciertos, rondas, tiempo_partida/aciertos)
        victoria=True
        perfil=comprobar_sin_perfil(perfil)
        
        if perfil!="ninguno":
            guardar_datos(puntos,aciertos,rondas,tiempo_partida,perfil,categoria,dificultad)
            os.system('cls')
            print("¡¡¡Datos guardado!!!")
            print("Accede a perfiles para verlos reflejados")
            os.system('pause')
    
    return victoria, perfil

#================================================MINI JUEGOS================================================#

#----------ta te ti----------#
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

#----------numero aleatorio----------#
def adivina_numero_recursivo(aleatorio,inicio,fin,iteracion):
    os.system('pause')
    if iteracion>6:
        retorno=False
    else:
        numero=recivir_numero(inicio,fin)
        
        if numero==aleatorio:
            retorno=True
        else:
            if numero>aleatorio:
                fin=numero-1
            else:
                inicio=numero+1
            retorno=adivina_numero_recursivo(aleatorio,inicio,fin,iteracion+1)
    return retorno

def recivir_numero(inicio,fin):
    while True:
        os.system('cls')
        numero=input(f"Adivina el numero del {inicio} al {fin}\n")
        if es_numero(numero):
            numero=int(numero)
            if numero>=inicio and numero<=fin:
                break
            else:
                print(f"Valor invalido, tiene que estar entre {inicio} y {fin}")
                os.system('pause')
        else:
            print("ingrese un numero")
            os.system('pause')
    
    return numero

#----------Perfiles----------#
def cambiar_cuenta(perfil):
    while True:
        jugadores = obtener_jugadores()
        nombre=ingresar_nombre(jugadores)
        
        #reiniciar si eligui la cuenta en la que esta
        if nombre==perfil:
            os.system('cls')
            print("Ya estas en esta cuenta")
            os.system('pause')
            continue
        
        #salir si pone exit
        if nombre=="exit":
            break
        
        #verificar si la cuenta existe
        jugador,encontrado = obtener_jugador(jugadores, nombre)
        if encontrado:
            #verificar si la contraseña coincide
            if ingresar_contraseña(jugador):
                perfil=nombre
            break
        else:
            print("Cuenta no encontrada, intente otra ves")
            os.system('pause')
    return perfil

def ingresar_contraseña(jugador):
    retorno = False
    #ingresar directamente si no tiene contraseña
    if sin_contraseña(jugador):
        mensaje_ingreso(jugador['nombre'])
        retorno = True
    else:
        while True:
            os.system('cls')
            print("Ingrese la contraseña")
            print("'exit' para cancelar")
            contraseña = input("\n")
            
            #salir si pone exit
            if contraseña=="exit":
                retorno = True
                break
            
            #comprobar si la contraseña coincide y volver a pedirla si no coincide
            if jugador["contraseña"]==contraseña:
                retorno = True
                mensaje_ingreso(jugador['nombre'])
                break
            else:
                os.system('cls')
                print("Contraseña incorrecta")
                os.system('pause')
    return retorno

def ingresar_nombre(jugadores):
    os.system('cls')
    print("¿A que cuenta queres cambiar?\n")
    mostrar_jugadores(jugadores)
    print("'exit' para cancelar")
    nombre=input("\nIngrese el nombre de la cuenta:\n")
    return nombre

def crear_cuenta(perfil):
    jugadores,nuevo_jugador = agregar_usuario()
    if nuevo_jugador['nombre']=="":
        return perfil
    cargar_jugadores(jugadores)
    return nuevo_jugador['nombre']

def comprobar_sin_perfil(perfil):
    while True:
        os.system('cls')
        if perfil=="ninguno":
            print("Al parecer no tienes un perfil ¿que quieres hacer entonces?\n")
            print("1. Ingresar en un perfil")
            print("2. Crear un perfil")
            print("3. Salir (se perdera tu puntuacion)")
            opcion=input("\n")
            match opcion:
                case "1":
                    perfil = cambiar_cuenta(perfil)
                    break
                case "2":
                    perfil = crear_cuenta(perfil)
                    break
                case "3":
                    break
                case _:
                    print("Opción inválida. Intenta de nuevo.")
                    os.system('pause')
    return perfil
