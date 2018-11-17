# -*- coding: utf-8 -*-
from NormalCase.Action.ActionManager import ActionManager
from NormalCase.Actor.ActorManager import ActorManager
from NormalCase.Item.ItemManager import ItemManager
from NormalCase.Map.MapManager import MapManager
from Event.EventManager import EventManager
import os
import json


class GameManager(object):
    def __init__(self):
        self.action_manager = ActionManager(self)
        self.actor_manager = ActorManager(self)
        self.item_manager = ItemManager(self)
        self.map_manager = MapManager(self)
        self.event_manager = EventManager(self)

    def new_game(self):
        pass

    def save_game(self, file):
        with open(os.path.join('./GameFile', file), 'w') as f:
            json_str = json.dumps(self.save(), indent='    ')
            f.write(json_str)

    def save(self):
        return {"action_manager": self.action_manager.save(),
                "actor_manager": self.actor_manager.save(),
                "item_manager": self.item_manager.save(),
                "map_manager": self.map_manager.save(),
                "event_manager": self.event_manager.save()
                }

    def load_game(self, file):
        with open(os.path.join('./GameFile', file), 'r') as f:
            file = json.loads(f.read())
            self.load_base_element(file)
            self.load_reference(file)

    def load_base_element(self, value):
        self.action_manager = ActionManager(self)
        self.action_manager.load_base_element(value["action_manager"])

        self.actor_manager = ActorManager(self)
        self.actor_manager.load_base_element(value["actor_manager"])

        self.item_manager = ItemManager(self)
        self.item_manager.load_base_element(value["item_manager"])

        self.map_manager = MapManager(self)
        self.map_manager.load_base_element(value["map_manager"])

        self.event_manager = EventManager(self)
        self.event_manager.load_base_element(value['event_manager'])

    def load_reference(self, value):
        self.action_manager.load_reference(value["action_manager"])
        self.actor_manager.load_reference(value["actor_manager"])
        self.item_manager.load_reference(value['item_manager'])
        self.map_manager.load_reference(value['map_manager'])
        self.event_manager.load_reference(value['event_manager'])
