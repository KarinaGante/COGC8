# rotacao
import pygame
import tkinter as tk
import numpy as np
import math
from tkinter import simpledialog

pygame.init()

largura, altura = 400, 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("ROOOOTTAAAAAATTTTIIIIOOOOOONNNNN")

white = (255, 255, 255)
black = (0, 0, 0)
purple = (150, 0, 250)


def desenharQuad(x, y, tamanho, angulo):
    quadrado = pygame.surface((tamanho, tamanho), pygame.SRCALPHA)
    pygame.draw.rect(quadrado, purple, (0, 0, tamanho, tamanho))
    quadradoRot = pygame.transform.rotate(quadrado, angulo)
    # determinar centro do retangulo
    rect = quadradoRot.get_rect(center=(x, y))
    # atualiza a mudança na estrutura do obj
    tela.blit(quadradoRot, rect.topleft)


def matrizRot(angulo):  # rad
    # matriz matematica e nao array
    return np.array([[math.cos(angulo), -math.sin(angulo)],
                     [math.sin(angulo), math.cos(angulo)]])


xQuad, yQuad = 200, 200
anguloRot = 0
tamanhoQuad = 150


def obterAngulo():
    root = tk.Tk()
    root.withdraw()  # oculta a janela root
    angulo = simpledialog.askfloat(
        "Rotation", "Digite o angulo da rotação em graus: ")
    root.destroy()  # fecha a janela tkinter
    return math.radians(angulo)


running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            angulo = obterAngulo()
            matriz = matrizRot(angulo)
            coordQuad = np.array([[xQuad, yQuad]]).T
            # transladando as coordenadas para o centro
            coordQuad[0] -= xQuad
            coordQuad[1] -= yQuad

            nCoord = np.dot(matriz, coordQuad)  # rotacionar coord

            nCoord[0] += xQuad  # transladar de volta a posicao
            nCoord[1] += yQuad

            xQuad, yQuad = nCoord[0, 0], nCoord[1, 0]
            anguloRot = angulo

    tela.fill(black)
    desenharQuad(xQuad, yQuad, tamanhoQuad, math.degrees(anguloRot))
    pygame.display.flip()  # att a tela

pygame.quit()
