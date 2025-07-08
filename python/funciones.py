import os
import msvcrt
import time
from outputs import *
from datos import *
#from datos import finalizar, guardar_puntuacion, obtener_configuracion, sumar_puntos, preguntas_y_respuestas, tiempo_restante, detectar_tecla, verificar_victoria, obtener_posicion, obtener_jugadores, sin_contraseña, cargar_jugadores, agregar_usuario, validar_ta_te_ti, calcular_fila_columna, obtener_jugador
import random

#============================================================ JUEGO ============================================================#
def menu_juego():
    salir = False
    categoria = 0
    dificultad = 0
    perfil="ninguno"
    while True:
        os.system('cls')
        print("Bienvenido a Preguntados Runner")
        print("1. Empezar juego")
        print("2. Tutorial")
        print("3. Puntuaciones")
        print(f"4. Perfil ({perfil})")
        print("5. Salir")
        opcion = input()
        match opcion:
            case "1":
                categoria=elegir_categoria_dificultad(["Ciencia","Historia","Entretenimiento"],[0, 15, 30],True)
                dificultad=elegir_categoria_dificultad(["Fácil","Media","Difícil"],[0, 5, 10],False)
                break
            case "2":
                tutorial()
            case "3":
                mostrar_puntuacion()
            case "4":
                menu_perfiles(perfil)
                pass
            case "5":
                salir = True
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return salir,categoria,dificultad

def mensaje_victoria(puntos, categoria, dificultad):
    os.system('cls')
    print("FELICIDADES LLEGASTE A CASA\n")
    print(f"Tu puntaje final es: {puntos} puntos")
    os.system('pause')
    nombre = input("\nIngresa un nombre para guardar tu puntaje: ")
    guardar_puntuacion(nombre, puntos, categoria, dificultad)

def jugar_runer_preguntados():
    while True:
        salir,categoria,dificultad = menu_juego()
        if salir:
            os.system('cls')
            print("¡Hasta luego!")
            exit()
        rondas, tiempo_barra, barra_largo, intentos_mini = obtener_configuracion(dificultad)
        
        ronda=0
        puntos=0
        seleccion = 1
        elegidas = []
        
        while True:
            if ronda>=rondas:
                mensaje_victoria(puntos, categoria, dificultad)
                break
        
            pregunta,respuestas,correcta,puntos_pregunta = preguntas_y_respuestas(categoria,dificultad,elegidas)
            resultado = jugar_ronda(barra_largo,tiempo_barra,seleccion,pregunta,respuestas,correcta,ronda,categoria,intentos_mini)
            intentos_mini=resultado[2]
            
            if resultado[0]:
                ronda+=1
                puntos += sumar_puntos(puntos_pregunta, resultado, dificultad)
            else:
                print("Te quedaste sin oportunidades de mini juego, empieza de 0 :c")
                os.system('pause')
                break

def jugar_ronda(barra_largo, tiempo_barra, seleccion, pregunta, respuestas, correcta, ronda, categoria, intentos_mini):
    inicio = time.time()
    segundo_anterior = int(time.time())
    resultado=False
    while True:
        # Actualizar pantalla cada segundo
        if int(time.time()) != segundo_anterior:
            segundo_anterior = int(time.time())
            mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,None,ronda,categoria,False)

        # Finalizar cuando se acaba el tiempo
        if finalizar(inicio,barra_largo,tiempo_barra):
            restante = 0
            transcurrido=tiempo_barra
            mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria,True)
            if seleccion == correcta:
                resultado=True
            else:
                if intentos_mini > 0:
                    if not mini_juego():
                        break
                    resultado=True
                    intentos_mini-=1
                    print(f"\nTe quedan {intentos_mini} intentos de mini juego.")
                    os.system('pause')
            break
        
        # Cambiar opcion
        if msvcrt.kbhit():
            match detectar_tecla():
                case 1:
                    seleccion = (seleccion - 1) % len(respuestas)
                case 2:
                    seleccion = (seleccion + 1) % len(respuestas)
                case 3:
                    restante, transcurrido = tiempo_restante(inicio,tiempo_barra)
                    mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria,True)
                    if seleccion == correcta:
                        resultado=True
                    else:
                        if intentos_mini > 0:
                            if not mini_juego():
                                break
                            resultado=True
                            intentos_mini-=1
                            print(f"\nTe quedan {intentos_mini} intentos de mini juego.")
                            os.system('pause')
                    break
            mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,None,ronda,categoria,False)

    return resultado, restante, intentos_mini, transcurrido

#----------Mini juego----------#
def mini_juego():
    resultado = None
    while resultado == None:
        resultado = ta_te_ti() 
    return resultado

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

#----------Perfiles----------#
def menu_perfiles(perfil):
    while True:
        mostrar_menu_perfiles(perfil)
        opcion = input()
        match opcion:
            case "1":
                ver_informacion(perfil)
            case "2":
                perfil = cambiar_cuenta(perfil)
            case "3":
                perfil = crear_cuenta()
            case "4":
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return perfil

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

def crear_cuenta():
    jugadores,nuevo_jugador= agregar_usuario()
    cargar_jugadores(jugadores)
    return nuevo_jugador['nombre']

jugar_runer_preguntados()