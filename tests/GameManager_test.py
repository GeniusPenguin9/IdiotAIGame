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
        self.assertEqual(old.actor_manager.player.current_location_name, new.actor_manager.player.current_location_name)
        self.assertEqual(new.map_manager.node_list[0].name, new.actor_manager.player.current_location_name)

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
        node1 = BaseMapNode(old, "n1", 20, 20)
        node2 = BaseMapNode(old, "n2", 30, 40)
        node3 = BaseMapNode(old, "n3", 0, 40)
        old.map_manager.node_list = [node1, node2, node3]
        route1 = BaseRoute(old, 'route1', node1, node2)
        route2 = BaseRoute(old, 'route2', node1, node3)
        old.map_manager.route_list = [route1, route2]
        old.map_manager.update_node_routes()

        police = Police(old, "penguin")
        old.actor_manager.npc_list.append(police)
        police.move_location(node1)
        police.move_location(node2)
        with self.assertRaises(ValueError):
            police.move_location(node3)
        police.move_location(node1)
        police.move_location(node3)
        old.save_game("GameFile4.txt")

        new = GameManager()
        new.load_game("GameFile4.txt")
        self.assertEqual(old.actor_manager.npc_list[0].current_location_name,
                         new.actor_manager.npc_list[0].current_location_name)
        self.assertEqual(new.time_manager.time_slice_count, 75)
        pass

    def test_time_manager(self):
        old = GameManager()
        node1 = BaseMapNode(old, "n1", 20, 20)
        node2 = BaseMapNode(old, "n2", 30, 40)
        node3 = BaseMapNode(old, "n3", 0, 40)
        old.map_manager.node_list = [node1, node2, node3]
        route1 = BaseRoute(old, 'route1', node1, node2)
        route2 = BaseRoute(old, 'route2', node1, node3)
        old.map_manager.route_list = [route1, route2]
        old.map_manager.update_node_routes()

        police = Police(old, "penguin")
        old.actor_manager.npc_list.append(police)
        police.move_location(node1)
        police.move_location(node2)
        self.assertEqual(police.current_location_name, "n1")
        old.time_manager.run_time(25)
        self.assertEqual(police.current_location_name, "n2")
