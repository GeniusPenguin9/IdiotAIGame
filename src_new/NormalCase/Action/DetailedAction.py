# -*- coding: utf-8 -*-
from NormalCase.Action.BaseAction import BaseAction


class MoveAction(BaseAction):
    def __init__(self, game_manager, name=None, route=None):
        super(MoveAction, self).__init__(game_manager, name)
        self.during_count = None  # TODO
        self.add_attribute_factor_list = []  # TODO
        self.route = route

    def action_dependence(self, item):
        pass


class EatAction(BaseAction):
    def __init__(self, game_manager, name=None, item=None):
        super(EatAction, self).__init__(game_manager, name)
        self.during_count = None  # TODO
        self.add_attribute_factor_list = []  # TODO
        self.item = item

    def action_dependence(self, item):
        pass


class StealAction(BaseAction):
    def __init__(self, game_manager, name=None, item=None):
        super(StealAction, self).__init__(game_manager, name)
        self.during_count = None  # TODO
        self.add_attribute_factor_list = []  # TODO
        self.item = item

    def action_dependence(self, item):
        pass


class SleepAction(BaseAction):
    def __init__(self, game_manager, name=None):
        super(SleepAction, self).__init__(game_manager, name)
        self.during_count = None  # TODO
        self.add_attribute_factor_list = []  # TODO
        self.during_count = 10

    def action_dependence(self, item):
        pass
