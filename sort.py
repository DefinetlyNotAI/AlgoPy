# TODO Turn everything to classmethod
# TODO Remove all prints etc
# TODO Each method should return the result and specify its type


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

    class _RBNode:
        def __init__(self, data, color="red"):
            self.data = data
            self.color = color
            self.left = None
            self.right = None
            self.parent = None

    class _BPlusTreeNode:
        def __init__(self, is_leaf=False):
            self.is_leaf = is_leaf
            self.keys = []
            self.children = []

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

        @classmethod
        def __min_value_node(cls, root):
            if root is None or root.left is None:
                return root
            return cls.__min_value_node(root.left)

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

    class Complete:
        @classmethod
        def __init__(cls):
            cls.root = None

        @classmethod
        def insert(cls, value):
            if cls.root is None:
                cls.root = BinaryTreeOfType._Node(value)
            else:
                cls.__insert_recursive(cls.root, value)

        @classmethod
        def __insert_recursive(cls, node, value):
            if value < node.value:
                if node.left is None:
                    node.left = BinaryTreeOfType._Node(value)
                else:
                    cls.__insert_recursive(node.left, value)
            else:
                if node.right is None:
                    node.right = BinaryTreeOfType._Node(value)
                else:
                    cls.__insert_recursive(node.right, value)

        @classmethod
        def delete(cls, value):
            cls.root = cls.__delete_recursive(cls.root, value)

        @classmethod
        def __delete_recursive(cls, node, value):
            if node is None:
                return node
            if value < node.value:
                node.left = cls.__delete_recursive(node.left, value)
            elif value > node.value:
                node.right = cls.__delete_recursive(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = cls.__min_value_node(node.right)
                node.value = temp.value
                node.right = cls.__delete_recursive(node.right, temp.value)
            return node

        @staticmethod
        def __min_value_node(node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        @classmethod
        def traverse(cls):
            result = []
            cls.__inorder_traversal_recursive(cls.root, result)
            return result

        @classmethod
        def __inorder_traversal_recursive(cls, node, result):
            if node:
                cls.__inorder_traversal_recursive(node.left, result)
                result.append(node.value)
                cls.__inorder_traversal_recursive(node.right, result)

    class Degenerate:
        @classmethod
        def __init__(cls):
            cls.root = None

        @classmethod
        def insert(cls, key):
            if cls.root is None:
                cls.root = BinaryTreeOfType._Node(key)
            else:
                current = cls.root
                while current.right is not None:
                    current = current.right
                current.right = BinaryTreeOfType._Node(key)

        @classmethod
        def search(cls, key):
            current = cls.root
            while current is not None:
                if current.key == key:
                    return True
                current = current.right
            return False

        @classmethod
        def delete(cls, key):
            if cls.root is None:
                return
            if cls.root.key == key:
                cls.root = cls.root.right
                return
            current = cls.root
            while current.right is not None:
                if current.right.key == key:
                    current.right = current.right.right
                    return
                current = current.right

        @classmethod
        def traverse(cls):
            current = cls.root
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

    class RedBlackTree:
        @classmethod
        def __init__(cls):
            cls.NIL = BinaryTreeOfType._RBNode(data=None, color="black")  # Sentinel node for leaves
            cls.root = cls.NIL

        @classmethod
        def insert(cls, key):
            new_node = BinaryTreeOfType._RBNode(key)
            new_node.left = cls.NIL
            new_node.right = cls.NIL
            parent = None
            current = cls.root

            while current != cls.NIL:
                parent = current
                if new_node.data < current.data:
                    current = current.left
                else:
                    current = current.right

            new_node.parent = parent
            if parent is None:
                cls.root = new_node
            elif new_node.data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

            new_node.color = "red"
            cls.insert_fixup(new_node)

        @classmethod
        def insert_fixup(cls, node):
            while node != cls.root and node.parent.color == "red":
                if node.parent == node.parent.parent.left:
                    uncle = node.parent.parent.right
                    if uncle.color == "red":
                        node.parent.color = "black"
                        uncle.color = "black"
                        node.parent.parent.color = "red"
                        node = node.parent.parent
                    else:
                        if node == node.parent.right:
                            node = node.parent
                            cls.left_rotate(node)
                        node.parent.color = "black"
                        node.parent.parent.color = "red"
                        cls.right_rotate(node.parent.parent)
                else:
                    uncle = node.parent.parent.left
                    if uncle.color == "red":
                        node.parent.color = "black"
                        uncle.color = "black"
                        node.parent.parent.color = "red"
                        node = node.parent.parent
                    else:
                        if node == node.parent.left:
                            node = node.parent
                            cls.right_rotate(node)
                        node.parent.color = "black"
                        node.parent.parent.color = "red"
                        cls.left_rotate(node.parent.parent)
            cls.root.color = "black"

        @classmethod
        def left_rotate(cls, x):
            y = x.right
            x.right = y.left
            if y.left != cls.NIL:
                y.left.parent = x
            y.parent = x.parent
            if x.parent is None:
                cls.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
            y.left = x
            x.parent = y

        @classmethod
        def right_rotate(cls, y):
            x = y.left
            y.left = x.right
            if x.right != cls.NIL:
                x.right.parent = y
            x.parent = y.parent
            if y.parent is None:
                cls.root = x
            elif y == y.parent.right:
                y.parent.right = x
            else:
                y.parent.left = x
            x.right = y
            y.parent = x

        @classmethod
        def __repr__(cls):
            def recurse(node):
                if node == cls.NIL:
                    return []
                return recurse(node.left) + [node.data] + recurse(node.right)

            return str(recurse(cls.root))

    class BPlusTree:
        @classmethod
        def __init__(cls, t=3):
            cls.root = BinaryTreeOfType._BPlusTreeNode(is_leaf=True)
            cls.t = t

        @classmethod
        def insert(cls, key):
            root = cls.root
            if len(root.keys) == (2 * cls.t) - 1:
                temp = BinaryTreeOfType._BPlusTreeNode()
                cls.root = temp
                temp.children.append(root)
                cls.split_child(temp, 0)
                cls.insert_non_full(temp, key)
            else:
                cls.insert_non_full(root, key)

        @classmethod
        def insert_non_full(cls, node, key):
            if node.is_leaf:
                node.keys.append(key)
                node.keys.sort()
            else:
                i = len(node.keys) - 1
                while i >= 0 and key < node.keys[i]:
                    i -= 1
                i += 1
                if len(node.children[i].keys) == (2 * cls.t) - 1:
                    cls.split_child(node, i)
                    if key > node.keys[i]:
                        i += 1
                cls.insert_non_full(node.children[i], key)

        @classmethod
        def split_child(cls, node, i):
            t = cls.t
            y = node.children[i]
            z = BinaryTreeOfType._BPlusTreeNode(is_leaf=y.is_leaf)
            node.children.insert(i + 1, z)
            node.keys.insert(i, y.keys[t - 1])
            z.keys = y.keys[t:(2 * t) - 1]
            y.keys = y.keys[0:t - 1]
            if not y.is_leaf:
                z.children = y.children[t:(2 * t)]
                y.children = y.children[0:t]

        @classmethod
        def search(cls, key, node=None):
            if node is None:
                node = cls.root
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return True
            if node.is_leaf:
                return False
            else:
                return cls.search(key, node.children[i])

        @classmethod
        def traverse(cls, node=None, level=0):
            if node is None:
                node = cls.root
            print("Level", level, ":", " ".join(str(key) for key in node.keys))
            if not node.is_leaf:
                for child in node.children:
                    cls.traverse(child, level + 1)

    class SegmentTree:
        @classmethod
        def __init__(cls, data):
            cls.n = len(data)
            cls.tree = [0] * (2 * cls.n)
            cls.__build(data)

        @classmethod
        def __build(cls, data):
            # Insert leaf nodes in tree
            for i in range(cls.n):
                cls.tree[cls.n + i] = data[i]
            # Build the tree by calculating parents
            for i in range(cls.n - 1, 0, -1):
                cls.tree[i] = cls.tree[i * 2] + cls.tree[i * 2 + 1]

        @classmethod
        def update(cls, pos, value):
            # Update leaf node
            pos += cls.n
            cls.tree[pos] = value
            # Update internal nodes
            while pos > 1:
                pos //= 2
                cls.tree[pos] = cls.tree[2 * pos] + cls.tree[2 * pos + 1]

        @classmethod
        def query(cls, left, right):
            # Range sum query
            left += cls.n
            right += cls.n
            sum_query = 0
            while left <= right:
                if left % 2 == 1:
                    sum_query += cls.tree[left]
                    left += 1
                if right % 2 == 0:
                    sum_query += cls.tree[right]
                    right -= 1
                left //= 2
                right //= 2
            return sum_query
