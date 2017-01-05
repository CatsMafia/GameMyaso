import pygame
from pygame import *
import sys
import CONST
import Player
import GameWorld

class Game():


	def start(self):
		pygame.init()
		self.pl = Player.Player([50,50],CONST.SIZE_HERO,CONST.HERO_IMAGE)
		self.gameWorld = GameWorld.GameWorld()
		self.window = pygame.display.set_mode(CONST.SIZE_WINDOW)
		self.left,self.right,self.up,self.down,self.fire = False,False,False,False,False		
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
					if e.key == K_LEFT:
						self.left = True
					if e.key == K_RIGHT:
						self.right = True
					if e.key == K_UP:
						self.up = True
					if e.key == K_DOWN:
						self.down = True
					if e.key == K_SPACE:
						self.fire = True
				elif e.type == KEYUP:
					if e.key == K_LEFT:
						self.left = False
					if e.key == K_RIGHT:
						self.right = False
					if e.key == K_UP:
						self.up = False
					if e.key == K_DOWN:
						self.down = False
					if e.key == K_SPACE:
						self.fire = False
		self.pl.update(self.left,self.right,self.up,self.down,self.fire,self.gameWorld,self.time)
		self.gameWorld.update()



def main():
	game = Game()
	game.start()

if __name__ == '__main__':
	main()


