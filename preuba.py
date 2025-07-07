import os
import json

perfil="Jugador1"
def menu_perfiles(perfil):
    while True:
        os.system('cls')
        if perfil != "ninguno":
            print(f"Hola {perfil} ¿que queres hacer?\n")
        else:
            print(f"Bienvenido ¿quieres crearte una cuenta o seleccionar una?\n")
        print("1. Informacion")
        print("2. Cambiar cuenta")
        print("3. Crear cuenta")
        print("4. Salir")
        opcion = input()
        match opcion:
                case "1":
                    ver_informacion(perfil)
                case "2":
                    perfil = cambiar_cuenta(perfil)
                    pass
                case "3":
                    # crear_cuenta()
                    pass
                case "4":
                    break
                case _:
                    print("Opción inválida. Intenta de nuevo.")
                    os.system('pause')
    return perfil

def obtener_jugadores():
    with open("jugadores.json", "r", encoding="utf-8") as f:
        jugadores = json.load(f)
    return jugadores

def obtener_jugador(jugadores, perfil):
    retorno = None
    for jugador in jugadores:
        if jugador["nombre"] == perfil:
            retorno = jugador
    return retorno

def obtener_informacion_jugador(perfil):
    jugadores = obtener_jugadores()
    jugador = obtener_jugador(jugadores, perfil)
    total_intentos = jugador["aciertos"] + jugador["errores"]
    if total_intentos > 0:
        porcentaje_aciertos = (jugador["aciertos"] / total_intentos) * 100
        porcentaje_errores = (jugador["errores"] / total_intentos) * 100
    else:
        porcentaje_aciertos = porcentaje_errores = 0
    if jugador["partidas"] > 0:
        tiempo_promedio = jugador["tiempo_total"] / jugador["partidas"]
    else:
        tiempo_promedio = 0
    return jugador, porcentaje_aciertos, porcentaje_errores, tiempo_promedio

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

def mostrar_jugadores(perfil, i, jugador):
    print(f"{i}. {jugador['nombre']}")
    return False

def verificar_jugadores(perfil, i, jugador):
    if jugador['nombre']==perfil:
        return True

def mostrar_verificar_jugadores(perfil,jugadores,funcion):
    retorno = False
    for i, jugador in enumerate(jugadores, 1):
        if funcion(perfil, i, jugador):
            retorno = True
    return retorno

def ingresar_contraseña(jugadores, nombre):
    while True:
        jugador=obtener_jugador(jugadores, nombre)
        os.system('cls')
        print("Ingrese la contraseña")
        print("'exit' para cancelar")
        contraseña = input("\n")
        if contraseña=="exit":
            break
        if jugador["contraseña"]==contraseña:
            os.system('cls')
            perfil=nombre
            print(f"Bienvenido {perfil}")
            os.system('pause')
            break
        else:
            os.system('cls')
            print("Contraseña incorrecta")
            os.system('pause')

def ingresar_nombre(jugadores):
    os.system('cls')
    print("¿A que cuenta queres cambiar?\n")
    mostrar_verificar_jugadores(None,jugadores,mostrar_jugadores)
    print("'exit' para cancelar")
    nombre=input("\nIngrese el nombre de la cuenta:\n")
    return nombre

def cambiar_cuenta(perfil):
    while True:
        jugadores = obtener_jugadores()
        nombre=ingresar_nombre(jugadores)
        if nombre=="exit":
            break
        
        if mostrar_verificar_jugadores(nombre,jugadores,verificar_jugadores):
            ingresar_contraseña(jugadores, nombre)
            break
        else:
            print("Cuenta no encontrada, intente otra ves")
            os.system('pause')
    return perfil

# def crear_cuenta(perfil):

menu_perfiles(perfil)