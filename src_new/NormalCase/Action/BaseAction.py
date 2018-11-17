# -*- coding: utf-8 -*-


class BaseAction(object):
    def __init__(self, game_manager, name=None):
        self.game_manager = game_manager
        self.name = name
        self.during_count = None
        self.add_attribute_factor_list = []

    def action_dependence(self, item):
        pass
