#quadrado usando openGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

pygame.init()
windowSize = (500, 600)
screen = pygame.display.set_mode(windowSize, DOUBLEBUF | OPENGL)

white = (255, 255, 255)
black = (0, 0, 0)
purple = (150, 0, 250)

def quadrado():
    glBegin(GL_QUADS)
    glColor3fv(purple)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    quadrado()
    pygame.display.flip()
pygame.quit()