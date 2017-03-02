import pygame
from pygame import *
import sys
import CONST
import Player
import GameWorld

class Game():


	def start(self):
		pygame.init()
		self.pl = Player.Player([128,128],CONST.SIZE_HERO,CONST.HERO_IMAGE)
		self.gameWorld = GameWorld.GameWorld(self.pl)
		self.window = pygame.display.set_mode(CONST.SIZE_WINDOW)
		self.left,self.right,self.up,self.down,self.fire,self.direction = False,False,False,False,False,0
		pygame.display.set_caption('MyasoRubka')
		self.timer = pygame.time.Clock()
		while 1 :
			self.time = self.timer.tick(60)
			self.updateEvent()
			self.updateScreen()


	def updateScreen(self):
		self.gameWorld.draw(self.window)
		self.pl.draw(self.window)

		pygame.display.update()

	def updateEvent(self):
		for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)
				elif e.type == KEYDOWN:
					if e.key == K_LEFT or e.key == K_a:
						self.left = True
					if e.key == K_RIGHT or e.key == K_d:
						self.right = True
					if e.key == K_UP or e.key == K_w:
						self.up = True
					if e.key == K_DOWN or e.key == K_s:
						self.down = True
					if e.key == K_q:
						sys.exit(0)
				elif e.type == KEYUP:
					if e.key == K_LEFT or e.key == K_a:
						self.left = False
					if e.key == K_RIGHT or e.key == K_d:
						self.right = False
					if e.key == K_UP or e.key == K_w:
						self.up = False
					if e.key == K_DOWN or e.key == K_s:
						self.down = False
				elif e.type == MOUSEBUTTONDOWN:
					if e.button == 1:
						self.fire = True
				elif e.type == MOUSEBUTTONUP:
					if e.button == 1:
						self.fire = False
						self.direction = 0
		if self.fire:
			self.direction = pygame.mouse.get_pos()
		self.pl.update(self.left,self.right,self.up,self.down,self.fire,self.direction,self.gameWorld,self.time)
		self.gameWorld.update()
		


def main():
	game = Game()
	game.start()

if __name__ == '__main__':
	main()


