# -*- coding: utf-8 -*-
# @Time    : 2018/12/10
# @Author  : Yifei Duan
# @Summary :


class GameStats:
    """统计游戏信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚开始为活动状态：
        self.game_active = False

        # 最高分
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏运行期间变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1