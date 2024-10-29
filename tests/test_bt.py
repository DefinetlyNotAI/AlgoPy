import unittest

from algopy import bt


class TestBinaryTree(unittest.TestCase):
    def test_avl_insert_balances_tree(self):
        root = None
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            root = bt.AVL.insert(root, key)
        self.assertEqual(bt.AVL.pre_order(root), "30 20 10 25 40 50")

    def test_avl_delete_balances_tree(self):
        root = None
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            root = bt.AVL.insert(root, key)
        root = bt.AVL.delete(root, 40)
        self.assertEqual(bt.AVL.pre_order(root), "30 20 10 25 50")

    def test_degenerate_tree_inserts_correctly(self):
        tree = bt.Degenerate()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        self.assertEqual(tree.traverse(), "10 -> 20 -> 30 -> 40 -> 50 -> 25 -> None")

    def test_degenerate_tree_deletes_correctly(self):
        tree = bt.Degenerate()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        tree.delete(30)
        self.assertEqual(tree.traverse(), "10 -> 20 -> 40 -> 50 -> 25 -> None")

    def test_perfect_tree_creates_correctly(self):
        tree = bt.Perfect(3)
        tree.create()
        self.assertEqual(tree.return_list(), [0, 1, 2, 3, 4, 5, 6])

    def test_red_black_tree_inserts_correctly(self):
        tree = bt.RedBlackTree()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        self.assertEqual(str(tree), "[10, 20, 25, 30, 40, 50]")

    def test_bplus_tree_inserts_correctly(self):
        tree = bt.BPlusTree(t=3)
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            tree.insert(key)
        self.assertTrue(tree.search(6))
        self.assertFalse(tree.search(15))

    def test_bplus_tree_traverses_correctly(self):
        tree = bt.BPlusTree(t=3)
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            tree.insert(key)
        expected_traversal = [
            "Level 0: 10",
            "Level 1: 5 6 7",
            "Level 1: 12 17 20 30",
        ]
        self.assertEqual(tree.traverse(), expected_traversal)

    def test_segment_tree_builds_correctly(self):
        data = [1, 3, 5, 7, 9, 11]
        tree = bt.SegmentTree(data)
        self.assertEqual(tree.tree[tree.n:], data)

    def test_segment_tree_updates_correctly(self):
        data = [1, 3, 5, 7, 9, 11]
        tree = bt.SegmentTree(data)
        tree.update(1, 10)
        self.assertEqual(tree.query(1, 1), 10)

    def test_segment_tree_queries_correctly(self):
        data = [1, 3, 5, 7, 9, 11]
        tree = bt.SegmentTree(data)
        self.assertEqual(tree.query(1, 3), 15)

    def test_default_tree_inserts_correctly(self):
        tree = bt.Default()
        root = None
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            root = tree.insert(root, key)
        bted_list = []
        tree.inorder_traversal(root, bted_list)
        self.assertEqual(bted_list, [5, 6, 7, 10, 12, 17, 20, 30])

    def test_default_tree_bts_correctly(self):
        tree = bt.Default()
        arr = [10, 20, 5, 6, 12, 30, 7, 17]
        bted_arr = tree.tree_sort(arr)
        self.assertEqual(bted_arr, [5, 6, 7, 10, 12, 17, 20, 30])
