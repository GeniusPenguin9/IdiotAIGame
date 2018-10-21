# -*- coding: utf-8 -*-
class BaseMapNode(object):
    def __init__(self):
        self.routes = []

    # @property
    # def energy(self):
    #     return self._energy
    #
    # @energy.setter
    # def energy(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('energy must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('energy must between 0 ~ 100!')
    #     self._energy = value

    def add_routes(self, neighbour_nodes):
        if not isinstance(neighbour_nodes, list):
            raise ValueError('\'neighbour_nodes\' should be a list')
        for n in neighbour_nodes:
            if not isinstance(n, BaseMapNode):
                raise ValueError('neighbour_node should be a BaseMapNode')
            if n in self.routes:
                raise ValueError('neighbour_node cannot be duplicated')
        self.routes.extend(neighbour_nodes)


class Airport(BaseMapNode):
    def __init__(self):
        super(Airport, self).__init__()


class Shop(BaseMapNode):
    def __init__(self):
        super(Shop, self).__init__()



