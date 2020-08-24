import sys, time, random, math, pygame
from pygame.locals import *

pillar_height = 200

class PillarClass(pygame.sprite.Sprite):

    def __init__(self,screen):
        
        # 调用父类方法
        super().__init__()

        # 绘制背景
        self.image = pygame.Surface([100 ,pillar_height])
        pillar_color = 0, 0, 0
        self.image.fill(pillar_color)
        
        # 确定坐标
        self.pos_x = 0
        self.pos_y = screen.get_height() - self.image.get_height()
        self.p_width = self.image.get_width()
        self.p_height = self.image.get_height()
        
        self.rect = Rect(self.pos_x, self.pos_y, self.p_width, self.p_height)


    #X property
    def _getx(self): 
        return self.rect.x

    def _setx(self,value): 
        self.rect.x = value

    X = property(_getx,_setx)

    #Y property
    def _gety(self): 
        return self.rect.y

    def _sety(self,value): 
        self.rect.y = value
    Y = property(_gety,_sety)

    #position property
    def _getpos(self): 
        return self.rect.topleft

    def _setpos(self,pos): 
        self.rect.topleft = pos

    position = property(_getpos,_setpos)

    #width property
    def _getwidth(self):
         return self.rect.width

    def _setwidth(self,value): 
        self.rect.width = value
    Width = property(_getwidth, _setwidth)

    def update(self,rect):
        self.rect = rect
        
        
        
   
        
