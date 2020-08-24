import sys, time, random, math, pygame

from pygame.locals import *

from otherclass.Pillar import *

stick_width = 2
stick_height = 1


class StickClass(pygame.sprite.Sprite):

    def __init__(self, pillar):

        super().__init__()

        self.image = pygame.Surface([stick_width, stick_height])
        stick_color = 0,0,0
        self.image.fill(stick_color)
        self.rect = Rect(pillar.Width + pillar.X - stick_width, pillar.Y, stick_width, stick_height)
        self.angle = 0
        self.mousedown = False

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

     #height property
    def _getheight(self):
         return self.rect.height

    def _setheight(self,value): 
        self.rect.height = value
    Height = property(_getheight, _setheight) 

