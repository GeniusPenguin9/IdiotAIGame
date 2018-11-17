# -*- coding: utf-8 -*-
import uuid


class BaseEvent(object):
    def __init__(self, game_manager, actor=None):
        self.game_manager = game_manager
        self.id = uuid.uuid1()
        self.actor = actor
        self.start_time = 0
        self.end_time = self.start_time + self.actor.current_action.during_count
