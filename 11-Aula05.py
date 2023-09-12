# clipping
# implementando o algoritmo de cohen-suthertland

import pygame
import sys

white = (255, 255, 255)  # bg
black = (0, 0, 0)  # retas
purple = (150, 0, 250)  # window

# codigos de cohen-sutherland
dentro = 0
esquerda = 1
direita = 2
base = 4
topo = 8

# coordenadas janela de recorte
Xmin, Ymin, Xmax, Ymax = 100, 100, 400, 400

# funcao para calcular o codigo e verificar se
# um ponto esta dentro ou fora da minha view


def calcularRC(x, y):
    codigo = dentro

    if x < Xmin:
        codigo |= esquerda
    elif x > Xmax:
        codigo |= direita

    if y < Ymin:
        codigo |= base
    elif y > Ymax:
        codigo |= topo

    return codigo

# funcao para aplicar o algoritmo (flag)


def cohenSutherland(x1, x2, y1, y2):
    clipCode1 = calcularRC(x1, y1)
    clipCode2 = calcularRC(x2, y2)

    aceito = False

    while True:
        if not (clipCode1 | clipCode2):  # pontos dentro da janela
            aceito = True
            break
        else:
            x = 0
            y = 0

            outClipCode = clipCode1 if clipCode1 else clipCode2
            # se clipcode1 for verdade, mantem, senao, atrubui clipcode2

            if outClipCode and topo:
                coefMax = (Ymax - y1) / (y2 - y1)  # coeficiente
                coefMin = (Ymin - y1) / (y2 - y1)
                coefRig = (Xmax - x1) / (x2 - x1)
                coefLef = (Xmin - x1) / (x2 - x1)

                x = x1 + (x2 - x1) * coefMax
                y = Ymax

            elif outClipCode and base:
                x = x1 + (x2 - x1) * coefMin
                y = Ymin

            elif outClipCode and direita:
                y = y1 + (y2 - y1) * coefRig
                x = Xmax

            elif outClipCode and esquerda:
                y = y1 + (y2 - y1) * coefLef
                x = Xmin

            if outClipCode == clipCode1:
                x1, y1 = x, y

                clipCode1 = calcularRC(x1, y1)

            else:
                x2, y2 = x, y
                clipCode2 = calcularRC(x2, y2)

        if aceito:
            return int(x1), int(x2), int(y1), int(y2)


pygame.init()
window = (800, 600)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Algoritmo FODA")

# lista de segmentos de reta
lines = []

running = True
draw = False

currentLine = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mouse event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if draw:
                    currentLine.append(event)
                else:
                    currentLine = [event.pos]  # release mouse button
                    draw = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and draw:
                    currentLine.append(event.pos)  # novo elemento na lista
                    lines.append(currentLine)
                    currentLine = []
                    draw = False

    screen.fill(black)
    pygame.draw.rect(screen, purple, (Xmin, Ymin, Xmax, Ymax), 2)

    # desenhando linhas
    for linha in lines:
        clippedLine = cohenSutherland(
            linha[0][0], linha[0][1], linha[1][0], linha[1][1])

        if clippedLine:
            pygame.draw.line(
                screen, white, clippedLine[0:2], clippedLine[2:4], 2)

        if draw:
            pygame.draw.line(
                screen, white, currentLine[0], pygame.mouse.get_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()
