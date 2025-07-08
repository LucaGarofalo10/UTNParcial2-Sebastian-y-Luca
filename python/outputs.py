import os
import msvcrt
import time
import random
from colorama import init, Fore, Style
from datos import *

#--------- Tutorial ----------# 
def tutorial():
    segundo_anterior = int(time.time())
    seleccion = 1
    respuestas = ["Estas seran las respuestas","Puedes elegirla con → pero si se acaba el tiempo","Se elige la que estes seleccionando"]
    while True:
        # Actualizar pantalla cada segundo
        if int(time.time()) != segundo_anterior:
            segundo_anterior = int(time.time())
            mostrar_tutorial(seleccion,respuestas)
        
        # Cambiar opcion
        if msvcrt.kbhit():
            match detectar_tecla():
                case 1:
                    seleccion = (seleccion - 1) % len(respuestas)
                case 2:
                    seleccion = (seleccion + 1) % len(respuestas)
                case 3:
                    break
            mostrar_tutorial(seleccion,respuestas)

def mostrar_tutorial(seleccion,respuestas):
    os.system('cls')  # limpiar pantalla en Windows
    print("Para llegar a casa tenes que responder 5 preguntas correctamente, pero si te equivocas volves a empezar\n")
    
    print("Usá las flechas ↑ ↓ para moverte. → para seleccionar.\n")
    
    print("Esta será la pregunta")
    mostrar_marcadores(seleccion,respuestas,0,False)

    print("\n[=== Esta barra se ira reduciendo con el tiempo ===]")

#---------- Preparación ----------#
def elegir_categoria_dificultad(texto,opciones,categoria):
    while True:
        os.system('cls')
        print("Selecciona una categoría:")
        print(f"1. {texto[0]}")
        print(f"2. {texto[1]}")
        print(f"3. {texto[2]}")
        if categoria:
            print("4. Aleatoria")
        parametro=input()
        match parametro:
            case "1":
                parametro = opciones[0]
                break
            case "2":
                parametro = opciones[1]
                break
            case "3":
                parametro = opciones[2]
                break
            case "4":
                if categoria:
                    parametro = random.choice([0, 15, 30])
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")
                    os.system('pause')
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return parametro

#---------- Juego ----------# 
def mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,respuesta_correcta,ronda,categoria,correcta):
    os.system('cls')  # limpiar pantalla en Windows
    color = Style.RESET_ALL
    print(f"Categoría: {mostrar_categoria(categoria)} | RONDA {ronda+1}/5\n")
    print(pregunta)
    
    mostrar_marcadores(seleccion,respuestas,correcta,respuesta_correcta)
    
    if correcta:
        color = Fore.CYAN
    
    print(f"\n{color}[{"="*calcular_barra(inicio,barra_largo,tiempo_barra)}]{Style.RESET_ALL}")
    
    if correcta:
        mostrar_mensaje_resultado(seleccion, respuesta_correcta)

def mostrar_marcadores(seleccion,respuestas,mostrar_correcta,correcta):
    for i, opcion in enumerate(respuestas):
        #establecemos el color en blanco por defecto
        color = Style.RESET_ALL
        if i == seleccion:
            marcador = "●"
        else:
            marcador = "○"
        #si queremos mostrar la correcta, cambiamos el color
        if mostrar_correcta:
            color=verificar_correcta(i,seleccion,correcta)
        print(f"{color}{marcador} {opcion}{Style.RESET_ALL}")

def mostrar_mensaje_resultado(seleccion, correcta):
    if seleccion == correcta:
        print("Opcion " + Fore.GREEN + "⋆*⋆*CORRECTA*⋆*⋆" + Style.RESET_ALL + " pasa a la siguiente pregunta")
    else:
        print("Opcion " + Fore.RED + "INCORRECTA" + Style.RESET_ALL + " pero puede que tengas otra oportunidad")
    os.system('pause')

def mostrar_puntuacion():
    os.system('cls')
    jugador=0
    if len(puntuaciones) == 0:
        print("No hay puntuaciones guardadas.")
    else:
        print("Puntuaciones:")
    for puntuacion in puntuaciones:
        jugador+=1
        print(f"{jugador}- ", end="")
        if puntuacion["nombre"] == "":
            print(f"?????: ", end="")
        else:
            print(f"{puntuacion['nombre']}: ", end="")
        print(f"{puntuacion['puntos']} puntos   ", end="")
        print(f"{puntuacion['categoria']}-{puntuacion['dificultad']}")
    os.system('pause')

#---------mini juegos---------#
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

def resultado_ta_te_ti(tablero,marca):
    os.system('cls')
    mostrar_ta_te_ti(tablero)
    match marca:
        case "X":
            print(f"\n\n{Fore.GREEN}Ganaste vos{Style.RESET_ALL}. Por lo que podras seguir jugando")
        case "O":
            print(f"\n\n{Fore.RED}Gano el vagabundo{Style.RESET_ALL}. Empieza de 0 :c")
        case "":
            print(f"\n\nEmpataste con el vagabundo. Vuelve a intentarlo")
    os.system('pause')

#----------Perfiles----------#
def mostrar_menu_perfiles(perfil):
    os.system('cls')
    if perfil != "ninguno":
        print(f"Hola {perfil} ¿que queres hacer?\n")
    else:
        print(f"Bienvenido ¿quieres crearte una cuenta o seleccionar una?\n")
    print("1. Informacion")
    if perfil != "ninguno":
        print("2. Cambiar cuenta")
    else:
        print("2. Seleccionar cuenta")
    print("3. Crear cuenta")
    print("4. Salir")

def ver_informacion(perfil):
    jugador, porcentaje_aciertos, porcentaje_errores, tiempo_promedio = obtener_informacion_jugador(perfil)
    os.system('cls')
    print("\n|------------Datos del jugador------------|")
    print(f"Nombre: {jugador['nombre']}")
    print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")
    print(f"Porcentaje de errores: {porcentaje_errores:.2f}%")
    print(f"Tiempo promedio: {tiempo_promedio:.2f}s")
    print("\n|--------------Mejor partida--------------|")
    print(f"Puntos: {jugador['mejor_puntos']}")
    print(f"Tiempo: {jugador['mejor_tiempo']}s")
    print(f"Dificultad: {jugador['mejor_dificultad']}")
    print(f"Categoría: {jugador['mejor_categoria']}")
    os.system('pause')

def mostrar_jugadores(jugadores):
    for i, jugador in enumerate(jugadores, 1):
        print(f"{i}. {jugador['nombre']}")

def mensaje_ingreso(nombre):
    os.system('cls')
    print(f"Bienvenido {nombre}")
    os.system('pause')





