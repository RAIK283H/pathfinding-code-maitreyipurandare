import math
import unittest
import graph_data
from pathing import get_bfs_path
from pathing import get_dfs_path 
import global_game_data
import permutation


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
        global_game_data.current_graph_index = 0 
        global_game_data.target_node = [1] 
        global_game_data.graph_paths = []

    def test_DFS_correct_path(self):
        expected_path = [0, 1, 2]
        actual_path = get_dfs_path()
        self.assertEqual(expected_path, actual_path, "dfs path is not correct")

    def test_DFS_incorrect_path(self):
        expected_path = [0, 1, 0, 1, 2]
        actual_path = get_dfs_path()
        self.assertNotEqual(expected_path, actual_path, "dfs path is not correct")

    def test_BFS_correct_path(self):
        expected_path = [0, 1, 2]
        actual_path = get_bfs_path()
        self.assertEqual(expected_path, actual_path, "bfs path is not correct")

    def test_BFS_incorrect_path(self):
        expected_path = [0, 1, 0, 1, 2]
        actual_path = get_bfs_path()
        self.assertNotEqual(expected_path, actual_path, "bfs path is not correct")


    def test_Hamiltonian_Not_False(self):
        graph = [
            [(0, 0), [1, 5]],         
            [(50, -200), [0, 2, 3, 4]],  
            [(50, -300), [1, 3]],     
            [(200, -500), [1, 2, 4]],    
            [(200, 100), [0, 3, 1]], 
            [(300, 100), [0, 4]]
            ]
        
        expected = [[1, 2, 3, 4], [4, 1, 2, 3], [1, 4, 3, 2], [3, 4, 1, 2], [4, 3, 2, 1], [3, 2, 1, 4], [2, 3, 4, 1], [2, 1, 4, 3]]
        h_list = (permutation.get_Hamiltonian_List((permutation.SJT(len(graph) - 1)), graph))
        self.assertEqual(h_list, expected, "did not get the hamiltonian cycles correctly")
    
    def test_Hamiltonian_Not_False_On_Given_Graph(self):
        graph = graph_data.graph_data[1]
        
        expected = [[1, 2], [2, 1]] 
        h_list = (permutation.get_Hamiltonian_List((permutation.SJT(len(graph) - 1)), graph))
        self.assertEqual(h_list, expected, "did not get the hamiltonian cycles correctly")
    
    def test_Hamiltonian_False(self):
        graph = [
            [(0, 0), [1, 2, 3, 4]],         
            [(50, -200), [0]],  
            [(50, -300), [0]],     
            [(200, -500), [0]],    
            [(200, 100), [0]], 
            ]
        actual = permutation.get_Hamiltonian_List((permutation.SJT(len(graph) - 1)), graph)
        self.assertFalse(actual, "should be false (no cycles) but was not")

    def test_Hamiltonian_False_on_Given_graph(self):
        graph = graph_data.graph_data[0]
        actual = permutation.get_Hamiltonian_List((permutation.SJT(len(graph) - 1)), graph)
        self.assertFalse(actual, "should be false (no cycles) but was not")

    def test_permutationsSJT(self):
        actual = permutation.SJT(3)
        expected = [[1, 2], [2, 1]]
        self.assertEqual(actual, expected, "did not get all the permutations correctly")


if __name__ == '__main__':
    unittest.main()
