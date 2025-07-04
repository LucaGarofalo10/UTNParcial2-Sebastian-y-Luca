import os
import msvcrt
import time
from outputs import *

#=============================================================== JUEGO ===============================================================#

def menu_juego():
    salir = False
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
                categoria=elegir_categoria_dificultad(["Ciencia","Historia","Entretenimiento"],[0, 15, 30],True)
                dificultad=elegir_categoria_dificultad(["Fácil","Media","Difícil"],[0, 5, 10],False)
                break
            case "2":
                tutorial()
            case "3":
                mostrar_puntuacion()
            case "4":
                salir = True
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return salir,categoria,dificultad

def jugar_runer_preguntados():
    while True:
        salir,categoria,dificultad = menu_juego()
        if salir:
            os.system('cls')
            print("¡Hasta luego!")
            exit()
        tiempo_barra, barra_largo = obtener_datos_barra(dificultad)
        
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
                guardar_puntuacion(nombre, puntos, categoria, dificultad)
                break
            
            pregunta,respuestas,correcta,puntos_pregunta = preguntas_y_respuestas(categoria,dificultad,elegidas)
            resultado = jugar_ronda(barra_largo,tiempo_barra,seleccion,pregunta,respuestas,correcta,ronda,categoria)
            
            if resultado[0]:
                ronda+=1
                puntos += sumar_puntos(puntos_pregunta, resultado, dificultad)
            else:
                break

def jugar_ronda(barra_largo, tiempo_barra, seleccion, pregunta, respuestas, correcta, ronda, categoria):
    inicio = time.time()
    segundo_anterior = int(time.time())
    retorno = [False, 0]
    
    while True:
        # Actualizar pantalla cada segundo
        if int(time.time()) != segundo_anterior:
            segundo_anterior = int(time.time())
            mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,None,ronda,categoria,False)

        # Finalizar cuando se acaba el tiempo
        if finalizar(inicio,barra_largo,tiempo_barra):
            restante = 0
            if seleccion == correcta:
                retorno[0] = True
            mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria,True)
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
                    mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,correcta,ronda,categoria,True)
                    if seleccion == correcta:
                        retorno[0] = True
                        break
                    else:
                        break
            mostrar_juego(inicio,seleccion,barra_largo,tiempo_barra,pregunta,respuestas,None,ronda,categoria,False)

    retorno[1] = restante
    return retorno
