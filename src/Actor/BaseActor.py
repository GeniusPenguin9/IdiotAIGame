# -*- coding: utf-8 -*-
import sys

from Time.BaseAction import MoveAction


class BaseActor(object):
    def __init__(self, game_manager, name=None, job=None, money=None, current_location=None):
        self.name = name
        self.job = job
        self.money = money
        self.energy = 100
        self.full = 100
        self.current_location = None if current_location is None else current_location
        self.game_manager = game_manager

    def add_money(self, change_money):
        if change_money is not int:
            raise ValueError('change_money should be a int object')
        if (self.money + change_money) < 0:
            raise ValueError('your money is less than what you want')
        else:
            self.money += change_money

    def add_energy(self, change_energy):
        if change_energy is not int:
            raise ValueError('change_energy should be a int object')
        if (self.energy + change_energy) < 0:
            raise ValueError('your change_energy is less than what you want')
        else:
            self.energy = min(self.energy + change_energy, 100)

    def add_full(self, change_full):
        if change_full is not int:
            raise ValueError('change_full should be a int object')
        if (self.full + change_full) < 0:
            raise ValueError('your change_full is less than what you want')
        else:
            self.full = min(self.full + change_full, 100)

    def move_location(self, next_location):
        if self.current_location is None:
            self.current_location = next_location
        else:
            for route in self.current_location.routes:
                if self.current_location in route.neighbour_node and next_location in route.neighbour_node:
                    self.current_location = next_location
                    return
            raise ValueError('you cannot move to this location because no route is available')

    def move(self, next_location):
        move_action = MoveAction(self.game_manager, None, self, self.current_location, next_location)
        self.game_manager.time_manager.add_action(move_action)

    def save(self):
        return {
            "name": self.name,
            "job": self.job,
            "money": self.money,
            "energy": self.energy,
            "full": self.full,
            "current_location_name": None if self.current_location is None else self.current_location.name,

            "actor_class": self.__class__.__name__,
            "actor_module": self.__class__.__module__}

    def load_base_element(self, value):
        self.name = value["name"]
        self.job = value["job"]
        self.money = value["money"]
        self.energy = value["energy"]
        self.full = value["full"]

        self.__class__ = getattr(sys.modules[value["actor_module"]], value["actor_class"])

    def load_reference(self, value):
        self.current_location = self.game_manager.map_manager.find_node(value['current_location_name'])
