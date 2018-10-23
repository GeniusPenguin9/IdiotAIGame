import unittest
from GameManager import *
from Actor.Player import *
from Map.MapManager import *


class TestGameManager(unittest.TestCase):
    def test_save_game_empty(self):
        old = GameManager()
        old.save_game('GameFile1.txt')

        new = GameManager()
        new.load_game('GameFile1.txt')

        self.assertEqual(old.map_manager.node_list, new.map_manager.node_list)
        self.assertEqual(old.actor_manager.player, new.actor_manager.player)
        self.assertEqual(old.actor_manager.npc_list, new.actor_manager.npc_list)

    def test_save_game(self):
        npc1 = NPC('Penguin', 'Penguin', 1000000000000, None)
        player1 = Player('Husky', 'Dog', 9, None)
        node1 = BaseMapNode("shop")

        player1.move_location(node1)

        old = GameManager()
        old.actor_manager.player = player1
        old.actor_manager.npc_list.append(npc1)
        old.map_manager.node_list.append(node1)
        old.save_game('GameFile2.txt')

        new = GameManager()
        new.load_game('GameFile2.txt')

        self.assertEqual(len(old.map_manager.node_list), len(new.map_manager.node_list))
        self.assertEqual(old.map_manager.node_list[0].name, new.map_manager.node_list[0].name)

        self.assertEqual(old.actor_manager.player.name, new.actor_manager.player.name)
        self.assertEqual(old.actor_manager.player.current_location.name, new.actor_manager.player.current_location.name)
        self.assertEqual(new.map_manager.node_list[0], new.actor_manager.player.current_location)
