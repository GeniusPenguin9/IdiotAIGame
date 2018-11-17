# -*- coding: utf-8 -*-
from NormalCase.Item.BaseItem import BaseItem
from NormalCase.Action.DetailedAction import *


class Bread(BaseItem):
    def __init__(self, game_manager):
        super(Bread, self).__init__(game_manager)
        self.possible_action_list = [EatAction, StealAction]  # TODO
        self.add_attribute_value_list = []
