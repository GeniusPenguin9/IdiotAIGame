# -*- coding: utf-8 -*-


class BaseRoute(object):
    def __init__(self, game_manager, name="", starting_node=None, end_node=None):
        self.game_manager = game_manager
        self.name = name
        self.add_attribute_value_list = []
        self.neighbour_node = [] if starting_node is None and end_node is None else [starting_node,
                                                                                     end_node]
        self.length = 0 if starting_node is None and end_node is None else pow(
            pow(starting_node.location_x - end_node.location_x, 2) + pow(
                starting_node.location_y - end_node.location_y, 2), 0.5)
