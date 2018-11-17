# -*- coding: utf-8 -*-
from NormalCase.Actor.BaseActor import *


class NPC(BaseActor):
    def __init__(self, game_manager, name=None, job=None, money=None, item_list=None, current_location=None,
                 current_action=None):
        super(NPC, self).__init__(game_manager, name, job, money, item_list, current_location, current_action)
