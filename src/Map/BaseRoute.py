# -*- coding: utf-8 -*-
class BaseRoute(object):
    def __init__(self, game_manager, name="", starting_node=None, end_node=None, add_attribute_list=None):
        self.game_manager = game_manager
        self.name = name
        self.neighbour_node = [] if starting_node is None and end_node is None else [starting_node,
                                                                                     end_node]
        self.add_attribute_list = add_attribute_list
        self.length = 0 if starting_node is None and end_node is None else pow(
            pow(starting_node.location_x - end_node.location_x, 2) + pow(
                starting_node.location_y - end_node.location_y, 2), 0.5)

    def save(self):
        return {"name": self.name, "neighbour_node_name": [node.name for node in self.neighbour_node],
                "add_attribute_list": self.add_attribute_list,
                "length": self.length}

    def load_base_element(self, value):
        self.name = value['name']
        self.add_attribute_list = value['add_attribute_list']
        self.length = value['length']

    def load_reference(self, value):
        self.neighbour_node = [self.game_manager.map_manager.find_node(node_name) for node_name in
                               value['neighbour_node_name']]
