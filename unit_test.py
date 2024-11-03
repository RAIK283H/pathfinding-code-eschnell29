import math
import unittest
from pathing import dfs_path, bfs_path
from permutation import is_ham_cycle
from permutation import get_all_sjt_permutations
from permutation import find_all_hamiltonian_cycles

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
        self.hamGraph1 = {
            0: [(0, 0), [1]],
            1: [(1, 0), [0, 2]],
            2: [(0, 1), [1]]
        }
        self.noHamGraph = {
            0: [(0, 0), [1]],
            1: [(1, 1), []], 
            2: [(0, 2), [3]],
            3: [(1, 2), [2]] 
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

    def test_valid_cycle(self):
        path = [0,1,2]
        self.assertTrue(is_ham_cycle(self.hamGraph1, path))

    def test_invalide_start_node(self):
        path = [1,0,2]
        self.assertFalse(is_ham_cycle(self.hamGraph1, path))

    def test_invalid_end_node(self):
        path = [0, 1, 2, 0]  
        self.assertFalse(is_ham_cycle(self.hamGraph1, path))

    def test_no_edge(self):
        path = [0,1,3]
        self.assertFalse(is_ham_cycle(self.hamGraph1, path))
    
    def test_non_hamiltonian_cycle(self):
        path = [0, 1, 2, 0]
        self.assertFalse(is_ham_cycle(self.hamGraph1, path))
    
    def test_no_hamiltonian_cycle(self):
        path = find_all_hamiltonian_cycles(self.noHamGraph)
        self.assertIn(path, [-1, False], "Expected -1 or False for no Hamiltonian cycle.")

    def test_sjt_zero(self):
        self.assertEqual(get_all_sjt_permutations(0), [[]])

    def test_sjt_one(self):
        self.assertEqual(get_all_sjt_permutations(1), [[0]])

    def test_sjt_no_duplicates(self):
        permutations = get_all_sjt_permutations(3)
        unique_permutations = [list(x) for x in set(tuple(p) for p in permutations)]
        self.assertEqual(len(permutations), len(unique_permutations), "SJT generated duplicate permutations.")
    
    def test_sjt_four(self):
        expected_response_length = 24
        result = get_all_sjt_permutations(4)
        self.assertEqual(len(result), expected_response_length)

if __name__ == '__main__':
    unittest.main()
