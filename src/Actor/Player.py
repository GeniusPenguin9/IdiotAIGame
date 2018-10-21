# -*- coding: utf-8 -*-
from Actor.Actor import *


class Player(BaseActor):
    def __init__(self, name, job, money, current_location):
        super(Player, self).__init__(name, job, money, current_location)
