#associando tkinter com pygame

import pygame
import tkinter as tk 
from tkinter import ttk

pygame.init()

window_w = 400
window_h = 300

window = pygame.display.set_mode((window_w, window_h))

pygame.display.set_caption("Change window color")

red = 255
green = 255
blue = 255

#funcao p mudar o fundo da janela
def updateColor():
    global red, green, blue

    red = int (redEntry.get())
    green = int (greenEntry.get())
    blue = int (blueEntry.get())

    window.fill((red, green, blue))

    pygame.display.update() #atualiza o que ja esta instanciado

#GUI

guiWindow = tk.Tk()

guiWindow.title("RGB controls")

#frame/form e componentes de interface

form = tk.Frame(guiWindow)
form.pack(padx = 10, pady = 10) #padding do guiWindow ao form, valores em pixel

#definicao parametizada das cores RGB
redLbl = ttk.Label(form, text = "R") #label
redLbl.grid(row = 0, column = 0, padx = 5, pady = 5) #posicao label
redEntry = ttk.Entry(form) #entrada de dados
redEntry.grid(row = 0, column = 1, padx = 5, pady = 5)

greenLbl = ttk.Label(form, text = "G")
greenLbl.grid(row = 1, column = 0, padx = 5, pady = 5)
greenEntry = ttk.Entry(form)
greenEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

blueLbl = ttk.Label(form, text = "B")
blueLbl.grid(row = 2, column = 0, padx = 5, pady = 5)
blueEntry = ttk.Entry(form)
blueEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

updateBtn = ttk.Button(form, text = "Update", command = updateColor)
updateBtn.grid(row = 3, column = 1, padx = 5, pady = 10)

#loop principal
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
            guiWindow.destroy()
    #att GUI
    guiWindow.update()

#finalizar pygame
pygame.quit()