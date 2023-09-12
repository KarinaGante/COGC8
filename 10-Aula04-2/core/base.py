import pygame
import sys
from core.input import Input

class Base(object):

	def __init__(self):
		pygame.init()
		screenSize = (640, 480)		
		displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

		self.screen = pygame.display.set_mode(screenSize, displayFlags)
		pygame.display.set_caption("janela grafica")

		self.running = True
		self.clock = pygame.time.Clock()
		self.input = Input()

	def initialize(self):
		pass

	def update(self):
		pass

	def run(self):
		self.initialize()

		while self.running:
			self.input.update()

			if self.input.quit:
				self.running = False

			self.update()

			pygame.display.flip()
			self.clock.tick(60)

		pygame.quit()
		pygame.exit(0)