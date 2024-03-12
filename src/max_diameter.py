class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def diameter(root: BinaryTree) -> int:
    max_diameter = 0

    def height(node):
        nonlocal max_diameter
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height , right_height)

    height(root)
    return max_diameter

