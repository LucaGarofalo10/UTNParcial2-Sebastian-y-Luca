import os
from outputs import *

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
                perfil = crear_cuenta(perfil)
            case "4":
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
                os.system('pause')
    return perfil

#Opcion 1
def ver_informacion(perfil):
    os.system('cls')
    if perfil=="ninguno":
        print("Parece ser que no estas en un perfi\ncrea o ingresa en uno para ver su informacion ;)\n")
    else:
        jugador, partidas, porcentaje_aciertos, porcentaje_errores, tiempo_promedio = obtener_informacion_jugador(perfil)
        print("\n|------------Datos del jugador------------|")
        print(f"Nombre: {jugador['nombre']}")
        print(f"Partidas: {partidas}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")
        print(f"Porcentaje de errores: {porcentaje_errores:.2f}%")
        print(f"Tiempo promedio: {tiempo_promedio:.2f}s")
        print("\n|--------------Mejor partida--------------|")
        print(f"Puntos: {jugador['mejor_puntos']}")
        print(f"Tiempo: {jugador['mejor_tiempo']:.2f}s")
        print(f"Dificultad: {jugador['mejor_dificultad']}")
        print(f"Categoría: {jugador['mejor_categoria']}")
    os.system('pause')

#Opcion 2
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

#Opcion 3
def crear_cuenta(perfil):
    jugadores,nuevo_jugador = agregar_usuario()
    if nuevo_jugador['nombre']=="":
        return perfil
    cargar_jugadores(jugadores)
    return nuevo_jugador['nombre']

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

def comprobar_sin_perfil(perfil):
    while True:
        os.system('cls')
        if perfil=="ninguno":
            print("Al parecer no tienes un perfil ¿que quieres hacer entonces?\n")
            print("1. Ingresar en un perfil")
            print("2. Crear un perfil")
            print("3. Salir (se perdera tu puntuacion)")
            opcion=input("\n")
            match opcion:
                case "1":
                    perfil = cambiar_cuenta(perfil)
                    break
                case "2":
                    perfil = crear_cuenta(perfil)
                    break
                case "3":
                    break
                case _:
                    print("Opción inválida. Intenta de nuevo.")
                    os.system('pause')
    return perfil

#-------------------outputs-------------------#
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

def mostrar_jugadores(jugadores):
    for i, jugador in enumerate(jugadores, 1):
        print(f"{i}. {jugador['nombre']}")

def mensaje_ingreso(nombre):
    os.system('cls')
    print(f"Bienvenido {nombre}")
    os.system('pause')
