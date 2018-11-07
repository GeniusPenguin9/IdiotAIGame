# -*- coding: utf-8 -*-
from Map.BaseMapNode import *
from Map.BaseRoute import *


class MapManager(object):
    def __init__(self, game_manager, node_list=None, route_list=None):
        self.game_manager = game_manager
        self.node_list = node_list if node_list is not None else []
        self.route_list = route_list if route_list is not None else []

    def add_node(self, new_node):
        if isinstance(new_node, BaseMapNode):
            raise ValueError('new_node should be a BaseMapNode')
        self.node_list.append(new_node)

    def add_route(self, new_route):
        self.route_list.append(new_route)

    def update_node_routes(self):
        for each_node in self.node_list:
            for each_route in self.route_list:
                if each_node in each_route.neighbour_node:
                    each_node.routes.append(each_route)

    def save(self):
        return {"node_list": [node.save() for node in self.node_list],
                "route_list": [route.save() for route in self.route_list]}

    def find_node(self, name):
        for node in self.node_list:
            if node.name == name:
                return node
        return None

    def find_route(self, name):
        for route in self.route_list:
            if route.name == name:
                return route
        return None

    def load_base_element(self, value):
        self.node_list = []
        for node_dict in value["node_list"]:
            node = BaseMapNode(self.game_manager)
            node.load_base_element(node_dict)
            self.node_list.append(node)
        self.route_list = []
        for route_dict in value['route_list']:
            route = BaseRoute(self.game_manager)
            route.load_base_element(route_dict)
            self.route_list.append(route)

    def load_reference(self, value):
        for node_dict in value["node_list"]:
            node = self.find_node(node_dict['name'])
            node.load_reference(node_dict)
        for route_dict in value['route_list']:
            route = self.find_route(route_dict['name'])
            route.load_reference(route_dict)
