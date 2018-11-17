# -*- coding: utf-8 -*-
import uuid
import sys


class BaseAction(object):
    def __init__(self, game_manager, during_count=None):
        self.game_manager = game_manager
        self.id = uuid.uuid1()
        self.start_time = None
        self.during_count = during_count

    def complete(self):
        pass

    def save(self):
        return {"id": self.id,
                "start_time": self.start_time,
                "during_count": self.during_count,

                "base_action_module": self.__class__.__module__,
                "base_action_class": self.__class__.__name__}

    def load_base_element(self, value):
        self.id = value['id']
        self.start_time = value['start_time']
        self.during_count = value['during_count']

        self.__class__ = getattr(sys.modules[value["base_action_module"]], value["base_action_class"])

    def load_reference(self, value):
        pass


class MoveAction(BaseAction):
    def __init__(self, game_manager, during_count=None, actor=None, route=None):
        super(MoveAction, self).__init__(game_manager, during_count)
        self.during_count = 5

        self.actor = actor
        self.route = route

    def complete(self):
        self.actor.move(self.route)
        self.actor.ask_for_next_action()

    def save(self):
        result = super(MoveAction, self).save()
        result['actor_name'] = self.actor.name
        result['route_name'] = self.route.name
        return result

    def load_base_element(self, value):
        pass

    def load_reference(self, value):
        self.actor = self.game_manager.actor_manage.find_actor(value['actor_name'])
        self.route = self.game_manager.map_manager.find_route(value['route_name'])


class EatAction(BaseAction):
    def __init__(self, game_manager, during_count=None, actor=None, item=None):
        super(EatAction, self).__init__(game_manager, during_count)
        self.during_count = 2

        self.actor = actor
        self.item = item

    def complete(self):
        try:

        except ValueError:
            print("Hi, guy! Put down this food!")

    def save(self):
        result = super(EatAction, self).save()
        result['actor_name'] = self.actor.name
        return result

    def load_base_element(self, value):
        pass

    def load_reference(self, value):
        self.actor = self.game_manager.actor_manage.find_actor(value['actor_name'])


class SleepAction(BaseAction):
    def __init__(self, game_manager, during_count=None, actor=None):
        super(SleepAction, self).__init__(game_manager, during_count)
        self.during_count = 10

        self.actor = actor

    def complete(self):
        pass

    def save(self):
        result = super(SleepAction, self).save()
        result['actor_name'] = self.actor.name
        return result

    def load_base_element(self, value):
        pass

    def load_reference(self, value):
        self.actor = self.game_manager.actor_manage.find_actor(value['actor_name'])
