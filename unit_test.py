import math
import unittest
from pathing import dfs_path, bfs_path


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
    def setUp(self):
        self.graph1 = {
                0: [(0, 0), [1, 2]],
                1: [(1, 0), [0, 3]],
                2: [(0, 1), [0, 3]],
                3: [(1, 1), [1, 2]]
            }
    
    def test_dfs_path(self):
        result = dfs_path(self.graph1, 0, 3)
        self.assertIsNotNone(result, "DFS should find a path and it shouldn't be None")
        self.assertEqual(result[-1], 3, "path should end at node 3")
        self.assertEqual(result[0], 0, "path should start at node 0")
    
    def test_bfs_path(self):
        result = bfs_path(self.graph1, 0,3)
        self.assertIsNotNone(result, "BFS should find a path that is not None")
        self.assertEqual(result[-1], 3, "path should end at node 3")
        self.assertEqual(result[0], 0, "path should start at node 0")


if __name__ == '__main__':
    unittest.main()
