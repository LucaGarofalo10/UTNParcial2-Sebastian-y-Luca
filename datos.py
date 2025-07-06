import msvcrt
import time
import random
import re
import json
from colorama import init, Fore, Style
from puntuaciones import *


#========================================================== CALCULAR ===========================================================#

def tiempo_restante(inicio,tiempo_barra):
    transcurrido = time.time() - inicio
    restante = tiempo_barra - transcurrido
    return restante

def calcular_barra(inicio,barra_largo,tiempo_barra):
    restante = tiempo_restante(inicio,tiempo_barra)
    largo = int((restante / tiempo_barra) * barra_largo)
    return largo

def sumar_puntos(puntos_pregunta,resultado,dificultad):
    match dificultad:
        case 0:
            puntos = int(50 + resultado[1] * puntos_pregunta)
        case 5:
            puntos = int(100 + resultado[1] * puntos_pregunta)
        case 10:
            puntos = int(150 + resultado[1] * puntos_pregunta)
    return puntos

def posicion_puntuacion(puntos):
    retorno = len(puntuaciones)
    for i, puntuacion in enumerate(puntuaciones):
        if puntos > puntuacion["puntos"]:
            retorno = i
            break
    return retorno

def verificar_correcta(i,seleccion, correcta):
    if i == correcta:
        color = Fore.GREEN
    elif i == seleccion and seleccion != correcta:
        color = Fore.RED
    else:
        color = Style.RESET_ALL
    return color

#======================================================== OBTENER DATOS ========================================================#

def pregunta_aleatoria(preguntas,elegidas):
    vueltas = 0
    if len(elegidas) > 0:
        while vueltas < len(elegidas):
            vueltas = 0
            pregunta_actual = preguntas[random.randint(0, 4)]
            for pregunta in elegidas:
                if pregunta_actual["pregunta"] == pregunta["pregunta"]:
                    break
                vueltas += 1
    else:
        pregunta_actual = preguntas[random.randint(0, 4)]
    return pregunta_actual

def preguntas_csv(categoria,dificultad):
    preguntas_ronda = {}
    with open("preguntas.csv", encoding="utf-8") as archivo:
        for i in range(0, categoria + dificultad + 1):
            archivo.readline()
        
        for i in range(0, 5):
            pregunta = archivo.readline()
            pregunta = re.split(r',', pregunta.strip())
            preguntas_ronda[i] = {
                "pregunta": pregunta[0],
                "respuestas": pregunta[1:4],
                "correcta": int(pregunta[4]),
                "puntaje": int(pregunta[6])
            }
    return preguntas_ronda

def preguntas_y_respuestas(categoria,dificultad,elegidas):
    preguntas= preguntas_csv(categoria,dificultad)
    pregunta_actual = pregunta_aleatoria(preguntas,elegidas)
    elegidas.append(pregunta_actual)
    pregunta = pregunta_actual["pregunta"]
    respuestas = pregunta_actual["respuestas"]
    correcta = pregunta_actual["correcta"]
    puntaje = pregunta_actual["puntaje"]
    return pregunta, respuestas, correcta, puntaje

def obtener_datos_barra(dificultad):
    with open("configuracion.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    tiempo_barra = 0
    barra_largo = config["barra_largo"]
    
    match dificultad:
        case 0:
            tiempo_barra = config["dificultad_facil"]
        case 5:
            tiempo_barra = config["dificultad_normal"]
        case 10:
            tiempo_barra = config["dificultad_dificil"]
    return tiempo_barra, barra_largo

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

def mostrar_dificultad(dificultad):
    retorno = ""
    match dificultad:
        case 0:
            retorno = "Fácil"
        case 5:
            retorno = "Normal"
        case 10:
            retorno = "Difícil"
    return retorno

def guardar_puntuacion(nombre, puntos, categoria, dificultad):
    puntuacion = {}
    puntuacion["nombre"] = nombre
    puntuacion["puntos"] = puntos
    puntuacion["categoria"] = mostrar_categoria(categoria)
    puntuacion["dificultad"] = mostrar_dificultad(dificultad)

    posicion=posicion_puntuacion(puntos)
    puntuaciones.insert(posicion,puntuacion)
    return puntuaciones

#--------- Deteccion ----------#

def finalizar(inicio,barra_largo,tiempo_barra):
    retorno = False
    if calcular_barra(inicio,barra_largo,tiempo_barra) <= 0:
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

#===========================================================MINI JUEGOS===========================================================#
def validar_ta_te_ti(seleccion,fila,columna,tablero):
    retorno=""
    if type(seleccion) == int and seleccion >=1 and seleccion <= 9:
        if tablero[fila][columna] == " ":
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
            if ord(seleccion) >= ord('1') and ord(seleccion) <= ord('9'):
                break
            else:
                print("ingrese un numero")
        else:
            print("ingrese solo un numero del 1 al 9")
    return int(seleccion)