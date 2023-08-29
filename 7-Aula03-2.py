# rotacao

import pygame
import sys
import math

pygame.init()

altura, largura = 800, 600
canvas = (altura, largura)

tela = pygame.display.set_mode(canvas)

pygame.display.set_caption("rotacao")  # titulo da janela

preto = (0, 0, 0)
roxo = (150, 0, 250)

r_largura = 100
r_altura = 150

r_X = largura // 2 - r_largura // 2
r_y = altura // 2 - r_altura // 2

# angulo rotacao em graus
angulo = 0

# velocidade rotacao
v_rotacao = -1

# funcao p desenhar retangulo rotacionado


def retanguloRotate(tela, cor, x, y, largura, altura, angulo):
    retRotate = pygame.Surface((altura, largura), pygame.SRCALPHA)
    retRotate.fill(preto)
    pygame.draw.rect(retRotate, cor, (0, 0, largura, altura))
    rotacao = pygame.transform.rotate(retRotate, angulo)
    newRet = rotacao.get_rect(center=(x, y))
    tela.blit(rotacao, newRet.topleft)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit(0)
    tela.fill(preto)
    retanguloRotate(tela, roxo, r_X, r_y, r_largura,
                    r_altura, angulo)  # desenhar reatngulo
    pygame.display.flip()  # atualizar tela

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        angulo -= v_rotacao

    if key[pygame.K_RIGHT]:
        angulo += v_rotacao

    pygame.display.update()
