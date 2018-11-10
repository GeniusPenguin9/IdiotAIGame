# -*- coding: utf-8 -*-
import sys

from Time.BaseAction import MoveAction, EatAction


class BaseActor(object):
    def __init__(self, game_manager, name=None, job=None, money=None, current_location=None):
        self.name = name
        self.job = job
        self.attribute_list = [money, 100, 100]  # money, energy, full
        self.feasible_action_list = [MoveAction, EatAction]
        self.current_location = None if current_location is None else current_location
        self.game_manager = game_manager

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

    def ask_for_next_action(self):
        next_requirement = self.judge_requirement()
        # TODO: find all the helpful ways for next_requirement

    def judge_requirement(self):
        requirement = 0
        requirement_value = 0
        for n in range(len(self.attribute_list)):
            value = 100 - self.attribute_list[n]
            if value > requirement_value:
                requirement_value = value
                requirement = n
        return requirement


    def save(self):
        return {
            "name": self.name,
            "job": self.job,
            "attribute_list": self.attribute_list
            "current_location_name": None if self.current_location is None else self.current_location.name,

            "actor_class": self.__class__.__name__,
            "actor_module": self.__class__.__module__}

    def load_base_element(self, value):
        self.name = value["name"]
        self.job = value["job"]
        self.attribute_list = value['attribute_list']

        self.__class__ = getattr(sys.modules[value["actor_module"]], value["actor_class"])

    def load_reference(self, value):
        self.current_location = self.game_manager.map_manager.find_node(value['current_location_name'])
