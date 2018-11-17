# -*- coding: utf-8 -*-


class BaseItem(object):
    def __init__(self, game_manager, name='', add_attribute_list=None):
        self.game_manager = game_manager
        self.name = name
        self.add_attribute_list = add_attribute_list


class Apple(BaseItem):
    def __init__(self, game_manager):
        super(Apple, self).__init__(game_manager, 'apple', [0, +1, +5])
