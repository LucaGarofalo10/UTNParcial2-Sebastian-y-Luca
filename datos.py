import msvcrt
import time
import random
import re
import json
import os
from colorama import init, Fore, Style

#========================================================== CALCULAR ===========================================================#

def tiempo_restante(inicio,tiempo_barra,sin_tiempo):
    transcurrido = time.time() - inicio
    restante = tiempo_barra - transcurrido
    if sin_tiempo:
        restante=0
        transcurrido=tiempo_barra
    return restante, transcurrido

def calcular_barra(inicio,barra_largo,tiempo_barra):
    restante, transcurrido = tiempo_restante(inicio,tiempo_barra,False)
    largo = int((restante / tiempo_barra) * barra_largo)
    return largo

def sumar_puntos(puntos_pregunta,restante,dificultad):
    match dificultad:
        case 0:
            puntos = int(50 + restante * puntos_pregunta)
        case 5:
            puntos = int(100 + restante * puntos_pregunta)
        case 10:
            puntos = int(150 + restante * puntos_pregunta)
    return puntos

def verificar_correcta(i,seleccion, correcta):
    if i == correcta:
        color = Fore.GREEN
    elif i == seleccion and seleccion != correcta:
        color = Fore.RED
    else:
        color = Style.RESET_ALL
    return color

def calcular_porcentaje(Dividendo,Divisor):
    return (Dividendo / Divisor) * 100

#======================================================== OBTENER DATOS ========================================================#

def pregunta_aleatoria(preguntas,elegidas):
    vueltas = 0
    if len(elegidas) > 0:
        while vueltas < len(elegidas):
            vueltas = 0
            pregunta_actual = preguntas[random.randint(0, 4)]
            for pregunta in elegidas:
                if pregunta_actual['pregunta'] == pregunta:
                    break
                vueltas += 1
    else:
        pregunta_actual = preguntas[random.randint(0, 4)]
    return pregunta_actual

def preguntas_csv(categoria,dificultad):
    preguntas_ronda = {}
    try:
        with open("datos/preguntas.csv", encoding="utf-8") as archivo:
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
    except Exception:
        preguntas_ronda = {}
        print("algo fallo al leer el archivo")
    return preguntas_ronda

def preguntas_y_respuestas(categoria,dificultad,elegidas):
    preguntas= preguntas_csv(categoria,dificultad)
    pregunta_actual = pregunta_aleatoria(preguntas,elegidas)
    elegidas.add(pregunta_actual['pregunta'])
    pregunta = pregunta_actual["pregunta"]
    respuestas = pregunta_actual["respuestas"]
    correcta = pregunta_actual["correcta"]
    puntaje = pregunta_actual["puntaje"]
    return pregunta, respuestas, correcta, puntaje

def obtener_configuracion(dificultad):
    try:
        with open("datos/configuracion.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        
        tiempo_barra = 0
        barra_largo = config["barra_largo"]
        rondas = config["rondas"]
        intentos_mini = config["intentos_mini"]
        
        match dificultad:
            case 0:
                tiempo_barra = config["dificultad_facil"]
            case 5:
                tiempo_barra = config["dificultad_normal"]
            case 10:
                tiempo_barra = config["dificultad_dificil"]
    except Exception:
        rondas=None
        tiempo_barra=None
        barra_largo=None
        intentos_mini=None
        print("algo fallo al leer el archivo")
    return rondas, tiempo_barra, barra_largo, intentos_mini

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

def ordenar_lista_burbujeo(lista,comprobacion):
    for i in range(0,len(lista)):
        for j in range(i+1,len(lista)):
            if comprobacion(lista[i],lista[j]):
                aux=lista[j]
                lista[j]=lista[i]
                lista[i]=aux
    return lista

#--------- Deteccion ----------#
def finalizar(inicio,barra_largo,tiempo_barra):
    retorno = False
    if calcular_barra(inicio,barra_largo,tiempo_barra) <= 0:
        retorno = True
    return retorno

def definir_tecla():
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

#--------- Especificas ----------#
def mayor_mejor_puntos(jugador1,jugador2):
    retorno =False
    if jugador1['mejor_puntos'] < jugador2['mejor_puntos']:
        retorno = True
    return retorno

#===========================================================MINI JUEGO===========================================================#

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

#===========================================================PERFILES===========================================================#
def agregar_usuario():
    jugadores=obtener_jugadores()
    while True:
        os.system('cls')
        nombre = input("Ingrese el nombre de la cuenta (no ingrese nada para cancelar):\n")
        #comprobamos si existe el jugador
        jugador, encontrado = obtener_jugador(jugadores, nombre)
        
        if not encontrado:
            os.system('cls')
            contraseña = input("Ingrese la contraseña de la cuenta:\n")
            nuevo_jugador = {
            "nombre": nombre,
            "contraseña": contraseña,
            "aciertos": 0,
            "errores": 0,
            "tiempo_total": 0.0,
            "partidas": 0,
            "mejor_puntos": 0,
            "mejor_tiempo": 0.0,
            "mejor_dificultad": "",
            "mejor_categoria": ""
            }
            jugadores.append(nuevo_jugador)
            return jugadores,nuevo_jugador
        else:
            print("Ese nombre ya existe, prueba con otro")

def cargar_jugadores(jugadores):
    try:
        with open("datos/jugadores.json", "w", encoding="utf-8") as f:
            json.dump(jugadores, f, indent=4, ensure_ascii=False)
    except Exception:
        print("algo fallo al leer el archivo")

def obtener_jugadores():
    try:
        with open("datos/jugadores.json", "r", encoding="utf-8") as f:
            jugadores = json.load(f)
    except Exception:
        jugadores = []
        print("algo fallo al leer el archivo")
    return jugadores

def obtener_jugador(jugadores, nombre):
    encontrado = False
    jugador = None
    for jugador in jugadores:
        if jugador['nombre'] == nombre:
            encontrado = True
            break
    return jugador, encontrado

def sin_contraseña(jugador):
    retorno=False
    if jugador["contraseña"]=="":
        retorno = True
    return retorno

def obtener_informacion_jugador(nombre):
    jugadores = obtener_jugadores()
    jugador,encontrado = obtener_jugador(jugadores, nombre)
    total_intentos = jugador["aciertos"] + jugador["errores"]
    if total_intentos > 0:
        porcentaje_aciertos = calcular_porcentaje(jugador["aciertos"],total_intentos)
        porcentaje_errores = calcular_porcentaje(jugador["errores"],total_intentos)
    else:
        porcentaje_aciertos = porcentaje_errores = 0
    if jugador["partidas"] > 0:
        tiempo_promedio = jugador["tiempo_total"] / jugador["partidas"]
    else:
        tiempo_promedio = 0
    return jugador, porcentaje_aciertos, porcentaje_errores, tiempo_promedio

def cambiar_datos_jugador(jugadores,nombre,puntos,aciertos,rondas,tiempo_partida,categoria,dificultad):
    for jugador in jugadores:
        if jugador['nombre'] == nombre:
            jugador['aciertos']+=aciertos
            jugador['errores']+=rondas-aciertos
            jugador['tiempo_total']+=tiempo_partida
            jugador['partidas']+=1
            if jugador['mejor_puntos']<puntos:
                jugador['mejor_puntos']=puntos
                jugador['mejor_tiempo']=tiempo_partida
                jugador['mejor_dificultad']=dificultad
                jugador['mejor_categoria']=categoria
            break
    return jugadores

def guardar_datos(puntos,aciertos,rondas,tiempo_partida,nombre,categoria,dificultad):
    jugadores=obtener_jugadores()
    jugadores=cambiar_datos_jugador(jugadores,nombre,puntos,aciertos,rondas,tiempo_partida,categoria,dificultad)
    cargar_jugadores(jugadores)

def obtener_top():
    jugadores=obtener_jugadores()
    mejores=[]
    
    for jugador in jugadores:
        mejores_jugador={
            "nombre": jugador['nombre'],
            "mejor_puntos": jugador['mejor_puntos']
        }
        mejores.append(mejores_jugador)
    return mejores




