# -*- coding: utf-8 -*-
from Actor.NPC import *
from Actor.Player import *
from Map.MapManager import *
import os


class GameManager(object):
    def __init__(self, npc_list, player, map_manager):
        if npc_list is not list:
            raise ValueError('npc_list should be a list')
        else:
            for n in npc_list:
                if n is not NPC:
                    raise ValueError('wrong npc list')
            self._NPC_list = npc_list

        if player is Player:
            self._player = player
        else:
            raise ValueError('wrong player')

        if map_manager is not MapManager:
            raise ValueError('map_manager should be a MapManager')
        else:
            self._map_manager = map_manager


def save_game(game_manager):
    with open(os.path.join('./GameFile', 'GameFile.txt'), 'w') as f:
        f.write(game_manager)
