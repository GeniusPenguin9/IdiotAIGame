# -*- coding: utf-8 -*-


class MapManager(object):
    def __init__(self, game_manager, node_list=None, route_list=None):
        self.game_manager = game_manager
        self.node_list = node_list if node_list is not None else []
        self.route_list = route_list if route_list is not None else []

    def add_node(self, new_node):
        self.node_list.append(new_node)

    def add_route(self, new_route):
        self.route_list.append(new_route)

    def update_node_routes(self):
        for each_node in self.node_list:
            for each_route in self.route_list:
                if each_node in each_route.neighbour_node:
                    each_node.routes.append(each_route)

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
