# -*- coding: utf-8 -*-


class BaseActor(object):
    def __init__(self, game_manager, name=None, job=None, money=None, item_list=None, current_location=None,
                 current_action=None):
        self.game_manager = game_manager
        self.name = name
        self.job = job

        self.possible_action_list = []

        self.attribute_list = [money, 100, 100]  # money, energy, full
        self.current_location = None if current_location is None else current_location
        self.current_action = current_action
        self.item_list = item_list

    def perform_action(self, action):
        self.attribute_list[0] += action.add_attribute_factor_list
