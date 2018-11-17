# -*- coding: utf-8 -*-
from NormalCase.Actor.BaseActor import *


class Player(BaseActor):
    def __init__(self, game_manager, name=None, job=None, money=None, item_list=None, current_location=None,
                 current_action=None):
        super(Player, self).__init__(game_manager, name, job, money, item_list, current_location, current_action)
