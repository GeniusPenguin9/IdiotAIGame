# -*- coding: utf-8 -*-
import sys


class BaseMapNode(object):
    def __init__(self, game_manager, name="", location_x=0, location_y=0):
        self.name = name
        self.routes = []
        self.game_manager = game_manager
        self.location_x = location_x
        self.location_y = location_y

    def set_location_xy(self, x, y):
        self.location_x = x
        self.location_y = y

    def save(self):
        return {
            "name": self.name,
            "routes_name": [route.name for route in self.routes],
            "location_x": self.location_x,
            "location_y": self.location_y,
            "base_map_node_module": self.__class__.__module__,
            "base_map_node_class": self.__class__.__name__}

    def load_base_element(self, value):
        self.name = value["name"]
        self.location_x = value["location_x"]
        self.location_y = value["location_y"]
        self.__class__ = getattr(sys.modules[value["base_map_node_module"]], value["base_map_node_class"])

    def load_reference(self, value):
        self.routes = [self.game_manager.map_manager.find_route(route_name) for route_name in value['routes_name']]


class Airport(BaseMapNode):
    def __init__(self, game_manager, name=""):
        super(Airport, self).__init__(game_manager, name)


class Shop(BaseMapNode):
    def __init__(self, game_manager, name=""):
        super(Shop, self).__init__(game_manager, name)



