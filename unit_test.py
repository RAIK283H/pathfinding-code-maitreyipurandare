import math
import unittest
import graph_data
from pathing import get_bfs_path
from pathing import get_dfs_path 
import global_game_data


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


if __name__ == '__main__':
    unittest.main()
