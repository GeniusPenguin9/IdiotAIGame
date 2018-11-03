# -*- coding: utf-8 -*-
from Actor.NPC import *
from Actor.Player import *
from Map.MapManager import *
from Actor.ActorManager import *
import os
import json


class GameManager(object):
    def __init__(self):
        self.actor_manager = ActorManager(self)
        self.map_manager = MapManager(self)

    def new_game(self):
        pass

    def save(self):
        return {"actor_manager": self.actor_manager.save(), "map_manager": self.map_manager.save()}

    def load_base_element(self, value):
        self.map_manager = MapManager(self)
        self.map_manager.load_base_element(value["map_manager"])

        self.actor_manager = ActorManager(self)
        self.actor_manager.load_base_element(value["actor_manager"])

    def load_reference(self, value):
        self.map_manager.load_reference(value["map_manager"])
        self.actor_manager.load_reference(value["actor_manager"])

    def save_game(self, file):
        with open(os.path.join('./GameFile', file), 'w') as f:
            json_str = json.dumps(self.save(), indent='    ')
            f.write(json_str)

    def load_game(self, file):
        with open(os.path.join('./GameFile', file), 'r') as f:
            self.load_base_element(json.loads(f.read()))
        with open(os.path.join('./GameFile', file), 'r') as f:
            self.load_reference(json.loads(f.read()))
