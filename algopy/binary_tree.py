from typing import Optional, List


class BinaryTree:
    class _Node:
        """
        Represents a node in a binary tree.

        Attributes:
            value (int): The value stored in the node.
            left (Optional[BinaryTree._Node]): The left child of the node.
            right (Optional[BinaryTree._Node]): The right child of the node.
            key (int): The key of the node, same as value.
        """

        def __init__(self, value: int) -> None:
            self.value: int = value
            self.left: Optional[BinaryTree._Node] = None
            self.right: Optional[BinaryTree._Node] = None
            self.key: int = value

    class _AVLNode:
        """
        Represents a node in an AVL tree.

        Attributes:
            key (int): The key stored in the node.
            left (Optional[BinaryTree._AVLNode]): The left child of the node.
            right (Optional[BinaryTree._AVLNode]): The right child of the node.
            height (int): The height of the node.
        """

        def __init__(self, key: int) -> None:
            self.key: int = key
            self.left: Optional[BinaryTree._AVLNode] = None
            self.right: Optional[BinaryTree._AVLNode] = None
            self.height: int = 1

    class _RBNode:
        """
        Represents a node in a Red-Black tree.

        Attributes:
            data (Optional[int]): The data stored in the node.
            color (str): The color of the node, either "red" or "black".
            left (Optional[BinaryTree._RBNode]): The left child of the node.
            right (Optional[BinaryTree._RBNode]): The right child of the node.
            parent (Optional[BinaryTree._RBNode]): The parent of the node.
        """

        def __init__(self, data: Optional[int], color: str = "red") -> None:
            self.data: Optional[int] = data
            self.color: str = color
            self.left: Optional[BinaryTree._RBNode] = None
            self.right: Optional[BinaryTree._RBNode] = None
            self.parent: Optional[BinaryTree._RBNode] = None

    class _BPlusTreeNode:
        """
        Represents a node in a B+ tree.

        Attributes:
            is_leaf (bool): Indicates if the node is a leaf.
            keys (List[int]): The keys stored in the node.
            children (List[BinaryTree._BPlusTreeNode]): The children of the node.
        """

        def __init__(self, is_leaf: bool = False) -> None:
            self.is_leaf: bool = is_leaf
            self.keys: List[int] = []
            self.children: List[BinaryTree._BPlusTreeNode] = []

    class AVL:
        @classmethod
        def insert(cls, root, key: int):
            """
            Inserts a key into the AVL tree and balances the tree if necessary.

            Args:
                root (BinaryTree._AVLNode): The root of the AVL tree.
                key (int): The key to insert.

            Returns:
                BinaryTree._AVLNode: The new root of the AVL tree.
            """
            if not isinstance(root, BinaryTree._AVLNode) and root is not None:
                raise TypeError(
                    "Root must be an instance of BinaryTree._AVLNode"
                )
            if not root:
                return BinaryTree._AVLNode(key)
            if key < root.key:
                root.left = cls.insert(root.left, key)
            else:
                root.right = cls.insert(root.right, key)

            root.height = 1 + max(
                cls._Get.height(root.left), cls._Get.height(root.right)
            )
            balance = cls._Get.balance(root)

            if balance > 1:
                if key < root.left.key:
                    return cls.__right_rotate(root)
                root.left = cls.__left_rotate(root.left)
                return cls.__right_rotate(root)
            if balance < -1:
                if key > root.right.key:
                    return cls.__left_rotate(root)
                root.right = cls.__right_rotate(root.right)
                return cls.__left_rotate(root)

            return root

        @classmethod
        def delete(cls, root, key: int):
            """
            Deletes a key from the AVL tree and balances the tree if necessary.

            Args:
                root (BinaryTree._AVLNode): The root of the AVL tree.
                key (int): The key to delete.

            Returns:
                BinaryTree._AVLNode: The new root of the AVL tree.
            """
            if not isinstance(root, BinaryTree._AVLNode):
                raise TypeError(
                    "Root must be an instance of BinaryTree._AVLNode"
                )
            if not root:
                return root
            if key < root.key:
                root.left = cls.delete(root.left, key)
            elif key > root.key:
                root.right = cls.delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                temp = cls.__min_value_node(root.right)
                root.key = temp.key
                root.right = cls.delete(root.right, temp.key)

            root.height = 1 + max(
                cls._Get.height(root.left), cls._Get.height(root.right)
            )
            balance = cls._Get.balance(root)

            if balance > 1:
                if cls._Get.balance(root.left) >= 0:
                    return cls.__right_rotate(root)
                root.left = cls.__left_rotate(root.left)
                return cls.__right_rotate(root)
            if balance < -1:
                if cls._Get.balance(root.right) <= 0:
                    return cls.__left_rotate(root)
                root.right = cls.__right_rotate(root.right)
                return cls.__left_rotate(root)

            return root

        @classmethod
        def __rotate(cls, z, direction: str):
            """
            Rotates the subtree rooted at z in the specified direction.

            Args:
                z (BinaryTree._AVLNode): The root of the subtree to rotate.
                direction (str): The direction to rotate ('left' or 'right').

            Returns:
                BinaryTree._AVLNode: The new root of the rotated subtree.
            """
            if not isinstance(z, BinaryTree._AVLNode):
                raise TypeError("Z must be an instance of BinaryTree._AVLNode")
            y = getattr(z, direction)
            setattr(
                z,
                direction,
                getattr(y, "left" if direction == "right" else "right"),
            )
            setattr(y, "left" if direction == "right" else "right", z)
            z.height = 1 + max(cls._Get.height(z.left), cls._Get.height(z.right))
            y.height = 1 + max(cls._Get.height(y.left), cls._Get.height(y.right))
            return y

        @classmethod
        def __left_rotate(cls, z):
            """
            Performs a left rotation on the subtree rooted at z.

            Args:
                z (BinaryTree._AVLNode): The root of the subtree to rotate.

            Returns:
                BinaryTree._AVLNode: The new root of the rotated subtree.
            """
            if not isinstance(z, BinaryTree._AVLNode):
                raise TypeError("Z must be an instance of BinaryTree._AVLNode")
            return cls.__rotate(z, "right")

        @classmethod
        def __right_rotate(cls, z):
            """
            Performs a right rotation on the subtree rooted at z.

            Args:
                z (BinaryTree._AVLNode): The root of the subtree to rotate.

            Returns:
                BinaryTree._AVLNode: The new root of the rotated subtree.
            """
            if not isinstance(z, BinaryTree._AVLNode):
                raise TypeError("Z must be an instance of BinaryTree._AVLNode")
            return cls.__rotate(z, "left")

        @classmethod
        def pre_order(cls, root) -> str:
            """
            Returns a string representation of the pre-order traversal of the AVL tree.

            Args:
                root (BinaryTree._AVLNode): The root of the AVL tree.

            Returns:
                str: The pre-order traversal of the AVL tree.
            """
            if not isinstance(root, BinaryTree._AVLNode):
                raise TypeError(
                    "Root must be an instance of BinaryTree._AVLNode"
                )
            result: List[str] = []
            cls._pre_order_helper(root, result)
            return " ".join(result)

        @classmethod
        def _pre_order_helper(cls, root, result: List[str]) -> None:
            """
            Helper function for pre-order traversal.

            Args:
                root (BinaryTree._AVLNode): The root of the AVL tree.
                result (List[str]): The list to store the traversal result.
            """
            if not isinstance(root, BinaryTree._AVLNode) and root is not None:
                raise TypeError(
                    "Root must be an instance of BinaryTree._AVLNode"
                )
            if root:
                result.append(str(root.key))
                cls._pre_order_helper(root.left, result)
                cls._pre_order_helper(root.right, result)

        @classmethod
        def __min_value_node(cls, root):
            """
            Finds the node with the minimum key in the subtree rooted at root.

            Args:
                root (BinaryTree._AVLNode): The root of the subtree.

            Returns:
                BinaryTree._AVLNode: The node with the minimum key.
            """
            if not isinstance(root, BinaryTree._AVLNode):
                raise TypeError(
                    "Root must be an instance of BinaryTree._AVLNode"
                )
            while root.left:
                root = root.left
            return root

        class _Get:
            @staticmethod
            def height(root) -> int:
                """
                Returns the height of the node.

                Args:
                    root (BinaryTree._AVLNode): The node to get the height of.

                Returns:
                    int: The height of the node.
                """
                if (
                        not isinstance(root, BinaryTree._AVLNode)
                        and root is not None
                ):
                    raise TypeError(
                        "Root must be an instance of BinaryTree._AVLNode"
                    )
                return root.height if root else 0

            @classmethod
            def balance(cls, root):
                """
                Returns the balance factor of the node.

                Args:
                    root (BinaryTree._AVLNode): The node to get the balance factor of.

                Returns:
                    int: The balance factor of the node.
                """
                if not isinstance(root, BinaryTree._AVLNode):
                    raise TypeError(
                        "Root must be an instance of BinaryTree._AVLNode"
                    )
                return cls.height(root.left) - cls.height(root.right) if root else 0

    class Degenerate:
        """
        Represents a degenerate (linked list-like) binary tree.
        """

        @classmethod
        def __init__(cls) -> None:
            """
            Initializes the Degenerate tree with an empty root.
            """
            cls.root: Optional[BinaryTree._Node] = None

        @classmethod
        def insert(cls, key: int) -> None:
            """
            Inserts a key into the degenerate tree.

            Args:
                key (int): The key to insert.
            """
            if not cls.root:
                cls.root = BinaryTree._Node(key)
            else:
                current = cls.root
                while current.right:
                    current = current.right
                current.right = BinaryTree._Node(key)

        @classmethod
        def search(cls, key: int) -> bool:
            """
            Searches for a key in the degenerate tree.

            Args:
                key (int): The key to search for.

            Returns:
                bool: True if the key is found, False otherwise.
            """
            current = cls.root
            while current:
                if current.key == key:
                    return True
                current = current.right
            return False

        @classmethod
        def delete(cls, key: int) -> None:
            """
            Deletes a key from the degenerate tree.

            Args:
                key (int): The key to delete.
            """
            if not cls.root:
                return
            if cls.root.key == key:
                cls.root = cls.root.right
                return
            current = cls.root
            while current.right:
                if current.right.key == key:
                    current.right = current.right.right
                    return
                current = current.right

        @classmethod
        def traverse(cls) -> str:
            """
            Traverses the degenerate tree and returns a string representation.

            Returns:
                str: A string representation of the tree.
            """
            result: List[str] = []
            current = cls.root
            while current:
                result.append(str(current.key))
                current = current.right
            result.append("None")
            return " -> ".join(result)

    class Perfect:
        """
        Represents a perfect binary tree.
        """

        @classmethod
        def __init__(cls, height: int) -> None:
            """
            Initializes the Perfect binary tree with a given height.

            Args:
                height (int): The height of the perfect binary tree.
            """
            cls.height: int = height
            cls.nodes: List[Optional[BinaryTree._Node]] = [None] * (
                    2 ** height - 1
            )

        @classmethod
        def create(cls) -> None:
            """
            Creates the perfect binary tree.
            """
            cls.__create(0)

        @classmethod
        def __create(cls, index: int) -> None:
            """
            Recursively creates nodes for the perfect binary tree.

            Args:
                index (int): The current index in the nodes list.
            """
            if index < len(cls.nodes):
                cls.__create(2 * index + 1)
                cls.nodes[index] = BinaryTree._Node(index)
                cls.__create(2 * index + 2)

        @classmethod
        def return_tree(cls) -> str:
            """
            Returns a string representation of the perfect binary tree.

            Returns:
                str: The string representation of the tree.
            """
            levels: List[List[Optional[BinaryTree._Node]]] = []
            cls.__print_tree(0, 0, levels)
            return cls.__format_tree(levels)

        @staticmethod
        def __format_tree(levels) -> str:
            """
            Formats the levels of the tree into a string.

            Args:
                levels (list): The levels of the tree.

            Returns:
                str: The formatted string representation of the tree.
            """
            if not isinstance(levels, list) or not all(
                    isinstance(level, list) for level in levels
            ):
                raise TypeError(
                    "levels must be an instance of BinaryTree._Node"
                )
            if not levels:
                return ""
            tree_str = ""
            max_width = len(
                " ".join(str(node.value) if node else "None" for node in levels[-1])
            )
            for level in levels:
                level_str = " ".join(
                    str(node.value) if node else "None" for node in level
                )
                tree_str += level_str.center(max_width) + "\n"
            return tree_str.replace("None", " ")

        @classmethod
        def return_list(cls) -> List[Optional[int]]:
            """
            Returns a list of node values in the perfect binary tree.

            Returns:
                list[Optional[int]]: The list of node values.
            """
            return [node.value if node else None for node in cls.nodes]

        @classmethod
        def __print_tree(cls, index: int, level: int, levels) -> None:
            """
            Recursively prints the tree levels.

            Args:
                index (int): The current index in the nodes list.
                level (int): The current level in the tree.
                levels (list): The list to store the levels of the tree.
            """
            if index < len(cls.nodes):
                if len(levels) == level:
                    levels.append([])
                levels[level].append(cls.nodes[index])
                cls.__print_tree(2 * index + 1, level + 1, levels)
                cls.__print_tree(2 * index + 2, level + 1, levels)

    class RedBlackTree:
        """
        Represents a Red-Black Tree.
        """

        @classmethod
        def __init__(cls) -> None:
            """
            Initializes the Red-Black Tree with a NIL node.
            """
            cls.NIL: BinaryTree._RBNode = BinaryTree._RBNode(
                data=None, color="black"
            )
            cls.root: BinaryTree._RBNode = cls.NIL

        @classmethod
        def insert(cls, key: int) -> None:
            """
            Inserts a new node with the given key into the Red-Black Tree.

            Args:
                key (int): The key to insert.
            """
            new_node = BinaryTree._RBNode(key)
            new_node.left = cls.NIL
            new_node.right = cls.NIL
            parent: Optional[BinaryTree._RBNode] = None
            current: BinaryTree._RBNode = cls.root

            while current != cls.NIL:
                parent = current
                if new_node.data < current.data:
                    current = current.left
                else:
                    current = current.right

            new_node.parent = parent
            if not parent:
                cls.root = new_node
            elif new_node.data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

            new_node.color = "red"
            cls.insert_fixup(new_node)

        @classmethod
        def insert_fixup(cls, node) -> None:
            """
            Fixes the Red-Black Tree after insertion to maintain its properties.

            Args:
                node (BinaryTree._RBNode): The node to fix up.
            """
            if not isinstance(node, BinaryTree._RBNode):
                raise TypeError(
                    "node must be an instance of BinaryTree._RBNode"
                )
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
        def rotate(cls, node, direction: str) -> None:
            """
            Rotates the subtree rooted at the given node in the specified direction.

            Args:
                node (BinaryTree._RBNode): The root of the subtree to rotate.
                direction (str): The direction to rotate ('left' or 'right').
            """
            if not isinstance(node, BinaryTree._RBNode):
                raise TypeError(
                    "node must be an instance of BinaryTree._RBNode"
                )
            opposite = "left" if direction == "right" else "right"
            child = getattr(node, direction)
            setattr(node, direction, getattr(child, opposite))
            if getattr(child, opposite) != cls.NIL:
                getattr(child, opposite).parent = node
            child.parent = node.parent
            if not node.parent:
                cls.root = child
            elif node == getattr(node.parent, opposite):
                setattr(node.parent, opposite, child)
            else:
                setattr(node.parent, direction, child)
            setattr(child, opposite, node)
            node.parent = child

        @classmethod
        def left_rotate(cls, x) -> None:
            """
            Performs a left rotation on the subtree rooted at the given node.

            Args:
                x (BinaryTree._RBNode): The root of the subtree to rotate.
            """
            if not isinstance(x, BinaryTree._RBNode):
                raise TypeError("x must be an instance of BinaryTree._RBNode")
            cls.rotate(x, "right")

        @classmethod
        def right_rotate(cls, y) -> None:
            """
            Performs a right rotation on the subtree rooted at the given node.

            Args:
                y (BinaryTree._RBNode): The root of the subtree to rotate.
            """
            if not isinstance(y, BinaryTree._RBNode):
                raise TypeError("y must be an instance of BinaryTree._RBNode")
            cls.rotate(y, "left")

        @classmethod
        def __repr__(cls) -> str:
            """
            Returns a string representation of the Red-Black Tree.

            Returns:
                str: A string representation of the tree.
            """

            def recurse(node: BinaryTree._RBNode) -> List[Optional[int]]:
                if node == cls.NIL:
                    return []
                return recurse(node.left) + [node.data] + recurse(node.right)

            return str(recurse(cls.root))

    class BPlusTree:
        """
        Represents a B+ Tree.

        Attributes:
            root (BinaryTree._BPlusTreeNode): The root node of the B+ tree.
            t (int): The minimum degree of the B+ tree.
        """

        @classmethod
        def __init__(cls, t: int = 3) -> None:
            """
            Initializes the B+ tree with a given minimum degree.

            Args:
                t (int): The minimum degree of the B+ tree. Default is 3.
            """
            cls.root: BinaryTree._BPlusTreeNode = (
                BinaryTree._BPlusTreeNode(is_leaf=True)
            )
            cls.t: int = t

        @classmethod
        def insert(cls, key: int) -> None:
            """
            Inserts a key into the B+ tree.

            Args:
                key (int): The key to insert.
            """
            root = cls.root
            if len(root.keys) == (2 * cls.t) - 1:
                temp = BinaryTree._BPlusTreeNode()
                cls.root = temp
                temp.children.append(root)
                cls.split_child(temp, 0)
                cls.insert_non_full(temp, key)
            else:
                cls.insert_non_full(root, key)

        @classmethod
        def insert_non_full(cls, node, key: int) -> None:
            """
            Inserts a key into a non-full node of the B+ tree.

            Args:
                node (BinaryTree._BPlusTreeNode): The node to insert the key into.
                key (int): The key to insert.
            """
            if not isinstance(node, BinaryTree._BPlusTreeNode):
                raise TypeError(
                    "node must be an instance of BinaryTree._BPlusTreeNode"
                )
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
        def split_child(cls, node, i: int) -> None:
            """
            Splits a child node of the B+ tree.

            Args:
                node (BinaryTree._BPlusTreeNode): The node whose child is to be split.
                i (int): The index of the child to split.
            """
            if not isinstance(node, BinaryTree._BPlusTreeNode):
                raise TypeError(
                    "node must be an instance of BinaryTree._BPlusTreeNode"
                )
            t = cls.t
            y = node.children[i]
            z = BinaryTree._BPlusTreeNode(is_leaf=y.is_leaf)
            node.children.insert(i + 1, z)
            node.keys.insert(i, y.keys[t - 1])
            z.keys = y.keys[t: (2 * t) - 1]
            y.keys = y.keys[0: t - 1]
            if not y.is_leaf:
                z.children = y.children[t: (2 * t)]
                y.children = y.children[0:t]

        @classmethod
        def search(cls, key: int, node=None) -> bool:
            """
            Searches for a key in the B+ tree.

            Args:
                key (int): The key to search for.
                node (BinaryTree._BPlusTreeNode, optional): The node to start the search from. Defaults to None.

            Returns:
                bool: True if the key is found, False otherwise.
            """
            if (
                    not isinstance(node, BinaryTree._BPlusTreeNode)
                    and node is not None
            ):
                raise TypeError(
                    "node must be an instance of BinaryTree._BPlusTreeNode"
                )
            if not node:
                node = cls.root
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return True
            if node.is_leaf:
                return False
            return cls.search(key, node.children[i])

        @classmethod
        def traverse(cls, node=None, level: int = 0) -> List[str]:
            """
            Traverses the B+ tree and returns a list of strings representing the keys at each level.

            Args:
                node (BinaryTree._BPlusTreeNode, optional): The node to start the traversal from. Defaults to None.
                level (int): The current level in the tree. Defaults to 0.

            Returns:
                List[str]: A list of strings representing the keys at each level.
            """
            if (
                    not isinstance(node, BinaryTree._BPlusTreeNode)
                    and node is not None
            ):
                raise TypeError(
                    "node must be an instance of BinaryTree._BPlusTreeNode"
                )
            if not node:
                node = cls.root
            result = [f"Level {level}: " + " ".join(str(key) for key in node.keys)]
            if not node.is_leaf:
                for child in node.children:
                    result.extend(cls.traverse(child, level + 1))
            return result

    class SegmentTree:
        """
        Represents a Segment Tree.

        Attributes:
            n (int): The size of the input data.
            tree (List[int]): The segment tree represented as a list.
        """

        @classmethod
        def __init__(cls, data: List[int]) -> None:
            """
            Initializes the Segment Tree with the given data.

            Args:
                data (List[int]): The input data to build the segment tree from.
            """
            cls.n: int = len(data)
            cls.tree: List[int] = [0] * (2 * cls.n)
            cls.__build(data)

        @classmethod
        def __build(cls, data: List[int]) -> None:
            """
            Builds the segment tree from the given data.

            Args:
                data (List[int]): The input data to build the segment tree from.
            """
            for i in range(cls.n):
                cls.tree[cls.n + i] = data[i]
            for i in range(cls.n - 1, 0, -1):
                cls.tree[i] = cls.tree[i * 2] + cls.tree[i * 2 + 1]

        @classmethod
        def update(cls, pos: int, value: int) -> None:
            """
            Updates the value at the given position in the segment tree.

            Args:
                pos (int): The position to update.
                value (int): The new value to set.
            """
            pos += cls.n
            cls.tree[pos] = value
            while pos > 1:
                pos //= 2
                cls.tree[pos] = cls.tree[2 * pos] + cls.tree[2 * pos + 1]

        @classmethod
        def query(cls, left: int, right: int) -> int:
            """
            Queries the sum of the values in the given range [left, right] in the segment tree.

            Args:
                left (int): The left index of the range.
                right (int): The right index of the range.

            Returns:
                int: The sum of the values in the given range.
            """
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

    class Default:
        def insert(self, root, key: int):
            """
            Inserts a key into the binary tree.

            Args:
                root (BinaryTree._Node): The root node of the binary tree.
                key (int): The key to insert.

            Returns:
                BinaryTree._Node: The new root of the binary tree.
            """
            if not isinstance(root, BinaryTree._Node) and root is not None:
                raise TypeError("root must be an instance of BinaryTree._Node")
            if root is None:
                return BinaryTree._Node(key)
            if key < root.value:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
            return root

        def inorder_traversal(self, root, sorted_list: List[int]) -> None:
            """
            Performs an inorder traversal of the binary tree and appends the values to the sorted list.

            Args:
                root (BinaryTree._Node): The root node of the binary tree.
                sorted_list (List[int]): The list to append the values to.
            """
            if not isinstance(root, BinaryTree._Node) and root is not None:
                raise TypeError("root must be an instance of BinaryTree._Node")
            if root:
                self.inorder_traversal(root.left, sorted_list)
                sorted_list.append(root.value)
                self.inorder_traversal(root.right, sorted_list)

        def tree_sort(self, arr: List[int]) -> List[int]:
            """
            Sorts a list of integers using the tree sort algorithm.

            Args:
                arr (List[int]): The list of integers to sort.

            Returns:
                List[int]: The sorted list of integers.
            """
            if not arr:
                return arr
            root = BinaryTree._Node(arr[0])
            for value in arr[1:]:
                self.insert(root, value)
            sorted_list: List[int] = []
            self.inorder_traversal(root, sorted_list)
            return sorted_list
