preguntas = [1,2,3,4,5,6,7,8,9,10]
vueltas = 0

while vueltas < len(preguntas):
    vueltas = 0
    print("while")
    pregunta_actual = 51
    
    for pregunta in preguntas:
        print(pregunta)
        if pregunta_actual == pregunta:
            print("igual")
            break  # salimos del for si encontramos la pregunta
        vueltas += 1
    
    print("a")
    if vueltas > len(preguntas):
        print("dentro del if")
        print(pregunta_actual)
        print(vueltas)
