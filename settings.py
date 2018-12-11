# -*- coding: utf-8 -*-
# @Time    : 2018/12/4
# @Author  : Yifei Duan
# @Summary :


class Settings:
    """a cleass to store settings for Alien Invasion."""

    def __init__(self):
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_limit = 3

        # bullet setting
        self.bullet_width = 300
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3000

        # alien setting
        self.fleet_drop_speed = 20

        # 加速设置
        self.speedup_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 2

        # fleet_direction为1向右移动，-1向左移动
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
