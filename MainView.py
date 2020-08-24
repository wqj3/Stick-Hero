import sys, time, random, math, pygame

from pygame.locals import *
from random import randint
from otherclass.Pillar import *
from otherclass.Stick import *
from otherclass.Hero import *
from otherclass.Global import *
from otherclass.Tool import *
from otherclass.Music import *


# 屏幕宽度
SCREEN_WIDTH = 360
# 屏幕高度
SCREEN_HEIGHT = 660
# 屏幕背景色
SCREEN_BG_COLOR = 255, 255, 255
# 背景图片
SCREEN_BG_IMAGE = 'image/bg/bg1.jpg'

# 帧率
FPS = 90

# 滑动速率
SLIDE_SPEED = 15

# 棍子增长高度
STICK_ADD_HEIGHT = 5

# 棍子旋转速率
STICK_TRANSFORM = 10

# 柱子初始宽高
STICK_WIDTH = 2
STICK_HEIGHT = 1

framerate = pygame.time.Clock()

#初始化界面
def initView():

    pygame.init()

    #设置标题
    pygame.display.set_caption('Stick Hero')

    # 屏幕大小
    window = (SCREEN_WIDTH,SCREEN_HEIGHT)
    # 初始化屏幕
    screen = pygame.display.set_mode(window)
    # 设置背景颜色
    white = SCREEN_BG_COLOR
    # 填充背景颜色
    screen.fill(white)
   
    pygame.display.flip()

    #绘制背景
    drawBackground(screen)

     # 更新视图
    pygame.display.update()

    return screen

# 绘制背景
def drawBackground(screen):
    # 加载图片
    bg = pygame.image.load(SCREEN_BG_IMAGE)
    bg.convert()
    #压缩图片
    bg = pygame.transform.smoothscale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #背景贴图
    screen.blit(bg, (0, 0,SCREEN_WIDTH,SCREEN_HEIGHT))


if __name__ == "__main__": 

    # 初始化游戏
    screen = initView()

    # pygame.display.flip()

    # 帧率
    framerate.tick(FPS)

    # 新柱子的X坐标
    right_pillar_new_x = 0

     # 初始状态
    game_status = Status.START

    # 分数
    score = 0
    # 文字
    text = pygame.font.SysFont("宋体", 50)
    text_fmt = text.render(str(score), 1, (0,0,0))

    # 创建柱子
    pillar_one = PillarClass(screen)
    pillar_two = PillarClass(screen)

    # 创建棍子
    stick = StickClass(pillar_one)

    # 创建英雄
    hero = HeroClass(pillar_one)

    #绘制柱子
    right_pillar_new_x = Tool.drawRandomPillar(pillar_one, pillar_two)

    screen.blit(pillar_one.image, pillar_one.rect)
    screen.blit(pillar_two.image, pillar_two.rect)
    screen.blit(stick.image, stick.rect)

    pygame.display.update()

    # 音乐
    music = Music()

    # 游戏循环
    while True:
        
        for event in pygame.event.get():

            #退出
            if event.type in (QUIT, KEYDOWN):
                sys.exit()

            #鼠标点击
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_status == Status.GROW_STICK:
                    stick.mousedown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if stick.mousedown:
                    stick.mousedown = False
                    game_status = Status.KICK

        if game_status == Status.START:
            game_status = Status.SLIDE_NEW_RIGHT_PILLAR

          #新柱子从屏幕右侧出现
        if game_status ==  Status.SLIDE_NEW_RIGHT_PILLAR:

            if (pillar_two.X - right_pillar_new_x > SLIDE_SPEED):
                pillar_two.X -= SLIDE_SPEED
            else:
                pillar_two.X -= pillar_two.X - right_pillar_new_x
                game_status = Status.GROW_STICK


        # 判断鼠标是否一直点击
        if stick.mousedown:

            stick.Height += STICK_ADD_HEIGHT
            stick.Y -= STICK_ADD_HEIGHT
            
            stick.image = pygame.Surface([stick.Width, stick.Height])
            pillar_color = 0, 0, 0
            stick.image.fill(pillar_color)

            music.stick_grow_sound.play()

        # 踢棍子
        if game_status == Status.KICK:
            hero.kick()
            game_status = Status.STICK_TRANSFORM

          
        # 旋转棍子
        if game_status == Status.STICK_TRANSFORM:

            stick.rect.center = (stick.rect.centerx, stick.rect.centery+stick.Height-stick.Width/2)
  
            stick.image = pygame.transform.rotate(stick.image, -90)

            music.fall_sound.play()

            game_status = Status.WALK

        # 沿着棍子走
        if game_status == Status.WALK :
            # 调用工具类判断棍子距离是否成功，并且返回要走的距离
            success, distance = Tool.calculationWalkDistance(stick, hero,  pillar_one, pillar_two)

            if success :
                
                hero.walk(distance)

                if distance == 0:

                    hero.walk_speed_image = 1

                    music.victory_sound.play()
                    #分数加1
                    score += 1

                    text = pygame.font.SysFont("宋体", 50)
                    text_fmt = text.render(str(score), 1, (0,0,0))

                    game_status = Status.SLIDE

            else:
                hero.walk(distance)

                if stick.Height + stick.X < hero.X :
                    game_status = Status.FALL
                
        # 掉落
        if game_status == Status.FALL:
            hero.fall()
            if hero.Y > SCREEN_HEIGHT :
                # 游戏结束
                game_status = Status.GAME_OVER
                music.dead_sound.play()
      
        #右侧柱子滑动到左侧边界
        if game_status == Status.SLIDE:
            # 棍子、左右柱子、英雄都要slide_speed速度按平移
            pillar_one.X -= SLIDE_SPEED
            pillar_two.X -= SLIDE_SPEED
            stick.X -= SLIDE_SPEED 
            hero.X -= SLIDE_SPEED

            # 如果棍子的坐标小于滑动速度
            if pillar_two.X < SLIDE_SPEED:
                # 例如：x的坐标为3，滑动速率为5，那么3%5余3，棍子x坐标向左平移3
                pillar_two.X -= pillar_two.X % SLIDE_SPEED
                # 英雄的坐标根据脚下的柱子确定
                hero.X = pillar_two.X +  pillar_two.Width - hero.Width - hero_interval_stick
                # 右侧柱子已滑到最左端，那么右侧柱子变为左侧，左侧柱子滑出屏幕变为右侧柱子
                # pillar_one 永远为左侧柱子，pillar_two永远为右侧柱子
                pillar_one, pillar_two = pillar_two, pillar_one
                # pillar_two为右侧柱子，那么从左侧滑出屏幕后，从屏幕右边重新进入屏幕
                pillar_two.X = SCREEN_WIDTH
                # 右侧进入屏幕的柱子，获取新的宽度和随机位置
                right_pillar_new_x = Tool.drawRandomPillar(pillar_one, pillar_two)

                # 重新绘制棍子颜色
                stick_color = 0,0,0,0
                stick.image = pygame.Surface([STICK_WIDTH, STICK_HEIGHT])
                stick.image.fill(stick_color)
                stick.rect = Rect(pillar_one.Width + pillar_one.X - STICK_WIDTH, pillar_one.Y, STICK_WIDTH, STICK_HEIGHT)
                
                # 改变游戏状态
                game_status = Status.SLIDE_NEW_RIGHT_PILLAR

        drawBackground(screen)

        screen.blit(pillar_one.image, pillar_one.rect)
        screen.blit(pillar_two.image, pillar_two.rect)
        screen.blit(stick.image, stick.rect)
        screen.blit(hero.image, hero.rect)
        screen.blit(text_fmt, (SCREEN_WIDTH/2, 100))

        #更新视图
        pygame.display.update()