# -*- coding: utf-8 -*-


class ActorManager(object):
    def __init__(self, game_manager, player=None, npc_list=None):
        self.game_manager = game_manager
        self.npc_list = npc_list if npc_list is not None else []
        self.player = player

    def find_actor(self, name):
        if self.player.name == name:
            return self.player
        else:
            for npc in self.npc_list:
                if npc.name == name:
                    return npc
