# -*- coding: utf-8 -*-
from NormalCase.Map.BaseMapNode import BaseMapNode
from NormalCase.Action.DetailedAction import *


class Airport(BaseMapNode):
    def __init__(self, game_manager, name="", location_x=0, location_y=0):
        super(Airport, self).__init__(game_manager, name, location_x, location_y)
        self.possible_action_list = [StealAction, MoveAction]   # TODO
        self.add_attribute_value_list = []


class Shop(BaseMapNode):
    def __init__(self, game_manager, name="", location_x=0, location_y=0):
        super(Shop, self).__init__(game_manager, name, location_x, location_y)
        self.possible_action_list = [StealAction, MoveAction]   # TODO
        self.add_attribute_value_list = []
