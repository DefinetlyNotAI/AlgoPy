# TODO Turn everything to classmethod

class BinaryTreeOfType:
    class _Node:
        def __init__(self, value: object):
            self.value = value
            self.left = None
            self.right = None

    class _AVLNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

    class AVL:
        @classmethod
        def insert(cls, root, key):
            if not root:
                return BinaryTreeOfType._AVLNode(key)
            elif key < root.key:
                root.left = cls.insert(root.left, key)
            else:
                root.right = cls.insert(root.right, key)

            root.height = 1 + max(cls.Get.height(root.left), cls.Get.height(root.right))
            balance = cls.Get.balance(root)

            # Left, Left
            if balance > 1 and key < root.left.key:
                return cls.__right_rotate(root)
            # Right, Right
            if balance < -1 and key > root.right.key:
                return cls.__left_rotate(root)
            # Left Right
            if balance > 1 and key > root.left.key:
                root.left = cls.__left_rotate(root.left)
                return cls.__right_rotate(root)
            # Right Left
            if balance < -1 and key < root.right.key:
                root.right = cls.__right_rotate(root.right)
                return cls.__left_rotate(root)

            return root

        @classmethod
        def delete(cls, root, key):
            if not root:
                return root

            if key < root.key:
                root.left = cls.delete(root.left, key)
            elif key > root.key:
                root.right = cls.delete(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                temp = cls.__min_value_node(root.right)
                root.key = temp.key
                root.right = cls.delete(root.right, temp.key)

            if root is None:
                return root

            root.height = 1 + max(cls.Get.height(root.left), cls.Get.height(root.right))
            balance = cls.Get.balance(root)

            # Left, Left
            if balance > 1 and cls.Get.balance(root.left) >= 0:
                return cls.__right_rotate(root)
            # Left, Right
            if balance > 1 and cls.Get.balance(root.left) < 0:
                root.left = cls.__left_rotate(root.left)
                return cls.__right_rotate(root)
            # Right, Right
            if balance < -1 and cls.Get.balance(root.right) <= 0:
                return cls.__left_rotate(root)
            # Right, Left
            if balance < -1 and cls.Get.balance(root.right) > 0:
                root.right = cls.__right_rotate(root.right)
                return cls.__left_rotate(root)

            return root

        @classmethod
        def __left_rotate(cls, z):
            y = z.right
            T2 = y.left
            y.left = z
            z.right = T2
            z.height = 1 + max(cls.Get.height(z.left), cls.Get.height(z.right))
            y.height = 1 + max(cls.Get.height(y.left), cls.Get.height(y.right))
            return y

        @classmethod
        def __right_rotate(cls, z):
            y = z.left
            T3 = y.right
            y.right = z
            z.left = T3
            z.height = 1 + max(cls.Get.height(z.left), cls.Get.height(z.right))
            y.height = 1 + max(cls.Get.height(y.left), cls.Get.height(y.right))
            return y

        @classmethod
        def pre_order(cls, root):
            if not root:
                return
            print("{0} ".format(root.key), end="")
            cls.pre_order(root.left)
            cls.pre_order(root.right)

        class Get:
            @staticmethod
            def height(root):
                if not root:
                    return 0
                return root.height

            @classmethod
            def balance(cls, root):
                if not root:
                    return 0
                return cls.height(root.left) - cls.height(root.right)

        @classmethod
        def __min_value_node(cls, root):
            if root is None or root.left is None:
                return root
            return cls.__min_value_node(root.left)

    class Complete:
        # TODO Add delete method
        def __init__(self):
            self.root = None

        def insert(self, value):
            if self.root is None:
                self.root = BinaryTreeOfType._Node(value)
            else:
                self.__insert_recursive(self.root, value)

        def __insert_recursive(self, node, value):
            if value < node.value:
                if node.left is None:
                    node.left = BinaryTreeOfType._Node(value)
                else:
                    self.__insert_recursive(node.left, value)
            else:
                if node.right is None:
                    node.right = BinaryTreeOfType._Node(value)
                else:
                    self.__insert_recursive(node.right, value)

        def traverse(self):
            result = []
            self.__inorder_traversal_recursive(self.root, result)
            return result

        def __inorder_traversal_recursive(self, node, result):
            if node:
                self.__inorder_traversal_recursive(node.left, result)
                result.append(node.value)
                self.__inorder_traversal_recursive(node.right, result)

    class Degenerate:
        def __init__(self):
            self.root = None

        def insert(self, key):
            if self.root is None:
                self.root = BinaryTreeOfType._Node(key)
            else:
                current = self.root
                while current.right is not None:
                    current = current.right
                current.right = BinaryTreeOfType._Node(key)

        def search(self, key):
            current = self.root
            while current is not None:
                if current.key == key:
                    return True
                current = current.right
            return False

        def delete(self, key):
            if self.root is None:
                return
            if self.root.key == key:
                self.root = self.root.right
                return
            current = self.root
            while current.right is not None:
                if current.right.key == key:
                    current.right = current.right.right
                    return
                current = current.right

        def traverse(self):
            current = self.root
            while current is not None:
                print(current.key, end=" -> ")
                current = current.right
            print("None")

    class Perfect:
        @classmethod
        def __init__(cls, height):
            cls.height = height
            cls.nodes = [None] * (2 ** height - 1)

        @classmethod
        def create(cls):
            cls.__create(0)

        @classmethod
        def __create(cls, index):
            if index < len(cls.nodes):
                cls.__create(2 * index + 1)
                # noinspection PyTypeChecker
                cls.nodes[index] = BinaryTreeOfType._Node(index)
                cls.__create(2 * index + 2)

        @classmethod
        def return_tree(cls) -> str:
            levels = []
            cls.__print_tree(0, 0, levels)
            tree_str = cls.__format_tree(levels)
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

        @classmethod
        def return_list(cls) -> list[int | None]:
            return [node.value if node else None for node in cls.nodes]

        @classmethod
        def __print_tree(cls, index, level, levels):
            if index < len(cls.nodes):
                if len(levels) == level:
                    levels.append([])
                levels[level].append(cls.nodes[index])
                cls.__print_tree(2 * index + 1, level + 1, levels)
                cls.__print_tree(2 * index + 2, level + 1, levels)

#       Red-black tree
#       B+ tree
#       Segment tree
