# -*- coding: utf-8 -*-
from Map.BaseMapNode import *


class MapManager(object):
    def __init__(self, node_list=None, current_node=None):
        """ initializes a node_list
            If no list or None is given,
            an empty node_list will be used
        """

        self.node_list = node_list if node_list is not None else []
        if current_node is None:
            pass
        elif current_node not in self.node_list:
            raise ValueError('current_node should be included in node_list')
        self.current_node = current_node

    def add_node(self, new_node):
        """create a new node"""
        if isinstance(new_node, BaseMapNode):
            raise ValueError('new_node should be a BaseMapNode')
        self.node_list = self.node_list.append(new_node)

    def move_node(self, next_node):
        if self.current_node is None:
            self.current_node = next_node
        else:
            if next_node not in self.current_node.routes:
                raise ValueError('you cannot move to this location')
            self.current_node = next_node
