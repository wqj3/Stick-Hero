import pygame

from pygame.locals import *

import otherclass.Pillar

image_width = 25
image_height = 27
hero_interval_stick = 3
walk_speed = 10
fall_speed = 50

class HeroClass(pygame.sprite.Sprite):

    
    def __init__(self, pillar):
        super().__init__()
        self.image = pygame.image.load("image/hero1/stay1.png")
        self.image.convert()
        #压缩图片
        self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))
        self.rect = Rect(pillar.X +  pillar.Width - image_width - hero_interval_stick, pillar.Y - image_height, image_width, image_height)
        self.status = 0
        self.walk_speed_image = 1

    
    def kick(self):
        
        self.image = pygame.image.load("image/hero1/kick4.png")
        self.image.convert()
        #压缩图片
        self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))

    def stay(self):
        pygame.time.wait(200)

        self.image = pygame.image.load("image/hero1/stay1.png")
        self.image.convert()
        #压缩图片
        self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))



    def walk(self, distance):

        # pygame.time.wait(10)

        #distance =  pillar.X +  pillar.Width - self.rect.x - image_width

        if distance < walk_speed:
            self.X += distance
        else:
            self.X += walk_speed

        if self.walk_speed_image % 5 == 1:
            self.image = pygame.image.load("image/hero1/walk1.png")
            self.image.convert()
            #压缩图片
            self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))

        elif self.walk_speed_image % 5 == 2:
            self.image = pygame.image.load("image/hero1/walk2.png")
            self.image.convert()
            #压缩图片
            self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))
            
        elif self.walk_speed_image % 5 == 3:
            self.image = pygame.image.load("image/hero1/walk3.png")
            self.image.convert()
            #压缩图片
            self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))
            
        elif  self.walk_speed_image % 5 == 4:
            self.image = pygame.image.load("image/hero1/walk4.png")
            self.image.convert()
            #压缩图片
            self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))

        elif  self.walk_speed_image % 5 == 0:
            self.image = pygame.image.load("image/hero1/walk5.png")
            self.image.convert()
            #压缩图片
            self.image = pygame.transform.smoothscale(self.image, (image_width, image_height))

            
        self.walk_speed_image += 1
    
    def fall(self):

        self.Y += fall_speed


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
