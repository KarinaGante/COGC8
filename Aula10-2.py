#ceu estreladoooooooooooooo
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

largura = 800
altura = 600
screen = pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)

pygame.display.set_caption("STAR WARS")

def ortogonal():
    glMatrixMode(GL_PROJECTION)     
    glLoadIdentity() 
    gluOrtho2D(0, 800, 0, 600)

running = False
ortogonal()

def drawStars(x, y, tamanho): #desenhar estrelas parametrizada
    glPointSize(tamanho)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity()
    drawStars(231, 151, 20)
    drawStars(150, 235, 10)
    drawStars(85, 480, 10)
    drawStars(25, 55, 15)
    drawStars(180, 555, 20) 
    drawStars(550, 25, 12)
    drawStars(630, 120, 9)      
    drawStars(-231, 151, 15) 
    pygame.display.flip()

pygame.quit()