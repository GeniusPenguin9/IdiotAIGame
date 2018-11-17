# -*- coding: utf-8 -*-
import sys

from Time.BaseAction import MoveAction, EatAction, SleepAction


class BaseActor(object):
    def __init__(self, game_manager, name=None, job=None, money=None, item_list=None, current_location=None):
        self.name = name
        self.job = job
        self.attribute_list = [money, 100, 100, None if current_location is None else current_location]  # money, energy, full, current_location
        self.possible_action_list = [MoveAction, EatAction]
        self.item_list = item_list
        self.game_manager = game_manager


    def move(self, route):
        move_action = MoveAction(self.game_manager, None, self, self.current_location, next_location)
        self.game_manager.time_manager.add_action(move_action)

    def ask_for_next_action(self):
        temp_choice=[]
        for action in self.possible_action_list:
            if action is MoveAction:
                for route in self.game_manager.map_manager.route_list:
                    value = route.add_attribute_list[0]+route.add_attribute_list[1]+route.add_attribute_list[2]
                    if value > 0:
                        temp_choice.append([value, action('route=' + route.name)])
            if action is EatAction:
                for item in self.item_list:
                    value = item.add_attribute_list[0]+item.add_attribute_list[1]+item.add_attribute_list[2]
                    if value > 0:
                        temp_choice.append([value, action('item=' + item.name)])


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
