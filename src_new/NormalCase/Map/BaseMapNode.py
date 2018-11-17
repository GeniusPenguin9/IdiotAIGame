# -*- coding: utf-8 -*-


class BaseMapNode(object):
    def __init__(self, game_manager, name="", location_x=0, location_y=0):
        self.game_manager = game_manager
        self.name = name
        self.routes = []
        self.location_x = location_x
        self.location_y = location_y
        self.possible_action_list = []
        self.add_attribute_value_list = []
