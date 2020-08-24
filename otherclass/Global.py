
from enum import Enum

class Status(Enum):
    START = 0                       # 开始
    GROW_STICK = 1                  # 绘制棍子
    KICK = 2                        # 踢棍子
    STICK_TRANSFORM = 3              # 棍子旋转
    WALK = 4                        # 走
    SLIDE = 5                       # 移动完成，开始移除柱子
    SLIDE_NEW_RIGHT_PILLAR = 6       # 滑入新柱子
    FALL = 7                        # 掉落
    GAME_OVER = 8
   

    