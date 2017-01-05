import pygame
from pygame import *
import CONST
import math
from GameWorld import GameObject
from GameWorld import Bullet

class Player(GameObject):
	
	def __init__(self,pos,size,image):
		super().__init__(pos,size,image)
		print('coor = ',self.imageCoor,' pos = ',self.pos)
		self.timer = 0
		self.speed  =CONST.SPEED_HERO

	def update(self,left,right,up,down,fire,gameWorld,time):
		self.timer += time

		isCol,colls = gameWorld.collide(self)
		if left:
			if isCol:
				for i in colls:
					if i.imageCoor[0] < self.imageCoor[0] and i.imageCoor[0]+i.size[0] > self.imageCoor[0]:
						print('asdsad')
						break
				else:
					self.pos[0] -=self.speed
			else:
				self.pos[0] -=self.speed

		if right:
			if isCol:
				for i in colls:
					if i.imageCoor[0] > self.imageCoor[0] and i.imageCoor[0] <= self.imageCoor[0]+self.size[0]:
						break
				else:
					self.pos[0] +=self.speed
			else:
				self.pos[0] +=self.speed				
		if up:
			if isCol:
				for i in colls:
					if i.imageCoor[1] < self.imageCoor[1] and i.imageCoor[1]+i.size[1] > self.imageCoor[1]:
						print('asdsad')
						break
				else:
					self.pos[1] -=self.speed
			else:
				self.pos[1] -=self.speed

		if down:
			if isCol:
				for i in colls:
					if i.imageCoor[1] >= self.imageCoor[1] and i.imageCoor[1] <= self.imageCoor[1]+self.size[1]:
						break
				else:
					self.pos[1] +=self.speed
			else:
				self.pos[1] +=self.speed
		if fire:
			self.fire(gameWorld)
			
	def fire(self,gameWorld):
		if self.timer > 250:
			b =Bullet(self.pos,CONST.SIZE_BULLET,CONST.BULLET_IMAGE,0)
			print('coor = ',self.imageCoor,' pos = ',self.pos)
			gameWorld.bullets.append(b)
			self.timer = 0

