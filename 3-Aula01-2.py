# ALTERANDO COR DO CANVAS COM PYGAME

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Hello world!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill((125, 168, 220))
        pygame.display.flip()
