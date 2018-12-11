# -*- coding: utf-8 -*-
# @Time    : 2018/12/4
# @Author  : Yifei Duan
# @Summary :


class Settings:
    """a cleass to store settings for Alien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 5
        self.ship_limit = 3

        # bullet setting:
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3000

        # alien setting:
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 60

        # fleet_direction为1向右移动，-1向左移动
        self.fleet_direction = 1
