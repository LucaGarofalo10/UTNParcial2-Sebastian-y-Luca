import os
import msvcrt
import time
import random
from colorama import init, Fore, Style
from datos import *

#========================================================== DATOS ==========================================================#

def tiempo_restante(inicio,tiempo_barra):
    transcurrido = time.time() - inicio
    restante = tiempo_barra - transcurrido
    return restante

def calcular_barra(inicio,barra_total,tiempo_barra):
    restante = tiempo_restante(inicio,tiempo_barra)
    largo = int((restante / tiempo_barra) * barra_total)
    return largo

def pregunta_aleatoria(preguntas,categoria,dificultad,elegidas):
    vueltas = 0
    if len(elegidas) > 0:
        while vueltas < len(elegidas):
            vueltas = 0
            pregunta_actual = preguntas[random.randint(0, 4) + categoria + dificultad]
            for pregunta in elegidas:
                if pregunta_actual["pregunta"] == pregunta["pregunta"]:
                    break
                vueltas += 1
    else:
        pregunta_actual = preguntas[random.randint(0, 4) + categoria + dificultad]
    return pregunta_actual

def preguntas_y_respuestas(preguntas,categoria,dificultad,elegidas):
    pregunta_actual = pregunta_aleatoria(preguntas,categoria,dificultad,elegidas)
    elegidas.append(pregunta_actual)
    pregunta = pregunta_actual["pregunta"]
    respuestas = pregunta_actual["respuestas"]
    correcta = pregunta_actual["correcta"]
    return pregunta, respuestas, correcta

def sumar_puntos(puntos,resultado,dificultad):
    match dificultad:
        case 0:
            puntos+= int(50 + resultado[1] * 50)
        case 5:
            puntos+= int(100 + resultado[1] * 100)
        case 10:
            puntos+= int(150 + resultado[1] * 150)
    return puntos

def obtener_tiempo_barra(dificultad):
    match dificultad:
        case 0:
            tiempo_barra = dificultad_facil
        case 5:
            tiempo_barra = dificultad_normal
        case 10:
            tiempo_barra = dificultad_dificil
    return tiempo_barra

#========================================================== DETECCION ==========================================================#

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

#=========================================================== PANTALLA ===========================================================#

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
    for i, opcion in enumerate(respuestas):
        if i == seleccion:
            marcador = "●"
        else:
            marcador = "○"
        print(f"{marcador} {opcion}")
        
    print("\n[=== Esta barra se ira reduciendo con el tiempo ===]")

#---------- Preparación ----------#

def elegir_dificultad():
    while True:
        os.system('cls')
        print("Selecciona la dificultad:")
        print("1. Fácil")
        print("2. Medio")
        print("3. Difícil")
        dificultad=input()
        match dificultad:
            case "1":
                dificultad = 0
                break
            case "2":
                dificultad = 5
                break
            case "3":
                dificultad = 10
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return dificultad

def elegir_categoria():
    while True:
        os.system('cls')
        print("Selecciona una categoría:")
        print("1. Ciencia")
        print("2. Historia")
        print("3. Entretenimiento")
        print("4. Aleatoria")
        categoria=input()
        match categoria:
            case "1":
                categoria = 0
                break
            case "2":
                categoria = 15
                break
            case "3":
                categoria = 30
                break
            case "4":
                categoria = random.choice([0, 15, 30])
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return categoria

def mostrar_categoria(categoria):
    retorno = ""
    match categoria:
        case 0:
            retorno = "Ciencia"
        case 15:
            retorno = "Historia"
        case 30:
            retorno = "Entretenimiento"
    return retorno

def guardar_puntuacion(nombre, puntos):
    puntuacion = {}
    puntuacion["nombre"] = nombre
    puntuacion["puntos"] = puntos
    puntuaciones.append(puntuacion)
    return puntuaciones

#---------- Juego ----------# 
def mostrar_juego(inicio,seleccion,tiempo_barra,pregunta,respuestas,ronda,categoria):
    os.system('cls')  # limpiar pantalla en Windows

    print(f"Categoría: {mostrar_categoria(categoria)} | RONDA {ronda+1}/5\n")
    print(pregunta)
    for i, opcion in enumerate(respuestas):
        if i == seleccion:
            marcador = "●"
        else:
            marcador = "○"
        print(f"{marcador} {opcion}")
    print("\n" + "[" + "="*calcular_barra(inicio,barra_total,tiempo_barra) + "]")

def mostrar_correcta(inicio,seleccion,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria):
    os.system('cls')  # limpiar pantalla en Windows

    print(f"Categoría: {mostrar_categoria(categoria)} | RONDA {ronda+1}/5\n")
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

def mostrar_puntuacion():
    os.system('cls')
    print("Puntuaciones:")
    if len(puntuaciones) == 0:
        print("No hay puntuaciones guardadas.")
    for puntuacion in puntuaciones:
        if puntuacion["nombre"] == "":
            print(f"?????: ", end="")
        else:
            print(f"{puntuacion['nombre']}: ", end="")
        print(f"{puntuacion['puntos']} puntos")
    os.system('pause')
#=============================================================== JUEGO ===============================================================#

def menu_juego():
    retorno = False
    categoria = 0
    dificultad = 0
    while True:
        os.system('cls')
        print("Bienvenido a Preguntados Runner")
        print("1. Empezar juego")
        print("2. Tutorial")
        print("3. Puntuaciones")
        print("4. Salir")
        opcion = input()
        match opcion:
            case "1":
                categoria=elegir_categoria()
                dificultad=elegir_dificultad()
                break
            case "2":
                tutorial()
            case "3":
                mostrar_puntuacion()
            case "4":
                retorno = True
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return retorno,categoria,dificultad

def jugar_runer_preguntados():
    while True:
        salir,categoria,dificultad = menu_juego()
        if salir:
            os.system('cls')
            print("¡Hasta luego!")
            exit()
        
        ronda=0
        puntos=0
        seleccion = 1
        
        elegidas = []
        while True:
            if ronda>4:
                os.system('cls')
                print("FELICIDADES LLEGASTE A CASA\n")
                print(f"Tu puntaje final es: {puntos} puntos")
                os.system('pause')
                nombre = input("\nIngresa un nombre para guardar tu puntaje: ")
                guardar_puntuacion(nombre, puntos)
                break
            
            pregunta,respuestas,correcta = preguntas_y_respuestas(preguntas,categoria,dificultad,elegidas)
            tiempo_barra = obtener_tiempo_barra(dificultad)
            resultado = jugar_ronda(barra_total,tiempo_barra,seleccion,pregunta,respuestas,correcta,ronda,categoria)
            if resultado[0]:
                ronda+=1
                puntos = sumar_puntos(puntos, resultado, dificultad)

            else:
                os.system('cls')
                print(f"Tu puntaje final es: {puntos} puntos\n")
                nombre = input("Ingresa un nombre para guardar tu puntaje: ")
                guardar_puntuacion(nombre, puntos)
                os.system('pause')
                break

def jugar_ronda(barra_total, tiempo_barra, seleccion, pregunta, respuestas, correcta, ronda, categoria):
    inicio = time.time()
    segundo_anterior = int(time.time())
    retorno = [False, 0]
    
    while True:
        # Actualizar pantalla cada segundo
        if int(time.time()) != segundo_anterior:
            segundo_anterior = int(time.time())
            mostrar_juego(inicio,seleccion,tiempo_barra,pregunta,respuestas,ronda,categoria)

        # Finalizar cuando se acaba el tiempo
        if finalizar(inicio,barra_total,tiempo_barra):
            restante = 0
            if seleccion == correcta:
                mostrar_correcta(inicio,seleccion,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria)
                retorno[0] = True
                break
            else:
                mostrar_correcta(inicio,seleccion,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria)
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
                    mostrar_correcta(inicio,seleccion,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria)
                    if seleccion == correcta:
                        retorno[0] = True
                        break
                    else:
                        break
            mostrar_juego(inicio,seleccion,tiempo_barra,pregunta,respuestas,ronda,categoria)
    
    retorno[1] = restante
    return retorno
