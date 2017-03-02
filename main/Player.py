import pygame
from pygame import *
import CONST
import math
from GameWorld import GameObject
from GameWorld import Bullet

class Player(GameObject):

	
	def __init__(self,pos,size,image):
		super().__init__(pos,size,image)
		self.boxColRight = GameObject([pos[0]+CONST.SIZE_HERO[0],pos[1]+CONST.SPEED_HERO+5],[2,size[1]-2*CONST.SPEED_HERO-10],None)
		self.boxColLeft = GameObject([pos[0]-2,pos[1]+CONST.SPEED_HERO+5],[2,size[1]-2*CONST.SPEED_HERO-10],None)
		self.boxColUp = GameObject([pos[0]+CONST.SPEED_HERO,pos[1]+CONST.SPEED_HERO],[CONST.SIZE_HERO[0]-2*CONST.SPEED_HERO,1],None)
		self.boxColDown = GameObject([pos[0]+CONST.SPEED_HERO,pos[1]+CONST.SIZE_HERO[1]-CONST.SPEED_HERO],[CONST.SIZE_HERO[0]-2*CONST.SPEED_HERO,1],None)
		self.timer = 0
		self.speed  =CONST.SPEED_HERO
		self.direction = 0


	def update(self,left,right,up,down,fire,coorFire,gameWorld,time):
		self.timer += time
		
		if left:
			if not gameWorld.collide(self.boxColLeft)[0]:
				self.move(-CONST.SPEED_HERO,0)
		if right:
			if not gameWorld.collide(self.boxColRight)[0]:
				self.move(CONST.SPEED_HERO,0)
		
		if 	up:
			if not gameWorld.collide(self.boxColUp)[0]:
				self.move(0,-CONST.SPEED_HERO)
		
		if down:
			if not gameWorld.collide(self.boxColDown)[0]:
				self.move(0,CONST.SPEED_HERO)

		if fire:
			if coorFire == 0:
				self.direction = 0
			else:
				self.direction = (math.copysign(math.pi/2,coorFire[1]-self.pos[1]) if (coorFire[0]-self.pos[0])== 0 else math.atan((coorFire[1]-self.pos[1])/(coorFire[0]-self.pos[0])))+math.pi*int(coorFire[0]<self.pos[0])
			self.fire(gameWorld,self.direction)
	
	def move(self,moveDX = 0,moveDY = 0):
		self.pos[0]+=moveDX
		self.boxColDown.pos[0]+=moveDX
		self.boxColDown.imageCoor[0]+=moveDX
		self.boxColUp.pos[0]+=moveDX
		self.boxColUp.imageCoor[0]+=moveDX
		self.boxColLeft.pos[0]+=moveDX
		self.boxColLeft.imageCoor[0]+=moveDX
		self.boxColRight.pos[0]+=moveDX
		self.boxColRight.imageCoor[0]+=moveDX
		self.pos[1]+=moveDY
		self.boxColDown.pos[1]+=moveDY
		self.boxColDown.imageCoor[1]+=moveDY
		self.boxColUp.pos[1]+=moveDY
		self.boxColUp.imageCoor[1]+=moveDY
		self.boxColLeft.pos[1]+=moveDY
		self.boxColLeft.imageCoor[1]+=moveDY
		self.boxColRight.pos[1]+=moveDY
		self.boxColRight.imageCoor[1]+=moveDY
		

	def fire(self,gameWorld,direction):
		if self.timer > CONST.SPEED_FIRE:
			b =Bullet(self.pos,CONST.SIZE_BULLET,CONST.BULLET_IMAGE,self.direction)
			gameWorld.bullets.append(b)
			self.timer = 0

