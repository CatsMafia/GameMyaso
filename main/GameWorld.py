import CONST
import math as mathM
import pygame
from pygame import *

class GameObject():
	def __init__(self,posCoor,size,image):
		self.pos = [posCoor[0]+size[0]//2,posCoor[1]+size[1]//2]
		self.size = size
		self.imageCoor = posCoor
		self.image = Surface(size)
		if type(image) == type(""):
			self.image = image.load(imagePath)
		elif type(image) == type((0,0,0)):
			self.image.fill(image)
		else:
			self.image.fill((0,0,0))

	def draw(self,window):
		self.imageCoor = [self.pos[0]-self.size[0]//2,self.pos[1]-self.size[1]//2]
		window.blit(self.image,self.imageCoor)


class Enemie(GameObject):

	def __init__(self, pos,size, image,gw):
		super().__init__(pos,size,image)
		self.speed = CONST.SPEED_ENEMIE
		self.boxColRight = GameObject([pos[0]+CONST.SIZE_ENEMIE[0],pos[1]+CONST.SPEED_ENEMIE+5],[2,size[1]-2*CONST.SPEED_ENEMIE-10],None)
		self.boxColLeft = GameObject([pos[0]-2,pos[1]+CONST.SPEED_ENEMIE+5],[2,size[1]-2*CONST.SPEED_ENEMIE-10],None)
		self.boxColUp = GameObject([pos[0]+CONST.SPEED_ENEMIE,pos[1]+CONST.SPEED_ENEMIE],[CONST.SIZE_ENEMIE[0]-2*CONST.SPEED_ENEMIE,1],None)
		self.boxColDown = GameObject([pos[0]+CONST.SPEED_ENEMIE,pos[1]+CONST.SIZE_ENEMIE[1]-CONST.SPEED_ENEMIE],[CONST.SIZE_ENEMIE[0]-2*CONST.SPEED_ENEMIE,1],None)
		self.life = 20
		self.gameWorld = gw
		self.tag = "Enemie"

	def update(self,posPlayer):
		self.moveToPoint(posPlayer)

	def moveToPoint(self,point):
		self.direction = (mathM.copysign(mathM.pi/2,point[1]-self.pos[1]) if (point[0]-self.pos[0])== 0 else mathM.atan((point[1]-self.pos[1])/(point[0]-self.pos[0])))+mathM.pi*int(point[0]<self.pos[0])
		if mathM.cos(self.direction) >= 0:
			if not self.gameWorld.collide(self.boxColRight)[0]:
				self.pos[0] += self.speed*mathM.cos(self.direction)
				self.boxColDown.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColDown.imageCoor[0]+=self.speed*mathM.cos(self.direction)
				self.boxColUp.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColUp.imageCoor[0]+=self.speed*mathM.cos(self.direction)
				self.boxColLeft.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColLeft.imageCoor[0]+=self.speed*mathM.cos(self.direction)
				self.boxColRight.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColRight.imageCoor[0]+=self.speed*mathM.cos(self.direction)
		if mathM.cos(self.direction) < 0:
			if not self.gameWorld.collide(self.boxColLeft)[0]:
				self.pos[0] += self.speed*mathM.cos(self.direction)
				self.boxColDown.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColDown.imageCoor[0]+=self.speed*mathM.cos(self.direction)
				self.boxColUp.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColUp.imageCoor[0]+=self.speed*mathM.cos(self.direction)
				self.boxColLeft.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColLeft.imageCoor[0]+=self.speed*mathM.cos(self.direction)
				self.boxColRight.pos[0]+=self.speed*mathM.cos(self.direction)
				self.boxColRight.imageCoor[0]+=self.speed*mathM.cos(self.direction)
		if mathM.sin(self.direction) >=0:
			if not self.gameWorld.collide(self.boxColDown)[0]:
				self.pos[1] += self.speed*mathM.sin(self.direction)
				self.boxColDown.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColDown.imageCoor[1]+=self.speed*mathM.sin(self.direction)
				self.boxColUp.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColUp.imageCoor[1]+=self.speed*mathM.sin(self.direction)
				self.boxColLeft.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColLeft.imageCoor[1]+=self.speed*mathM.sin(self.direction)
				self.boxColRight.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColRight.imageCoor[1]+=self.speed*mathM.sin(self.direction)
		if mathM.sin(self.direction) <0:
			if not self.gameWorld.collide(self.boxColUp)[0]:
				self.pos[1] += self.speed*mathM.sin(self.direction)
				self.boxColDown.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColDown.imageCoor[1]+=self.speed*mathM.sin(self.direction)
				self.boxColUp.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColUp.imageCoor[1]+=self.speed*mathM.sin(self.direction)
				self.boxColLeft.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColLeft.imageCoor[1]+=self.speed*mathM.sin(self.direction)
				self.boxColRight.pos[1]+=self.speed*mathM.sin(self.direction)
				self.boxColRight.imageCoor[1]+=self.speed*mathM.sin(self.direction)


class Block(GameObject):
	
	def __init__(self,pos,size,imagePath):
		super().__init__(pos,size,imagePath)
		self.life = 5
		self.tag = "Block"

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

	def __init__(self,pl):
		mapt = open('source/maps/map.mpt','r').read().split('\n')
		self.bullets = list()
		self.map = self.convert(mapt)
		self.player = pl
		self.enemies = list()
		enemie = Enemie([100,100],CONST.SIZE_ENEMIE,CONST.ENEMIE_IMAGE,self)
		self.enemies.append(enemie)

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
						if obj.tag == 'Block':
							self.map.remove(obj)
						elif obj.tag == 'Enemie':
							self.enemies.remove(obj)
				if i in self.bullets:
					self.bullets.remove(i)
		for i in self.enemies:
			i.update(self.player.pos)

	def draw(self,window):
		image = Surface(CONST.SIZE_WINDOW)
		image.fill(Color('#666666'))
		window.blit(image,(0,0))
		for i in self.map+self.bullets + self.enemies:
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
		for i in self.enemies:
			if self.checkColWith(i,obj):
				collides.append(i)
		return collides != [],collides

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