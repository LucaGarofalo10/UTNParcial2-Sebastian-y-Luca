import os
import time
from outputs import *
from ta_te_ti import ta_te_ti
from adivinar_numero import adivina_numero
from perfiles import menu_perfiles, comprobar_sin_perfil


def menu_juego(perfil):
    salir = False
    categoria = 0
    dificultad = 0
    while True:
        os.system("cls")
        print("Bienvenido a Preguntados Runner")
        print("1. Empezar juego")
        print("2. Tutorial")
        print("3. Top puntuaciones")
        print(f"4. Perfil ({perfil})")
        print("5. Salir")
        opcion = input()
        match opcion:
            case "1":
                categoria = elegir_categoria_dificultad(
                    ["Ciencia", "Historia", "Entretenimiento"], [0, 15, 30], "categoria"
                )
                dificultad = elegir_categoria_dificultad(
                    ["Fácil", "Media", "Difícil"], [0, 5, 10], "dificultad"
                )
                break
            case "2":
                tutorial()
            case "3":
                mostrar_top()
            case "4":
                perfil = menu_perfiles(perfil)
                pass
            case "5":
                salir = True
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system("pause")
    return salir, categoria, dificultad, perfil


def jugar_runer_preguntados():
    perfil = "ninguno"

    while True:
        salir, categoria, dificultad, perfil = menu_juego(perfil)
        if salir:
            os.system("cls")
            print("¡Hasta luego!")
            exit()
        rondas, tiempo_barra, barra_largo, intentos_mini = obtener_configuracion(
            dificultad
        )

        ronda = 0
        puntos = 0
        aciertos = 0
        tiempo_partida = 0
        seleccion = 1
        elegidas = set()

        while True:
            # Comprobamos si gano
            victoria, perfil = comprobar_victoria(
                puntos,
                categoria,
                dificultad,
                aciertos,
                rondas,
                ronda,
                tiempo_partida,
                perfil,
            )
            if victoria:
                break

            pregunta, respuestas, correcta, puntos_pregunta = preguntas_y_respuestas(
                categoria, dificultad, elegidas
            )
            resultado, restante, intentos_mini, transcurrido, aciertos = jugar_ronda(
                barra_largo,
                tiempo_barra,
                seleccion,
                pregunta,
                respuestas,
                correcta,
                ronda,
                categoria,
                intentos_mini,
                aciertos,
            )
            # intentos_mini=resultado[2]

            if resultado:
                ronda += 1
                tiempo_partida += transcurrido
                puntos += sumar_puntos(puntos_pregunta, restante, dificultad)
            else:
                os.system("cls")
                print("Te quedaste sin oportunidades de mini juego, empieza de 0 :c")
                os.system("pause")
                break


def jugar_ronda(
    barra_largo,
    tiempo_barra,
    seleccion,
    pregunta,
    respuestas,
    correcta,
    ronda,
    categoria,
    intentos_mini,
    aciertos,
):
    inicio = time.time()
    segundo_anterior = int(time.time())
    resultado = False
    sin_tiempo = False

    mostrar_juego(
        seleccion,
        False,
        inicio,
        barra_largo,
        tiempo_barra,
        pregunta,
        respuestas,
        None,
        ronda,
        categoria,
    )
    while True:
        # Actualizar pantalla cada segundo
        if int(time.time()) != segundo_anterior:
            segundo_anterior = int(time.time())
            mostrar_juego(
                seleccion,
                False,
                inicio,
                barra_largo,
                tiempo_barra,
                pregunta,
                respuestas,
                None,
                ronda,
                categoria,
            )

        # Finalizar cuando se acaba el tiempo
        if finalizar(inicio, barra_largo, tiempo_barra):
            mostrar_juego(
                seleccion,
                True,
                inicio,
                barra_largo,
                tiempo_barra,
                pregunta,
                respuestas,
                correcta,
                ronda,
                categoria,
            )
            resultado, intentos_mini, aciertos = seleccionar_respuesta(
                seleccion, correcta, intentos_mini, aciertos
            )
            sin_tiempo = True
            break

        # Cambiar opcion
        resultado, terminar, seleccion, intentos_mini, aciertos = detectar_tecla(
            seleccion,
            respuestas,
            False,
            (seleccion, correcta, intentos_mini, aciertos),
            mostrar_juego,
            (
                inicio,
                barra_largo,
                tiempo_barra,
                pregunta,
                respuestas,
                correcta,
                ronda,
                categoria,
            ),
        )
        if terminar:
            break

    restante, transcurrido = tiempo_restante(inicio, tiempo_barra, sin_tiempo)
    return resultado, restante, intentos_mini, transcurrido, aciertos


def detectar_tecla(
    seleccion,
    respuestas,
    tutorial,
    parametros_seleccionar,
    funcion_mostrar,
    parametros_mostrar,
):
    terminar = False
    resultado = False

    intentos_mini = parametros_seleccionar[2]
    aciertos = parametros_seleccionar[3]

    if msvcrt.kbhit():
        match definir_tecla():
            case 1:
                seleccion = (seleccion - 1) % len(respuestas)
            case 2:
                seleccion = (seleccion + 1) % len(respuestas)
            case 3:
                terminar = True
                if not tutorial:
                    funcion_mostrar(seleccion, True, *parametros_mostrar)
                    resultado, intentos_mini, aciertos = seleccionar_respuesta(
                        *parametros_seleccionar
                    )
        if tutorial:
            funcion_mostrar(seleccion, respuestas)
        else:
            funcion_mostrar(seleccion, False, *parametros_mostrar)

    return resultado, terminar, seleccion, intentos_mini, aciertos


def seleccionar_respuesta(seleccion, correcta, intentos_mini, aciertos):
    if seleccion == correcta:
        aciertos += 1
        resultado = True
    else:
        if intentos_mini > 0:
            if mini_juego():
                resultado = True
                intentos_mini -= 1
                print(f"\nTe quedan {intentos_mini} intentos de mini juego.")
                os.system("pause")
            else:
                resultado = False
        else:
            resultado = False
    return resultado, intentos_mini, aciertos


def comprobar_victoria(
    puntos, categoria, dificultad, aciertos, rondas, ronda, tiempo_partida, perfil
):
    victoria = False

    if ronda >= rondas:
        mensaje_victoria(
            puntos, categoria, dificultad, aciertos, rondas, tiempo_partida / aciertos
        )
        victoria = True
        perfil = comprobar_sin_perfil(perfil)

        if perfil != "ninguno":
            guardar_datos(
                puntos, aciertos, rondas, tiempo_partida, perfil, categoria, dificultad
            )
            os.system("cls")
            print("¡¡¡Datos guardado!!!")
            print("Accede a perfiles para verlos reflejados")
            os.system("pause")

    return victoria, perfil


# --------------------tutorial--------------------#
def tutorial():
    segundo_anterior = int(time.time())
    seleccion = 1
    respuestas = [
        "Estas seran las respuestas",
        "Puedes elegirla con → pero si se acaba el tiempo",
        "Se elige la que estes seleccionando",
    ]
    while True:
        # Actualizar pantalla cada segundo
        if int(time.time()) != segundo_anterior:
            segundo_anterior = int(time.time())
            mostrar_tutorial(seleccion, respuestas)

        # Cambiar opcion
        a, terminar, seleccion, b, c = detectar_tecla(
            seleccion, respuestas, True, (0, 0, 0, 0), mostrar_tutorial, ()
        )
        if terminar:
            break


# --------------------mini juegos--------------------#
def mini_juego():
    resultado = None
    while resultado == None:
        funcion_mini_juego = random.choice([ta_te_ti, adivina_numero])
        resultado = funcion_mini_juego()
    return resultado


jugar_runer_preguntados()
