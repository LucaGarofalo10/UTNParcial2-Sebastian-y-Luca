def mayor_mejor_puntos(jugador1,jugador2):
    retorno =False
    if jugador1['mejor_puntos'] > jugador2['mejor_puntos']:
        retorno = True
    return retorno

def normal(i,j):
    retorno =False
    if i > j:
        retorno = True
    return retorno

def ordenar_lista_burbujeo(lista,comprobacion):
    for i in range(0,len(lista)):
        for j in range(i+1,len(lista)):
            if comprobacion(lista[i],lista[j]):
                aux=lista[j]
                lista[j]=lista[i]
                lista[i]=aux
    return lista

lista=[2,3,5,12,3,5,4,3,5,47,645,2,453]
print(ordenar_lista_burbujeo(lista,normal))
