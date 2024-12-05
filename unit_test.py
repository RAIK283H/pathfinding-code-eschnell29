import math
import unittest
from pathing import dfs_path, bfs_path
from permutation import is_ham_cycle
from permutation import get_all_sjt_permutations
from permutation import find_all_hamiltonian_cycles
from pathing import dijkstra_path
from f_w import floyd_warshall, construct_full_path

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

    def test_correct_dijkstra_path(self):
        result = dijkstra_path(0, 2, self.hamGraph1)
        self.assertEqual(result, [0,1,2], "Dijkstra should return correct path from 0 to 2")
    
    def test_correct_dijkstra_path_2(self):
        result = dijkstra_path(1, 2, self.hamGraph1)
        self.assertEqual(result, [1,2], "Dijkstra should return correct path from 1 to 2")

    def test_no_path_dijkstra(self):
        result = dijkstra_path(1,3,self.hamGraph1)
        self.assertEqual(result, [], "Dijkstra should return empty cause no path")
    
    def test_disconnected_path_dijkstra(self):
        result = dijkstra_path(0, 3, self.noHamGraph)
        self.assertEqual(result, [], "Dijkstra returns empty path because disconnected nodes")
    
    def test_dijkstra_path_edge_case(self):
        graph = {0: [(0, 0), []]} 
        result = dijkstra_path(0, 0, graph) 
        self.assertEqual(result, [0], "Dijkstra return path containing only start node")

    def test_dijkstra_path_multiple_paths(self):
        graph = {
            0: [(0, 0), [1, 2]],
            1: [(1, 0), [0, 3]],
            2: [(0, 1), [0, 3]],
            3: [(1, 1), [1, 2]],
        }
        result = dijkstra_path(0, 3, graph)
        self.assertEqual(result, [0, 1, 3], "Dijkstra should return the shortest path from 0 to 3")

    
    def test_floyd_warshall_correctness(self):
        graph = {
            0: [(0, 0), [1, 2]],
            1: [(1, 0), [0, 3]],
            2: [(0, 1), [0, 3]],
            3: [(1, 1), [1, 2]],
        }
        expected_distances = [
            [0, 1, 1, 2],
            [1, 0, 2, 1],
            [1, 2, 0, 1],
            [2, 1, 1, 0],
        ]
        distance, _ = floyd_warshall(graph)
        self.assertEqual(distance, expected_distances, "should calculate correct shortest paths.")
        
    def test_construct_full_path(self):
        graph = {
            0: [(0, 0), [1, 2]],
            1: [(1, 0), [0, 3]],
            2: [(0, 1), [0, 3]],
            3: [(1, 1), [1, 2]],
        }
        _, parents = floyd_warshall(graph)
        path = construct_full_path(parents, 0, 3)
        expected_path = [0, 1, 3]
        self.assertEqual(path, expected_path, "should return the correct shortest path from 0 to 3.")

    def test_floyd_warshall_disconnected_graph(self):
        graph = {
            0: [(0, 0), [1]],
            1: [(1, 0), [0]],
            2: [(0, 1), [3]],
            3: [(1, 1), [2]],
        }
        distance, _ = floyd_warshall(graph)
        self.assertEqual(distance[0][2], math.inf, "should show no path between disconnected nodes.")
    
    def test_single_node_graph(self):
        self.single_node_graph = {
            0: [(0, 0), []]
        }

        distances, parents = floyd_warshall(self.single_node_graph)
        self.assertEqual(distances[0][0], 0, "Distance should be 0")
        self.assertEqual(construct_full_path(parents, 0, 0), [], "Path should be []")


    def test_path_with_no_direct_edges(self):
        graph_no_edges = {
            0: [(0, 0), [1]],
            1: [(1, 0), [0]],
        }
        distances, parents = floyd_warshall(graph_no_edges)
        self.assertEqual(distances[0][1], 1, "Distance from 0 to 1 should be 1")
        self.assertEqual(construct_full_path(parents, 0, 1), [0, 1], "Path from 0 to 1 should be [0, 1]")

    def test_multiple_paths_same_distance(self):
        graph_same_distance = {
            0: [(0, 0), [1, 2]],
            1: [(1, 0), [0, 3]],
            2: [(0, 1), [0, 3]],
            3: [(1, 1), [1, 2]],
        }
        distances, parents = floyd_warshall(graph_same_distance)
        self.assertEqual(distances[0][3], 2, "Shortest distance from 0 to 3 should be 2")
        path = construct_full_path(parents, 0, 3)
        self.assertIn(path, [[0, 1, 3], [0, 2, 3]], "Path should be one of [0, 1, 3] or [0, 2, 3]")

if __name__ == '__main__':
    unittest.main()
