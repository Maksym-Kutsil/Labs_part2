import unittest
from src.maze import *

class TestMaze(unittest.TestCase):

    def test_single_path_maze(self):
        input_file = 'C:/Users/User/Desktop/Lab 5/resources/test_input.txt'
        output_file = 'C:/Users/User/Desktop/Lab 5/resources/test_output.txt'

        start, finish, size, labyrinth = read_input(input_file)

        result = shotres_way(start, finish, size, labyrinth)

        expected_result = 10

        write_output(output_file, result)

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()



