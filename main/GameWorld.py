import CONST
import math as mathM
import pygame
from pygame import *


class GameObject():

	def __init__(self,pos,size,imagePath):
		self.pos = [mathM.fabs((pos[0]+size[0])/2),mathM.fabs((pos[1]+size[1])/2)]
		self.size = size
		self.imageCoor = pos
		self.image = Surface(size)
		self.image = image.load(imagePath)

	def draw(self,window):
		self.imageCoor = [mathM.fabs(self.pos[0]*2-self.size[0]),mathM.fabs(self.pos[1]*2-self.size[1])]
		window.blit(self.image,self.imageCoor)



class Block(GameObject):
	
	def __init__(self,pos,size,imagePath):
		super().__init__(pos,size,imagePath)
		self.life = 5

class Bullet(GameObject):
	def __init__(self,pos,size,image,direction):
		posCoor = [mathM.fabs(pos[0]*2-size[0]),mathM.fabs(pos[1]*2-size[1])]
		super().__init__(posCoor,size,image)
		self.direction = direction
		self.speed = CONST.SPEED_BULLET
		self.tick = 0


	def update(self):
		self.pos[0] += self.speed if mathM.tan(self.direction) == 0 else self.speed /mathM.tan(self.direction)
		self.pos[1] += self.speed * mathM.tan(self.direction)
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
				self.bullets.remove(i)
			isCol, obj = self.collide(i)
			if isCol:
				obj.life -=1
				if obj.life <= 0:
					self.map.remove(obj)
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

		res.sort(key = lambda x: x.pos[1])
		return res



	def collide(self,obj):
		for i in self.map:
			if self.checkColWith(i,obj):
				return True,i
		return False,None

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