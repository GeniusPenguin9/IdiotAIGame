# -*- coding: utf-8 -*-
from Actor.BaseActor import *


class Player(BaseActor):
    def __init__(self, game_manager, name=None, job=None, money=None, current_location=None):
        super(Player, self).__init__(game_manager, name, job, money, current_location)
