# -*- coding: utf-8 -*-
import sys


class BaseMapNode(object):
    def __init__(self, game_manager, name=""):
        self.routes = []
        self.name = name
        self.game_manager = game_manager

    def add_routes(self, neighbour_nodes):
        if not isinstance(neighbour_nodes, list):
            raise ValueError('\'neighbour_nodes\' should be a list')
        for n in neighbour_nodes:
            if not isinstance(n, BaseMapNode):
                raise ValueError('neighbour_node should be a BaseMapNode')
            if n in self.routes:
                raise ValueError('neighbour_node cannot be duplicated')
        self.routes.extend(neighbour_nodes)

    def save(self):
        return {
            "name": self.name,
            "routes": [node.name for node in self.routes],
            "base_map_node_module": self.__class__.__module__,
            "base_map_node_class": self.__class__.__name__}

    def load(self, value):
        self.name = value["name"]
        self.routes = []
        self.__class__ = getattr(sys.modules[value["base_map_node_module"]], value["base_map_node_class"])

    def load_route(self, value):
        for route_name in value["routes"]:
            route = self.game_manager.map_manager.find(route_name)
            self.routes.append(route)


class Airport(BaseMapNode):
    def __init__(self, game_manager, name=""):
        super(Airport, self).__init__(game_manager, name)


class Shop(BaseMapNode):
    def __init__(self, game_manager, name=""):
        super(Shop, self).__init__(game_manager, name)



