import os
from outputs import *
from ta_te_ti import *


def adivina_numero():
    tutorial_adivina_numero()
    resultado = adivina_numero_recursivo(random.randint(1, 100), 1, 100, 0)
    if resultado:
        mensaje_resultado("X")
    else:
        mensaje_resultado("O")
    return resultado


def adivina_numero_recursivo(aleatorio, inicio, fin, iteracion):
    os.system("pause")
    if iteracion > 6:
        retorno = False
    else:
        numero = recibir_numero(inicio, fin)

        if numero == aleatorio:
            retorno = True
        else:
            if numero > aleatorio:
                fin = numero - 1
            else:
                inicio = numero + 1
            retorno = adivina_numero_recursivo(aleatorio, inicio, fin, iteracion + 1)
    return retorno


def recibir_numero(inicio, fin):
    while True:
        os.system("cls")
        numero = input(f"Adivina el numero del {inicio} al {fin}\n")
        if es_numero(numero):
            numero = int(numero)
            if numero >= inicio and numero <= fin:
                break
            else:
                print(f"Valor invalido, tiene que estar entre {inicio} y {fin}")
                os.system("pause")
        else:
            print("ingrese un numero")
            os.system("pause")

    return numero


def tutorial_adivina_numero():
    os.system("cls")
    print(
        "Parece que te has desviado del camino, pero si adivinas en que numero piensa este vagabundo te guiara de vuelta al camino"
    )
    print(
        "\nPero te va a ayudar, te va a dar 7 intentos, y si no acertas te dira si el numero es mayor o menor"
    )
    print("suerte ;)\n")
