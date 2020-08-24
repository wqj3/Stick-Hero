from random import randint
from otherclass.Pillar import *
from otherclass.Stick import *
from otherclass.Hero import *
from otherclass.Global import *


# 屏幕宽度
screen_width = 360
# 屏幕高度
screen_height = 660

# 新生成柱子宽度随机值范围
right_pialler_width_min = 20
right_pialler_width_max = 100

# 柱子最低间距
pillar_spacing_min = 10

class Tool():

    # 绘制右侧柱子，返回柱子的X坐标
    @classmethod
    def drawRandomPillar(self, leftPillar, rightPillar):

        # 右边新生成柱子随机宽度规则：
        # 最短20，最长100，从right_pialler_min ~ right_pialler_max之间选随机宽度

        # 随机宽度
        random_width = randint(right_pialler_width_min, right_pialler_width_max)
    
        # 右边柱子的X坐标规则：
        # 距离左边柱子最少10 (pillar_spacing_min) 个像素
        # 左边距离左侧柱子最少差 pillar_spacing_min 个像素 + leftPillar.p_width

        # 左侧范围
        left_pillar_x_min = pillar_spacing_min + leftPillar.Width + leftPillar.X

        # 不能出右边的屏幕，screen_width  - random_width(随机宽度)
        right_pillar_x_max = screen_width  - random_width

        # 右侧柱子随机坐标
        right_pillar_x =  randint(left_pillar_x_min , right_pillar_x_max)

        # 重新定义右侧柱子的整体位置

        rightPillar.image = pygame.Surface([random_width ,rightPillar.p_height])
        pillar_color = 0,0,0
        rightPillar.image.fill(pillar_color)


        rightPillar.Width = random_width

        return right_pillar_x



    @classmethod
    def calculationWalkDistance(self, stick, hero, leftPillar, rightPillar):

        #棍子长度
        stick_lengh = stick.Height

        #棍子最短距离
        stick_rightPillar_distance_min = rightPillar.X - (leftPillar.X + leftPillar.Width)

        #棍子最长距离
        stick_rightPillar_distance_max = rightPillar.X + rightPillar.Width - (leftPillar.X + leftPillar.Width)

        if stick_lengh < stick_rightPillar_distance_min :

            return False , stick_lengh

        elif  stick_lengh > stick_rightPillar_distance_max :

            return False , stick_lengh

        else :
            
            return True ,  rightPillar.X +  rightPillar.Width - hero.X - hero.Width - hero_interval_stick