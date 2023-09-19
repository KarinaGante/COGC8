import pygame
import tkinter as tk
from tkinter import simpledialog
import numpy as np
import math

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 400, 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Transformação de Rotação com Matriz")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Função para desenhar um quadrado
def desenhar_quadrado(x, y, tamanho, angulo):
    quadrado = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
    pygame.draw.rect(quadrado, vermelho, (0, 0, tamanho, tamanho))
    quadrado_rotacionado = pygame.transform.rotate(quadrado, angulo)
    rect = quadrado_rotacionado.get_rect(center=(x, y))
    tela.blit(quadrado_rotacionado, rect.topleft)

# Matriz de rotação 2D (ângulo em radianos)
def matriz_rotacao(angulo):
    return np.array([[math.cos(angulo), -math.sin(angulo)],
                     [math.sin(angulo), math.cos(angulo)]])

# Coordenadas iniciais do quadrado
x_quadrado, y_quadrado = 200, 200
tamanho_quadrado = 50
angulo_rotacao = 0

# Função para obter o ângulo de rotação via tkinter
def obter_angulo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do tkinter

    angulo = simpledialog.askfloat("Rotação", "Digite o ângulo de rotação (em graus):")
    root.destroy()  # Fecha a janela do tkinter

    return math.radians(angulo)  # Converte de graus para radianos

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            # Obter o ângulo de rotação via tkinter
            angulo = obter_angulo()

            # Aplica a matriz de rotação às coordenadas do quadrado
            matriz = matriz_rotacao(angulo)
            coordenadas_quadrado = np.array([[x_quadrado, y_quadrado]]).T

            # Transladando as coordenadas para o centro do quadrado
            coordenadas_quadrado[0] -= x_quadrado
            coordenadas_quadrado[1] -= y_quadrado

            # Rotacionando as coordenadas
            novas_coordenadas = np.dot(matriz, coordenadas_quadrado)

            # Transladando as coordenadas de volta para a posição original
            novas_coordenadas[0] += x_quadrado
            novas_coordenadas[1] += y_quadrado

            x_quadrado, y_quadrado = novas_coordenadas[0, 0], novas_coordenadas[1, 0]
            angulo_rotacao = angulo

    # Limpa a tela
    tela.fill(branco)

    # Desenha o quadrado com a rotação
    desenhar_quadrado(x_quadrado, y_quadrado, tamanho_quadrado, math.degrees(angulo_rotacao))

    pygame.display.flip()

pygame.quit()
