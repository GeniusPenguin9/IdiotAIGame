# -*- coding: utf-8 -*-
import uuid


class BaseItem(object):
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.id = uuid.uuid1()
        self.possible_action_list = []
        self.add_attribute_value_list = []
