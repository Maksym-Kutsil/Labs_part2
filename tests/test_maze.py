import unittest
from src.maze import *

class EmptyMaze(unittest.TestCase):

    def test_single_path_maze(self):
        input_file = 'C:/Users/User/Desktop/Lab 5/resources/test_input.txt'
        output_file = 'C:/Users/User/Desktop/Lab 5/resources/test_output.txt'

        start, finish, size, labyrinth = read_input(input_file)

        result = shotres_way(start, finish, size, labyrinth)

        expected_result = None

        write_output(output_file, result)

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

class TestMaze(unittest.TestCase):

    def test_single_path_maze(self):
        input_file = 'C:/Users/User/Desktop/Lab 5/resources/test2_input.txt'
        output_file = 'C:/Users/User/Desktop/Lab 5/resources/test2_output.txt'

        start, finish, size, maze = read_input(input_file)

        result = shotres_way(start, finish, size, maze)

        expected_result = 9

        write_output(output_file, result)

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()



