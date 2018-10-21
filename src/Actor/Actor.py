# -*- coding: utf-8 -*-
from Map.MapManager import *


class BaseActor(object):
    def __init__(self, name, job, money, current_location):
        self.name = name
        self.job = job
        self._money = money
        self._energy = 100
        self._full = 100

        if current_location not in MapManager.node_list:
            raise ValueError('current_location should be included in node_list')
        self._current_location = current_location

    @property
    def money(self):
        return self._money

    def add_money(self, change_money):
        if change_money is not int:
            raise ValueError('change_money should be a int object')
        if (self._money + change_money) < 0:
            raise ValueError('your money is less than what you want')
        else:
            self._money += change_money

    @property
    def energy(self):
        return self._energy

    def add_energy(self, change_energy):
        if change_energy is not int:
            raise ValueError('change_energy should be a int object')
        if (self._energy + change_energy) < 0:
            raise ValueError('your change_energy is less than what you want')
        else:
            self._energy = min(self._energy + change_energy, 100)

    @property
    def full(self):
        return self._full

    def add_full(self, change_full):
        if change_full is not int:
            raise ValueError('change_full should be a int object')
        if (self._full + change_full) < 0:
            raise ValueError('your change_full is less than what you want')
        else:
            self._full = min(self._full + change_full, 100)

    def move_location(self, next_location):
            if next_location not in self._current_location.routes:
                raise ValueError('you cannot move to this location')
            self._current_location = next_location
