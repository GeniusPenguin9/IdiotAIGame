# -*- coding: utf-8 -*-
from Actor.NPC import *
from Actor.Player import *


class ActorManager(object):
    def __init__(self, game_manager, player=None, npc_list=None):
        self.game_manager = game_manager
        self.npc_list = npc_list if npc_list is not None else []
        self.player = player

    def find_actor(self, name):
        for npc in self.npc_list:
            if npc.name == name:
                return npc

    def save(self):
        return {"npc_list": [npc.save() for npc in self.npc_list],
                "player": None if self.player is None else self.player.save()}

    def load_base_element(self, value):
        self.npc_list = []
        for npc_dict in value["npc_list"]:
            npc = NPC(self.game_manager)
            npc.load_base_element(npc_dict)
            self.npc_list.append(npc)

        if value["player"] is not None:
            self.player = Player(self.game_manager)
            self.player.load_base_element(value["player"])

    def load_reference(self, value):
        for npc_dict in value["npc_list"]:
            npc = self.find_actor(npc_dict['name'])
            npc.load_reference(npc_dict)
        if value["player"] is not None:
            self.player.load_reference(value['player'])
