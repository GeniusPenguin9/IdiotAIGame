# -*- coding: utf-8 -*-
from Actor.BaseActor import *


class NPC(BaseActor):
    def __init__(self, game_manager, name=None, job=None, money=None, current_location=None):
        super(NPC, self).__init__(game_manager, name, job, money, current_location)


class Police(NPC):
    def __init__(self, game_manager, name=None, money=None, current_location=None):
        super(Police, self).__init__(game_manager, name, 'Police', money, current_location)
