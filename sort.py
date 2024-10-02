class BinaryTree:
    class Node:
        def __init__(self, value: object):
            self.value = value
            self.left = None
            self.right = None

    class OfType:
        class Complete:
            def __init__(self):
                self.root = None

            def insert(self, value):
                if self.root is None:
                    self.root = BinaryTree.Node(value)
                else:
                    self.__insert_recursive(self.root, value)

            def __insert_recursive(self, node, value):
                if value < node.value:
                    if node.left is None:
                        node.left = BinaryTree.Node(value)
                    else:
                        self.__insert_recursive(node.left, value)
                else:
                    if node.right is None:
                        node.right = BinaryTree.Node(value)
                    else:
                        self.__insert_recursive(node.right, value)

            def inorder_traversal(self):
                result = []
                self.__inorder_traversal_recursive(self.root, result)
                return result

            def __inorder_traversal_recursive(self, node, result):
                if node:
                    self.__inorder_traversal_recursive(node.left, result)
                    result.append(node.value)
                    self.__inorder_traversal_recursive(node.right, result)

        class Search:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

            def sort(self, root) -> list[int | float]:
                if root is None:
                    return []

                left_values = self.sort(root.left)
                values = [root.val]
                right_values = self.sort(root.right)

                return left_values + values + right_values

        class PerfectTree:
            def __init__(self):
                self.root = None

            def insert(self, value):
                if not self.root:
                    self.root = BinaryTree.Node(value)
                else:
                    self._insert(self.root, value)

            def _insert(self, node, value):
                if node is None:
                    return BinaryTree.Node(value)
                if not node.left and not node.right:
                    if value < node.value:
                        node.left = BinaryTree.Node(value)
                    else:
                        node.right = BinaryTree.Node(value)
                else:
                    if value < node.value:
                        node.left = self._insert(node.left, value)
                    else:
                        node.right = self._insert(node.right, value)
                return node

            def is_perfect(self):
                return self._is_perfect(self.root)

            def _is_perfect(self, node):
                if not node:
                    return True
                if not node.left or not node.right:
                    return False
                return self._is_perfect(node.left) and self._is_perfect(node.right)

    class CreateStatic:
        class PerfectTree:
            def __init__(self, height):
                self.height = height
                self.nodes = [None] * (2 ** height - 1)

            def create(self):
                self._create(0)

            def _create(self, index):
                if index < len(self.nodes):
                    self._create(2 * index + 1)
                    # noinspection PyTypeChecker
                    self.nodes[index] = BinaryTree.Node(index)
                    self._create(2 * index + 2)

            def return_tree(self) -> str:
                levels = []
                self.__print_tree(0, 0, levels)
                tree_str = self.__format_tree(levels)
                return tree_str

            @staticmethod
            def __format_tree(levels):
                if not levels:
                    return ""
                tree_str = ""
                max_width = len(" ".join(str(node.value) if node else "None" for node in levels[-1]))
                for level in levels:
                    level_str = " ".join(str(node.value) if node else "None" for node in level)
                    tree_str += level_str.center(max_width) + "\n"
                return tree_str.replace("None", " ")

            def return_list(self) -> list[int | None]:
                return [node.value if node else None for node in self.nodes]

            def __print_tree(self, index, level, levels):
                if index < len(self.nodes):
                    if len(levels) == level:
                        levels.append([])
                    levels[level].append(self.nodes[index])
                    self.__print_tree(2 * index + 1, level + 1, levels)
                    self.__print_tree(2 * index + 2, level + 1, levels)
