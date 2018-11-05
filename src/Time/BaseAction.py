# -*- coding: utf-8 -*-


class BaseAction(object):
    def __init__(self, game_manager, action_name=""):
        self.game_manager = game_manager
        self.action_name = action_name
