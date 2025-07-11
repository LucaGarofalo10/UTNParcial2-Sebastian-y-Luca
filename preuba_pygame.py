import pygame
import os
pygame.init()

def cambiar_dimenciones(personaje_img,factor_escala):
    personaje_img = pygame.transform.scale(personaje_img, (personaje_img.get_width()/factor_escala, personaje_img.get_height()/factor_escala))
    return personaje_img

def separar_pregunta(pregunta, caracteres):
    pregunta_partida=[]
    i=0
    while i < len(pregunta):
        parte = pregunta[i:i+caracteres]
        pregunta_partida.append(parte)
        i += caracteres
    return pregunta_partida

def mostrar_ronda(pregunta,respuestas):
    #separo la pregunta en partes para mostrarla con un salto de linea
    pregunta=separar_pregunta(pregunta,30)
    
    # Cargar imagen de fondo para obtener dimensiones
    bg_path = os.path.join('img', 'terreno.jpg')
    background = pygame.image.load(bg_path)
    WIDTH, HEIGHT = background.get_width(), background.get_height()

    # Configurar pantalla
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego Básico con Pygame")

    # Cargar imágenes
    personaje_img = pygame.image.load(os.path.join('img', 'personaje.png'))
    personaje_img = cambiar_dimenciones(personaje_img,3)

    # Creamos el texto
    fuente=pygame.font.SysFont("Arial",40)
    
    
    # Posiciones de árboles y personaje
    personaje_pos = (25, 300)

    # Bucle principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar fondo
        screen.blit(background, (0, 0))

        # Dibujar pregunta
        for i in range(0,len(pregunta)):
            texto=fuente.render(pregunta[i], False, (0,0,0),(11, 148, 0))
            screen.blit(texto,(25,(i+1)*45))
        
        # Dibujar respuestas
        # for i in range(0,len(respuestas)):
        #     texto=fuente.render(respuestas[i], False, (0,0,0),(11, 148, ))
        #     screen.blit(texto,(25,(i+1)*45))
        # Dibujar personaje
        screen.blit(personaje_img, personaje_pos)

        pygame.display.flip()

    pygame.quit()

mostrar_ronda("¿Qué planeta es conocido como el planeta rojo?",["Venus","Júpiter","Marte"])