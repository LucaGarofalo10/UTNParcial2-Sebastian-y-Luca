import os
import msvcrt
import time
from colorama import init, Fore, Style
from datos import *

#============================datos============================#

def tiempo_restante(inicio,tiempo_barra):
    transcurrido = time.time() - inicio
    restante = tiempo_barra - transcurrido
    return restante

def calcular_barra(inicio,barra_total,tiempo_barra):
    restante = tiempo_restante(inicio,tiempo_barra)
    largo = int((restante / tiempo_barra) * barra_total)
    return largo

def preguntas_y_respuestas(preguntas,ronda):
    pregunta_actual = preguntas[ronda]
    pregunta = pregunta_actual["pregunta"]
    respuestas = pregunta_actual["respuestas"]
    correcta = pregunta_actual["correcta"]
    return pregunta, respuestas, correcta

#============================deteccion============================#

def finalizar(inicio,barra_total,tiempo_barra):
    retorno = False
    if calcular_barra(inicio,barra_total,tiempo_barra) <= 0:
        retorno = True
    return retorno

def detectar_tecla():
    tecla = msvcrt.getch()
    retorno = 0
    match tecla:
        case b'H':
            retorno = 1 # Flecha arriba
        case b'P':  
            retorno = 2 # Flecha abajo
        case b'M':  
            retorno = 3 # Flecha derecha
    return retorno

#============================pantalla============================#

def menu_juego():
    retorno = False
    while True:
        os.system('cls')
        print("Bienvenido a Preguntados Runner")
        print("1. Empezar juego")
        print("2. Salir")
        opcion = input()
        match opcion:
            case "1":
                break
            case "2":
                retorno = True
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return retorno

def mostrar_menu(inicio,seleccion,pregunta,respuestas,ronda):
    os.system('cls')  # limpiar pantalla en Windows
    #print("Usá las flechas ↑ ↓ para moverte. → para seleccionar.\n")
    print(f"RONDA {ronda+1}/5")
    print(pregunta)
    for i, opcion in enumerate(respuestas):
        if i == seleccion:
            marcador = "●"
        else:
            marcador = "○"
        print(f"{marcador} {opcion}")
    print("\n" + "[" + "="*calcular_barra(inicio,barra_total,tiempo_barra) + "]")

def mostrar_correcta(inicio,seleccion,pregunta,respuestas,correcta):
    os.system('cls')  # limpiar pantalla en Windows
    #print("Usá las flechas ↑ ↓ para moverte. → para seleccionar.\n")
    print(pregunta)
    for i, opcion in enumerate(respuestas):
        if i == seleccion:
            marcador = "●"
        else:
            marcador = "○"
        
        color = ""
        if i == correcta:
            color = Fore.GREEN
        elif i == seleccion and seleccion != correcta:
            color = Fore.RED
        else:
            color = Style.RESET_ALL
        print(f"{color}{marcador} {opcion}{Style.RESET_ALL}")
        
    print("\n" + Fore.CYAN + "[" + "="*calcular_barra(inicio,barra_total,tiempo_barra) + "]" + Style.RESET_ALL) #barra frenada
    
    #mensaje de resultado
    if seleccion == correcta:
        print("Opcion " + Fore.GREEN + "⋆*⋆*CORECTA*⋆*⋆" + Style.RESET_ALL + " pasa a la siguiente pregunta")
    else:
        print("Opcion " + Fore.RED + "INCORECTA" + Style.RESET_ALL + " empieza de 0 :c")
    os.system('pause')

#============================juego============================#

def jugar_ronda(barra_total, tiempo_barra, seleccion, pregunta, respuestas, correcta, ronda):
    inicio = time.time()
    segundo_anterior = int(time.time())
    retorno = [False, 0]
    
    while True:
        # Actualizar pantalla cada segundo
        if int(time.time()) != segundo_anterior:
            segundo_anterior = int(time.time())
            mostrar_menu(inicio,seleccion,pregunta,respuestas,ronda)
        
        # Finalizar cuando se acaba el tiempo
        if finalizar(inicio,barra_total,tiempo_barra):
            restante = 0
            if seleccion == correcta:
                mostrar_correcta(inicio,seleccion,pregunta,respuestas,correcta)
                retorno[0] = True
                break
            else:
                mostrar_correcta(inicio,seleccion,pregunta,respuestas,correcta)
                break
        
        # Cambiar opcion
        if msvcrt.kbhit():
            match detectar_tecla():
                case 1:
                    seleccion = (seleccion - 1) % len(respuestas)
                case 2:
                    seleccion = (seleccion + 1) % len(respuestas)
                case 3:
                    restante = tiempo_restante(inicio,tiempo_barra)
                    mostrar_correcta(inicio,seleccion,pregunta,respuestas,correcta)
                    if seleccion == correcta:
                        retorno[0] = True
                        break
                    else:
                        break
            mostrar_menu(inicio,seleccion,pregunta,respuestas,ronda)
    
    retorno[1] = restante
    return retorno

def jugar_runer_preguntados(barra_total, tiempo_barra, seleccion):
    while True:
        if menu_juego():
            os.system('cls')
            print("¡Hasta luego!")
            exit()
        
        ronda=0
        puntos=0
        seleccion = 1
        
        while True:
            if ronda>4:
                os.system('cls')
                print("FELICIDADES LLEGASTE A CASA")
                print(f"Tu puntaje final es: {puntos} puntos")
                exit()
            pregunta,respuestas,correcta = preguntas_y_respuestas(preguntas,ronda)
            resultado = jugar_ronda(barra_total,tiempo_barra,seleccion,pregunta,respuestas,correcta,ronda)
            if resultado[0]:
                ronda+=1
                puntos+= int(100 + resultado[1] * 100)
            else:
                os.system('cls')
                print(f"Tu puntaje final es: {puntos} puntos")
                os.system('pause')
                break