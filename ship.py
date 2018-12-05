# -*- coding: utf-8 -*-
# @Time    : 2018/12/4
# @Author  : Yifei Duan
# @Summary :

import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_rigth = False
        self.moving_left = False

    def update(self):
        if self.moving_rigth:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
