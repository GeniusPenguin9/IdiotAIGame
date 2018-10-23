# import unittest
#
#
# class TestBaseMapNode(unittest.TestCase):
#     def test_init(self):
#         b = BaseMapNode()
#         self.assertEqual(b.energy, 0)
#         self.assertEqual(b.routes, [])
#
#     def test_wrong_energy(self):
#         b = BaseMapNode()
#         with self.assertRaises(ValueError):
#             b.energy = 300
#         with self.assertRaises(ValueError):
#             b.energy = []
#
#     def test_add_routes(self):
#         b = BaseMapNode()
#         a = Airport()
#         b.add_routes([a])
#         self.assertEqual(b.routes, [a])
#         with self.assertRaises(ValueError):
#             b.add_routes([a])
#         with self.assertRaises(ValueError):
#             b.add_routes([1])
#         with self.assertRaises(ValueError):
#             b.add_routes('test')
#
#
# class TestAirport(unittest.TestCase):
#     def test_init(self):
#         a = Airport()
#         self.assertEqual(a.energy, 10)
#         self.assertEqual(a.routes, [])
#
#
# class TestMapManager(unittest.TestCase):
#     def test_empty_map_manager(self):
#         map1 = MapManager()
#         self.assertEqual(map1.node_list, [])
#         self.assertEqual(map1.current_node, None)
#
#         a1 = Airport()
#         a2 = Airport()
#         s1 = Shop()
#         a1.routes = [s1, a2]
#         map1.add_node([a1, a2, s1])
#
#         map1.move_node(a1)
#         self.assertEqual(map1.current_node, a1)
#
#         map1.move_node(a2)
#         self.assertEqual(map1.current_node, a2)
#
#         with self.assertRaises(ValueError):
#             map1.move_node(s1)
#
#
# if __name__ == '__main__':
#     unittest.main()
