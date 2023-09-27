#translacao
#convertendo graus em rad
import pygame
import tkinter as tk
import numpy as np
from tkinter import simpledialog

pygame.init()

largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("CONVERSAAAAAAAAAAAAAAAAOOOOOOOOOOO")

white = (255, 255, 255) 
black = (0, 0, 0) 
purple = (150, 0, 250) 

def desenharQuadrado (x, y, tamanho):
    pygame.draw.rect(tela, purple, (x, y, tamanho, tamanho))

def matrizTranslacao(Dx, Dy):
    return np.array([[1, 0, Dx], [0, 1, Dy], [0, 0, 1]]) #defifinicao da matriz por colunas

#coordenadas iniciais do quadrado
xQuadrado, yQuadrado = 150, 150
tamanhoQuadrado = 50

#obter coordenadas de translacao do tkinter
def obterCoordenadas():
    root = tk.Tk() #inicializa o tkinter
    root.withdraw() #ocultar janela principal tkinter

    x = simpledialog.askinteger("translacao", "Digite a coordenada de X:")
    y = simpledialog.askinteger("translacao", "Digite a coordenada de Y:")

    return x, y

running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.quit:
            running = False

        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Dx, Dy = obterCoordenadas()

            matriz = matrizTranslacao(Dx, Dy) #aplicar matriz de translacao
            coordenadasQuadrado = np.array([[xQuadrado, yQuadrado, 1]]) .T #T maiusculo retorna a matriz transposta
            novasCoordenadas = np.dot(matriz, coordenadasQuadrado)
            
            xQuadrado = novasCoordenadas[0, 0]
            yQuadrado = novasCoordenadas[1, 0]

        tela.fill(black)
        desenharQuadrado(xQuadrado, yQuadrado, tamanhoQuadrado)
        pygame.display.flip()
    
pygame.quit()



