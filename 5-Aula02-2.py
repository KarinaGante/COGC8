import pygame
import tkinter as tk

from tkinter import simpledialog

pygame.init()

largura = (640, 480)
root = tk.Tk()
root.withdraw() #esconde a  janela principal
janela = pygame.display.set_mode(largura)

#coordenadas do quadrado
x1 = simpledialog.askinteger("Coordenada para x1", f"Digite uma coordenada para o x superior")
x2 = simpledialog.askinteger("Coordenada para x2", f"Digite uma coordenada para o x inferior")
y1 = simpledialog.askinteger("Coordenada para y1", f"Digite uma coordenada para o y superior")
y2 = simpledialog.askinteger("Coordenada para y2", f"Digite uma coordenada para o y inferior")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    janela.fill((0, 0, 0))

    pygame.draw.rect(janela, (150, 0, 255), (x1, y1, x2, y2), 2) #outline

    pygame.display.flip()