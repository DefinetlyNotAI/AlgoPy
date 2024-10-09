import unittest
from sort import Sort


class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.BubbleSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bubble_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.BubbleSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_bubble_sort_with_flag_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.BubbleSort.with_flag(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bubble_sort_with_flag_empty_list(self):
        arr = []
        sorted_arr = Sort.BubbleSort.with_flag(arr)
        self.assertEqual(sorted_arr, [])

    def test_quick_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.QuickSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_quick_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.QuickSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_merge_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.MergeSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_merge_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.MergeSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_bogo_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.BogoSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bogo_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.BogoSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_selection_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_selection_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.selection_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_insertion_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.insertion_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_insertion_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.insertion_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_heap_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.heap_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_heap_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.heap_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_radix_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.radix_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_radix_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.radix_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_counting_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.counting_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_counting_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.counting_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_bucket_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.bucket_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bucket_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.bucket_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_shell_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.shell_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_shell_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.shell_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_cocktail_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.cocktail_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_cocktail_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.cocktail_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_comb_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.comb_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_comb_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.comb_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_gnome_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.gnome_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_gnome_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.gnome_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_pancake_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.pancake_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_pancake_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.pancake_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_stooge_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.stooge_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_stooge_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.stooge_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_cycle_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.cycle_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_cycle_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.cycle_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_library_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.library_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_library_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.library_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_strand_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.strand_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_strand_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.strand_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_tim_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.tim_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_tim_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.tim_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_block_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.block_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_block_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.block_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_tournament_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.tournament_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_tournament_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.tournament_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_intro_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.intro_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_intro_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.intro_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_un_shuffle_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.un_shuffle_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_un_shuffle_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.un_shuffle_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_sleep_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.sleep_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_sleep_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.sleep_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_stupid_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.stupid_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_stupid_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.stupid_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_slow_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.slow_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_slow_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.slow_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_odd_even_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.odd_even_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_odd_even_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.odd_even_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_bingo_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.bingo_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bingo_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.bingo_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_pigeonhole_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = Sort.pigeonhole_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_pigeonhole_sort_empty_list(self):
        arr = []
        sorted_arr = Sort.pigeonhole_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_tag_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr, original_indices = Sort.tag_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(original_indices, [4, 6, 5, 0, 1, 2, 3])

    def test_tag_sort_empty_list(self):
        arr = []
        sorted_arr, original_indices = Sort.tag_sort(arr)
        self.assertEqual(sorted_arr, [])
        self.assertEqual(original_indices, [])


class TestSortingAlgorithmsTournament(unittest.TestCase):
    def tournament_sort_sorts_correctly(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_data = Sort.Tournament.tournament_sort(data)
        self.assertEqual(sorted_data, [9])

    def tournament_sort_empty_list(self):
        data = []
        sorted_data = Sort.Tournament.tournament_sort(data)
        self.assertEqual(sorted_data, [])

    def tournament_sort_single_element(self):
        data = [42]
        sorted_data = Sort.Tournament.tournament_sort(data)
        self.assertEqual(sorted_data, [42])

    def tournament_sort_all_equal_elements(self):
        data = [7, 7, 7, 7, 7]
        sorted_data = Sort.Tournament.tournament_sort(data)
        self.assertEqual(sorted_data, [7])


class TestBinaryTree(unittest.TestCase):
    def test_avl_insert_balances_tree(self):
        root = None
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            root = Sort.BinaryTree.AVL.insert(root, key)
        self.assertEqual(Sort.BinaryTree.AVL.pre_order(root), "30 20 10 25 40 50")

    def test_avl_delete_balances_tree(self):
        root = None
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            root = Sort.BinaryTree.AVL.insert(root, key)
        root = Sort.BinaryTree.AVL.delete(root, 40)
        self.assertEqual(Sort.BinaryTree.AVL.pre_order(root), "30 20 10 25 50")

    def test_degenerate_tree_inserts_correctly(self):
        tree = Sort.BinaryTree.Degenerate()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        self.assertEqual(tree.traverse(), "10 -> 20 -> 30 -> 40 -> 50 -> 25 -> None")

    def test_degenerate_tree_deletes_correctly(self):
        tree = Sort.BinaryTree.Degenerate()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        tree.delete(30)
        self.assertEqual(tree.traverse(), "10 -> 20 -> 40 -> 50 -> 25 -> None")

    def test_perfect_tree_creates_correctly(self):
        tree = Sort.BinaryTree.Perfect(3)
        tree.create()
        self.assertEqual(tree.return_list(), [0, 1, 2, 3, 4, 5, 6])

    def test_red_black_tree_inserts_correctly(self):
        tree = Sort.BinaryTree.RedBlackTree()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        self.assertEqual(str(tree), "[10, 20, 25, 30, 40, 50]")

    def test_bplus_tree_inserts_correctly(self):
        tree = Sort.BinaryTree.BPlusTree(t=3)
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            tree.insert(key)
        self.assertTrue(tree.search(6))
        self.assertFalse(tree.search(15))

    def test_bplus_tree_traverses_correctly(self):
        tree = Sort.BinaryTree.BPlusTree(t=3)
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
        tree = Sort.BinaryTree.SegmentTree(data)
        self.assertEqual(tree.tree[tree.n:], data)

    def test_segment_tree_updates_correctly(self):
        data = [1, 3, 5, 7, 9, 11]
        tree = Sort.BinaryTree.SegmentTree(data)
        tree.update(1, 10)
        self.assertEqual(tree.query(1, 1), 10)

    def test_segment_tree_queries_correctly(self):
        data = [1, 3, 5, 7, 9, 11]
        tree = Sort.BinaryTree.SegmentTree(data)
        self.assertEqual(tree.query(1, 3), 15)

    def test_default_tree_inserts_correctly(self):
        tree = Sort.BinaryTree.Default()
        root = None
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            root = tree.insert(root, key)
        sorted_list = []
        tree.inorder_traversal(root, sorted_list)
        self.assertEqual(sorted_list, [5, 6, 7, 10, 12, 17, 20, 30])

    def test_default_tree_sorts_correctly(self):
        tree = Sort.BinaryTree.Default()
        arr = [10, 20, 5, 6, 12, 30, 7, 17]
        sorted_arr = tree.tree_sort(arr)
        self.assertEqual(sorted_arr, [5, 6, 7, 10, 12, 17, 20, 30])
