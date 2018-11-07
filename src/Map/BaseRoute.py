# -*- coding: utf-8 -*-
class BaseRoute(object):
    def __init__(self, game_manager, name="", neighbour_node1=None, neighbour_node2=None):
        self.game_manager = game_manager
        self.name = name
        self.neighbour_node = [] if neighbour_node1 is None and neighbour_node2 is None else [neighbour_node1,
                                                                                              neighbour_node2]
        self.length = 0 if neighbour_node1 is None and neighbour_node2 is None else pow(
            pow(neighbour_node1.location_x - neighbour_node2.location_x, 2) + pow(
                neighbour_node1.location_y - neighbour_node2.location_y, 2), 0.5)

    def save(self):
        return {"name": self.name, "neighbour_node_name": [node.name for node in self.neighbour_node],
                "length": self.length}

    def load_base_element(self, value):
        self.name = value['name']
        self.length = value['length']

    def load_reference(self, value):
        self.neighbour_node = [self.game_manager.map_manager.find_node(node_name) for node_name in
                               value['neighbour_node_name']]
