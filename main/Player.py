import pygame
from pygame import *
import CONST
import math
from GameWorld import GameObject
from GameWorld import Bullet

class Player(GameObject):
	
	def __init__(self,pos,size,image):
		super().__init__(pos,size,image)
		self.timer = 0
		self.speed  =CONST.SPEED_HERO

	def update(self,left,right,up,down,fire,gameWorld,time):
		self.timer += time

		if left:
			self.pos[0] -=self.speed
		if right:
			self.pos[0] +=self.speed
		if up:
			self.pos[1] -=self.speed
		if down:
			self.pos[1] +=self.speed
		if fire:
			self.fire(gameWorld)
			
	def fire(self,gameWorld):
		if self.timer > 250:
			b =Bullet(pos = self.pos,size = CONST.SIZE_BULLET,image = CONST.BULLET_IMAGE,direction = 0)
			gameWorld.bullets.append(b)
			self.timer = 0

