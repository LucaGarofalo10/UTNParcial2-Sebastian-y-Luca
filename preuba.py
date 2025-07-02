import re

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
                "tiempo": int(pregunta[6]),
                "puntaje": int(pregunta[7])
            }
    return preguntas_ronda

print(preguntas_csv(0, 5))  # Test the function with example parameters