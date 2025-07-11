import os
import random
from colorama import init, Fore, Style
from datos import *

#--------- Tutorial ----------#

def mostrar_tutorial(seleccion,respuestas):
    os.system('cls')  # limpiar pantalla en Windows
    print("Para llegar a casa tenes que responder 5 preguntas correctamente, pero si te equivocas volves a empezar\n")
    
    print("Usá las flechas ↑ ↓ para moverte. → para seleccionar.\n")
    
    print("Esta será la pregunta")
    mostrar_marcadores(seleccion,respuestas,0,False)

    print("\n[=== Esta barra se ira reduciendo con el tiempo ===]")

#---------- Preparación ----------#
def elegir_categoria_dificultad(texto,opciones,categoria_dificultad):
    while True:
        os.system('cls')
        print(f"Selecciona una {categoria_dificultad}:")
        print(f"1. {texto[0]}")
        print(f"2. {texto[1]}")
        print(f"3. {texto[2]}")
        if categoria_dificultad=="categoria":
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
                if categoria_dificultad=="categoria":
                    parametro = random.choice([0, 15, 30])
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")
            case _:
                print("Opción inválida. Intenta de nuevo.")
        os.system('pause')
    return parametro

#---------- Juego ----------#
def mostrar_juego(seleccion,correcta,inicio,barra_largo,tiempo_barra,pregunta,respuestas,respuesta_correcta,ronda,categoria):
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

def mostrar_top():
    TOP=ordenar_lista_burbujeo(obtener_top(),mayor_mejor_puntos)
    a=""
    os.system('cls')
    if len(TOP) != 0:
        print("TOP Puntuaciones:\n")
        print("--------------------")
        posicion=0
        for jugador in TOP:
            posicion+=1
            print(f"{posicion}.")
            print(f"   {jugador['nombre']:<10}{jugador['mejor_puntos']:>6}\n")
            print("--------------------")
            
    else:
        print("No hay puntuaciones guardadas.")
    
    os.system('pause')

def mensaje_victoria(puntos, categoria, dificultad, aciertos, rondas, tiempo_promedio):
    os.system('cls')
    print("#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#")
    print("FELICIDADES LLEGASTE A CASA\n")
    print(f"Tu puntaje final es: {puntos} puntos")
    print(f"Preguntas acertadas: {aciertos}/{rondas}")
    print(f"Tiempo promedio por pregunta: {tiempo_promedio:.2f} segundos")
    print(f"\nCategoria: {categoria}  |  Dificultad: {dificultad}")
    print("#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-#\n")
    os.system('pause')

#================================================MINI JUEGOS================================================#

#----------ta te ti----------#
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

#----------numero aleatorio----------#
def tutorial_adivina_numero():
    os.system('cls')
    print("Parece que te has desviado del camino, pero si adivinas en que numero piensa este vagabundo te guiara de vuelta al camino")
    print("\nPero te va a ayudar, te va a dar 7 intentos, y si no acertas te dira si el numero es mayor o menor")
    print("suerte ;)\n")

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
    os.system('cls')
    if perfil=="ninguno":
        print("Parece ser que no estas en un perfi\ncrea o ingresa en uno para ver su informacion ;)\n")
    else:
        jugador, porcentaje_aciertos, porcentaje_errores, tiempo_promedio = obtener_informacion_jugador(perfil)
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





