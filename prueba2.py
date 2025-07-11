import random
import os
from datos import es_numero
from outputs import mensaje_resultado


def recivir_numero(inicio,fin):
    while True:
        os.system('cls')
        numero=input(f"Adivina el numero del {inicio} al {fin}\n")
        if es_numero(numero):
            numero=int(numero)
            if numero>=inicio and numero<=fin:
                break
            else:
                print(f"Valor invalido, tiene que estar entre {inicio} y {fin}")
                os.system('pause')
        else:
            print("ingrese un numero")
            os.system('pause')
    
    return numero

def adivina_numero_recursivo(aleatorio,inicio,fin,iteracion):
    print(aleatorio)
    os.system('pause')
    if iteracion>5:
        retorno=False
    else:
        numero=recivir_numero(inicio,fin)
        
        if numero==aleatorio:
            retorno=True
        else:
            if numero>aleatorio:
                fin=numero-1
            else:
                inicio=numero+1
            retorno=adivina_numero_recursivo(aleatorio,inicio,fin,iteracion+1)
    return retorno

def tutorial_adivina_numero():
    os.system('cls')
    print("Parece que te has desviado del camino, pero si adivinas en que numero piensa este vagabundo te guiara de vuelta al camino")
    print("\nPero te va a ayudar, te va a dar 6 intentos, y si no acertas te dira si el numero es mayor o menor")
    print("suerte ;)\n")

def adivina_numero():
    tutorial_adivina_numero()
    if adivina_numero_recursivo(random.randint(1, 100),1,100,0):
        mensaje_resultado("X")
    else:
        mensaje_resultado("O")

adivina_numero()