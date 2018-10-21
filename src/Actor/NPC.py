# -*- coding: utf-8 -*-
from Actor.Actor import *


class NPC(BaseActor):
    def __init__(self, name, job, money, current_location):
        super(NPC, self).__init__(name, job, money, current_location)


class Police(NPC):
    def __init__(self, name, money, current_location):
        super(Police, self).__init__(name, 'Police', money, current_location)
