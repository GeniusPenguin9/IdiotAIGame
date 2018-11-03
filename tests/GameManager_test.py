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
        old = GameManager()

        npc1 = NPC(old, 'Penguin', 'Penguin', 1000000000000, None)
        player1 = Player(old, 'Husky', 'Dog', 9, None)
        node1 = BaseMapNode(old, "shop")

        player1.move_location(node1)

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

    def test_save_police(self):
        old = GameManager()
        shop = Shop(old)
        old.map_manager.node_list.append(shop)
        police = Police(old, "penguin")

        old.actor_manager.npc_list.append(police)
        old.save_game('GameFile3.txt')

        new = GameManager()
        new.load_game('GameFile3.txt')
        self.assertTrue(isinstance(new.actor_manager.npc_list[0], Police))
        self.assertTrue(isinstance(new.map_manager.node_list[0], Shop))

    def test_load_complex(self):
        old = GameManager()
        node1 = BaseMapNode(old, "n1")
        node2 = BaseMapNode(old, "n2")
        node1.add_routes([node2])
        node2.add_routes([node1])
        old.map_manager.node_list = [node1, node2]

        police = Police(old, "penguin")
        old.actor_manager.npc_list.append(police)
        police.move_location(node2)

        old.save_game("GameFile4.txt")

        new = GameManager()
        new.load_game("GameFile4.txt")
        self.assertEqual(new.map_manager.node_list[0], new.map_manager.node_list[1].routes[0])
        self.assertEqual(new.map_manager.node_list[1], new.map_manager.node_list[0].routes[0])
        self.assertEqual(old.actor_manager.npc_list[0].current_location.name,
                         new.actor_manager.npc_list[0].current_location.name)
