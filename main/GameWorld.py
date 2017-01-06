import CONST
import math as mathM
import pygame
from pygame import *


class GameObject():

	def __init__(self,posCoor,size,imagePath):
		self.pos = [posCoor[0]+size[0]//2,posCoor[1]+size[1]//2]
		self.size = size
		self.imageCoor = posCoor
		self.image = Surface(size)
		if imagePath != None:
			self.image = image.load(imagePath)
		else:
			self.image.fill((0,0,0))

	def draw(self,window):
		self.imageCoor = [self.pos[0]-self.size[0]//2,self.pos[1]-self.size[1]//2]
		window.blit(self.image,self.imageCoor)



class Block(GameObject):
	
	def __init__(self,pos,size,imagePath):
		super().__init__(pos,size,imagePath)
		self.life = 5

class Bullet(GameObject):
	def __init__(self,pos,size,image,direction):
		posCoor = [pos[0]-size[0]//2,pos[1]-size[1]/2]
		super().__init__(posCoor,size,image)
		self.direction = direction
		self.speed = CONST.SPEED_BULLET
		self.tick = 0


	def update(self):
		self.pos[0] += self.speed*mathM.cos(self.direction)
		self.pos[1] += self.speed*mathM.sin(self.direction)
		self.tick +=1

class GameWorld():

	def __init__(self):
		mapt = open('source/maps/map.mpt','r').read().split('\n')
		self.bullets = list()
		self.map = self.convert(mapt)


	def update(self):
		for i in self.bullets:
			i.update()
			if i.tick >=30:
				if i in self.bullets:
					self.bullets.remove(i)
			isCol, objs = self.collide(i)
			if isCol:
				for obj in objs:
					obj.life -=1
					if obj.life <= 0:
						self.map.remove(obj)
				if i in self.bullets:
					self.bullets.remove(i)
	

	def draw(self,window):
		image = Surface(CONST.SIZE_WINDOW)
		image.fill(Color('#666666'))
		window.blit(image,(0,0))
		for i in self.map+self.bullets:
			i.draw(window)


	def convert(self,mapt):
		res = list()
		for i in range(len(mapt)):
			for j in range(len(mapt[i])):
				if mapt[i][j] == '#':
					b = Block([j*CONST.SIZE_BLOCK[0],i*CONST.SIZE_BLOCK[1]],CONST.SIZE_BLOCK,CONST.BLOCK_IMAGE)
					res.append(b)

		return res



	def collide(self,obj):
		collides = list()
		for i in self.map:
			if self.checkColWith(i,obj):
				collides.append(i)
		return collides != [],collides

	'''
	def checkColWithBlocks(self,obj):
		for i in self.map:
			if self.checkColWith(i,obj):
				return True,i
		return False,None				
	'''
	def checkColWith(self,obj1,obj2):
		if (obj1.imageCoor[0] + obj1.size[0] > obj2.imageCoor[0] + obj2.size[0] and obj2.imageCoor[0] + obj2.size[0]>obj1.imageCoor[0]) and (obj1.imageCoor[1] + obj1.size[1] > obj2.imageCoor[1] + obj2.size[1] and obj2.imageCoor[1] + obj2.size[1]>obj1.imageCoor[1]):
			return True
		elif (obj2.imageCoor[0] + obj2.size[0] > obj1.imageCoor[0] + obj1.size[0] and obj1.imageCoor[0] + obj1.size[0]>obj2.imageCoor[0]) and (obj1.imageCoor[1] + obj1.size[1] > obj2.imageCoor[1] + obj2.size[1] and obj2.imageCoor[1] + obj2.size[1]>obj1.imageCoor[1]):
			return True
		elif (obj1.imageCoor[0] + obj1.size[0] > obj2.imageCoor[0] + obj2.size[0] and obj2.imageCoor[0] + obj2.size[0]>obj1.imageCoor[0]) and (obj2.imageCoor[1] + obj2.size[1] > obj1.imageCoor[1] + obj1.size[1] and obj1.imageCoor[1] + obj1.size[1]>obj2.imageCoor[1]):
			return True
		elif (obj2.imageCoor[0] + obj2.size[0] > obj1.imageCoor[0] + obj1.size[0] and obj1.imageCoor[0] + obj1.size[0]>obj2.imageCoor[0]) and (obj2.imageCoor[1] + obj2.size[1] > obj1.imageCoor[1] + obj1.size[1] and obj1.imageCoor[1] + obj1.size[1]>obj2.imageCoor[1]):
			return True
		return False