# escala

import pygame

pygame.init()

altura, largura = 900, 700
canvas = (altura, largura)

tela = pygame.display.set_mode(canvas)

pygame.display.set_caption("escala")  # titulo da janela

preto = (0, 0, 0)
roxo = (150, 0, 250)

r_largura = 100
r_altura = 50

r_X = largura // 2 - r_largura // 2
r_y = altura // 2 - r_altura // 2

angulo = 0  # angulo rotacao em graus

escala = 1  # fator de escala

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit(0)
    tela.fill(preto)

    r_largura = int(largura * escala)
    r_altura = int(altura * escala)

    pygame.draw.rect(tela, roxo, (r_X, r_y, r_largura, r_altura))

    pygame.display.flip()  # atualizar tela

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        escala += 1

    if key[pygame.K_DOWN]:
        escala -= 1

    # escala = max(0.1, escala) #limitar tamanho da escala

    pygame.display.update()
