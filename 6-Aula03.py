#translacao

import pygame
import sys

pygame.init()

janela = (800, 600)
tela = pygame.display.set_mode(janela)

pygame.display.set_caption("translacao") #titulo da janela

preto = (0, 0, 0)
roxo = (150, 0, 250)

raio = 50
circulo_x = 600 // 2 #divisao de numeros inteiros
circulo_y = 400

#velocidade de translacao
v_translacao = 0.8

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit(0)
    tela.fill(preto)

    pygame.draw.circle(tela, roxo, (circulo_x, circulo_y), raio) #desenho circulo

    #atualizar tela
    pygame.display.flip()

    #translacao
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        circulo_x -= v_translacao 

    if key[pygame.K_RIGHT]:
        circulo_x += v_translacao

    if key[pygame.K_UP]:
        circulo_y -= v_translacao

    if key[pygame.K_DOWN]:
        circulo_y += v_translacao

    #limitar a janela
    circulo_x = max(raio, min(800 - raio, circulo_x))
    circulo_y = max(raio, min(600 - raio, circulo_y))

    pygame.display.update()
