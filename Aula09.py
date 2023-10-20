#quadrado pygame
import pygame
from pygame.locals import *

pygame.init()
largura, altura = 600, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("programa com pygame")

white = (255, 255, 255)
black = (0, 0, 0)
purple = (150, 0, 250)

running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    screen.fill((black))
    pygame.draw.rect(screen, purple, (300, 300, 100, 100))
    pygame.display.flip()
pygame.quit()