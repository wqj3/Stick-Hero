
import pygame



class Music():
     #音效

     

    def __init__(self):

        self.stick_grow_sound = pygame.mixer.Sound("sound/stick_grow_loop.wav")
        self.background_sound = pygame.mixer.Sound("sound/bg_bamboo.wav")
        self.dead_sound = pygame.mixer.Sound("sound/dead.wav")
        self.fall_sound = pygame.mixer.Sound("sound/fall.wav")
        self.victory_sound = pygame.mixer.Sound("sound/victory.wav")