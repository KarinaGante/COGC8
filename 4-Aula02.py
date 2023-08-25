import pygame

pygame.init()

largura = (640, 480)
janela = pygame.display.set_mode(largura)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    janela.fill((0, 0, 0))

    #pygame.draw.line(janela, (150, 0, 255), (100, 200), (500, 200), 5) #linha
    #pygame.draw.circle(janela, (150, 0, 255), (320, 240), 50) #circulo preenchido
    #pygame.draw.circle(janela, (150, 0, 255), (320, 240), 150, 5) #outline
    #pygame.draw.rect(janela, (150, 0, 255), (100, 100, 300, 300)) #quadrado/retangulo preenchido
    #pygame.draw.rect(janela, (150, 0, 255), (100, 100, 300, 300), 3) #quadrado/retangulo outline
    pygame.draw.polygon(janela, (150, 0, 255), ((50, 100), (400, 50), (160, 450), (90, 320)), 2)


    pygame.display.flip()