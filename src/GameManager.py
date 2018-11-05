# -*- coding: utf-8 -*-
from Map.MapManager import *
from Actor.ActorManager import *
from Time.TimeManager import *
import os
import json


class GameManager(object):
    def __init__(self):
        self.actor_manager = ActorManager(self)
        self.map_manager = MapManager(self)
        self.time_manager = TimeManager(self)

    def new_game(self):
        pass

    def save(self):
        return {"actor_manager": self.actor_manager.save(), "map_manager": self.map_manager.save(),
                "time_manager": self.time_manager.save()}

    def load_base_element(self, value):
        self.map_manager = MapManager(self)
        self.map_manager.load_base_element(value["map_manager"])

        self.actor_manager = ActorManager(self)
        self.actor_manager.load_base_element(value["actor_manager"])

        self.time_manager = TimeManager(self)
        self.time_manager.load_base_element(value['time_manager'])

    def load_reference(self, value):
        self.map_manager.load_reference(value["map_manager"])
        self.actor_manager.load_reference(value["actor_manager"])
        self.time_manager.load_reference(value['time_manager'])

    def save_game(self, file):
        with open(os.path.join('./GameFile', file), 'w') as f:
            json_str = json.dumps(self.save(), indent='    ')
            f.write(json_str)

    def load_game(self, file):
        with open(os.path.join('./GameFile', file), 'r') as f:
            file = json.loads(f.read())
            self.load_base_element(file)
            self.load_reference(file)
