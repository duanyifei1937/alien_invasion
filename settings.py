# -*- coding: utf-8 -*-
# @Time    : 2018/12/4
# @Author  : Yifei Duan
# @Summary :


class Settings:
    """a cleass to store settings for Alien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_heighy = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2

        # bullet setting:
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
