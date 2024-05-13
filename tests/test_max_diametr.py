from ..src.max_diameter import *
import unittest


class TestDiameter(unittest.TestCase):
    def test_example_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right.right = BinaryTree(5)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right.right = BinaryTree(6)
        self.assertEqual(diameter(root), 6)

    def test_example_2(self):
        root = BinaryTree(50)
        root.left = BinaryTree(31)
        root.right = BinaryTree(80)
        root.left.left = BinaryTree(28)
        root.left.right = BinaryTree(40)
        root.left.left.left = BinaryTree(20)
        root.left.right.left = BinaryTree(39)
        root.left.right.right = BinaryTree(42)
        root.left.left.left.left = BinaryTree(19)
        root.left.left.left.right = BinaryTree(25)
        root.left.right.right.right = BinaryTree(45)
        root.left.right.right.right.right = BinaryTree(48)
        self.assertEqual(diameter(root), 7)


