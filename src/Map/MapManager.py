# -*- coding: utf-8 -*-
from Map.BaseMapNode import *


class MapManager(object):
    def __init__(self, node_list=None):
        """ initializes a node_list
            If no list or None is given,
            an empty node_list will be used
        """
        self.node_list = node_list if node_list is not None else []

    def node_list(self):
        return self.node_list

    def add_node(self, new_node):
        """create a new node"""
        if isinstance(new_node, BaseMapNode):
            raise ValueError('new_node should be a BaseMapNode')
        self.node_list = self.node_list.append(new_node)

