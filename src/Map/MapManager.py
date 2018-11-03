# -*- coding: utf-8 -*-
from Map.BaseMapNode import *


class MapManager(object):
    def __init__(self, game_manager, node_list=None):
        """ initializes a node_list
            If no list or None is given,
            an empty node_list will be used
        """
        self.game_manager = game_manager
        self.node_list = node_list if node_list is not None else []

    def add_node(self, new_node):
        """create a new node"""
        if isinstance(new_node, BaseMapNode):
            raise ValueError('new_node should be a BaseMapNode')
        self.node_list = self.node_list.append(new_node)

    def save(self):
        return {"node_list": [node.save() for node in self.node_list]}

    def find(self, name):
        for node in self.node_list:
            if node.name == name:
                return node
        return None

    def load(self, value):
        self.node_list = []
        for node_dict in value["node_list"]:
            node = BaseMapNode(self.game_manager)
            node.load(node_dict)
            self.node_list.append(node)
        for node_dict in value["node_list"]:
            node = self.find(node_dict['name'])
            node.load_route(node_dict)

