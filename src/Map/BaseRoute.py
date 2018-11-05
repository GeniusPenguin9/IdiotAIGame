# -*- coding: utf-8 -*-
class BaseRoute(object):
    def __init__(self, game_manager, name="", neighbour_node1=None, neighbour_node2=None):
        self.name = name
        self.neighbour_node_name = [] if neighbour_node1 is None and neighbour_node2 is None else [neighbour_node1.name,
                                                                                                   neighbour_node2.name]
        self.length = 0 if neighbour_node1 is None and neighbour_node2 is None else pow(
            pow(neighbour_node1.location_x - neighbour_node2.location_x, 2) + pow(
                neighbour_node1.location_y - neighbour_node2.location_y, 2), 0.5)
        self.game_manager = game_manager

    def save(self):
        return {"name": self.name, "neighbour_node_name": self.neighbour_node_name, "length": self.length}

    def load_base_element(self, value):
        self.name = value['name']
        self.neighbour_node_name = value['neighbour_node_name']
        self.length = value['length']

    def load_reference(self, value):
        pass
