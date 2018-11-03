# -*- coding: utf-8 -*-
from Actor.NPC import *
from Actor.Player import *


class ActorManager(object):
    def __init__(self, game_manager, player=None, npc_list=None):
        self.game_manager = game_manager
        self.npc_list = npc_list if npc_list is not None else []
        self.player = player

    def save(self):
        return {"npc_list": [npc.save() for npc in self.npc_list],
                "player": None if self.player is None else self.player.save()}

    def load(self, value):
        self.npc_list = []
        for npc_dict in value["npc_list"]:
            npc = NPC(self.game_manager)
            npc.load(npc_dict)
            self.npc_list.append(npc)

        if value["player"] is not None:
            self.player = Player(self.game_manager)
            self.player.load(value["player"])
