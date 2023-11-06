#projecao ortogonal com OpenGL
#framebuffer == memoria reservada para processamento de elementos graficos

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

largura = 800
altura = 600
screen = pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)

pygame.display.set_caption("Open GL PYTHON KARINA")

#projecao ortogonal
def ortogonal():
    glMatrixMode(GL_PROJECTION)     #glMatrix seleciona uma matriz de projecao de visualizacao de objetos    #glProjection define as propriedades da camera que visualiza o objeto
    glLoadIdentity() #matriz identidade repoe essencialmente a matriz no seu estado predefinido
    gluOrtho2D(0, 640, 0, 480) #definir uma matriz de projecao ortogonal com coordenadas normalizadas

running = False
ortogonal()

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    #limpar buffer para colocar valores pre definidos
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #gl_color_buffer_bit limpa o buffer de cores  #gl_depth_buffer_bit limpa o buffer de profundidade
    glMatrixMode(GL_MODELVIEW) #inicializar matriz de visualizacao
    glLoadIdentity()
    glPointSize(5) #definir pontos a serem desenhados
    glBegin(GL_POINTS) #inicializar os vertices
    glVertex2i(100, 50)
    glVertex2i(630, 450)
    glEnd()
    
    pygame.display.flip()
    pygame.time.wait(100) #pausa de 100s antes de fechar a aplicacao

pygame.quit()