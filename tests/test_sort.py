import unittest

from algopy import sort


class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.BubbleSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bubble_sort_empty_list(self):
        arr = []
        sorted_arr = sort.BubbleSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_bubble_sort_with_flag_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.BubbleSort.with_flag(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bubble_sort_with_flag_empty_list(self):
        arr = []
        sorted_arr = sort.BubbleSort.with_flag(arr)
        self.assertEqual(sorted_arr, [])

    def test_quick_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.QuickSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_quick_sort_empty_list(self):
        arr = []
        sorted_arr = sort.QuickSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_merge_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.MergeSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_merge_sort_empty_list(self):
        arr = []
        sorted_arr = sort.MergeSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_bogo_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.BogoSort.default(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bogo_sort_empty_list(self):
        arr = []
        sorted_arr = sort.BogoSort.default(arr)
        self.assertEqual(sorted_arr, [])

    def test_selection_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_selection_sort_empty_list(self):
        arr = []
        sorted_arr = sort.selection_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_insertion_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.insertion_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_insertion_sort_empty_list(self):
        arr = []
        sorted_arr = sort.insertion_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_heap_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.heap_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_heap_sort_empty_list(self):
        arr = []
        sorted_arr = sort.heap_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_radix_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.radix_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_radix_sort_empty_list(self):
        arr = []
        sorted_arr = sort.radix_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_counting_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.counting_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_counting_sort_empty_list(self):
        arr = []
        sorted_arr = sort.counting_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_bucket_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.bucket_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bucket_sort_empty_list(self):
        arr = []
        sorted_arr = sort.bucket_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_shell_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.shell_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_shell_sort_empty_list(self):
        arr = []
        sorted_arr = sort.shell_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_cocktail_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.cocktail_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_cocktail_sort_empty_list(self):
        arr = []
        sorted_arr = sort.cocktail_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_comb_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.comb_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_comb_sort_empty_list(self):
        arr = []
        sorted_arr = sort.comb_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_gnome_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.gnome_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_gnome_sort_empty_list(self):
        arr = []
        sorted_arr = sort.gnome_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_pancake_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.pancake_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_pancake_sort_empty_list(self):
        arr = []
        sorted_arr = sort.pancake_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_stooge_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.stooge_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_stooge_sort_empty_list(self):
        arr = []
        sorted_arr = sort.stooge_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_cycle_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.cycle_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_cycle_sort_empty_list(self):
        arr = []
        sorted_arr = sort.cycle_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_library_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.library_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_library_sort_empty_list(self):
        arr = []
        sorted_arr = sort.library_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_strand_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.strand_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_strand_sort_empty_list(self):
        arr = []
        sorted_arr = sort.strand_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_tim_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.tim_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_tim_sort_empty_list(self):
        arr = []
        sorted_arr = sort.tim_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_block_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.block_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_block_sort_empty_list(self):
        arr = []
        sorted_arr = sort.block_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_tournament_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.tournament_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_tournament_sort_empty_list(self):
        arr = []
        sorted_arr = sort.tournament_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_intro_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.intro_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_intro_sort_empty_list(self):
        arr = []
        sorted_arr = sort.intro_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_un_shuffle_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.un_shuffle_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_un_shuffle_sort_empty_list(self):
        arr = []
        sorted_arr = sort.un_shuffle_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_sleep_sort_sorts_correctly(self):
        arr = [3, 6, 1, 2, 1]
        sorted_arr = sort.sleep_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6])

    def test_sleep_sort_empty_list(self):
        arr = []
        sorted_arr = sort.sleep_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_stupid_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.stupid_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_stupid_sort_empty_list(self):
        arr = []
        sorted_arr = sort.stupid_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_slow_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.slow_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_slow_sort_empty_list(self):
        arr = []
        sorted_arr = sort.slow_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_odd_even_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.odd_even_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_odd_even_sort_empty_list(self):
        arr = []
        sorted_arr = sort.odd_even_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_bingo_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.bingo_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_bingo_sort_empty_list(self):
        arr = []
        sorted_arr = sort.bingo_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_pigeonhole_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = sort.pigeonhole_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_pigeonhole_sort_empty_list(self):
        arr = []
        sorted_arr = sort.pigeonhole_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_tag_sort_sorts_correctly(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr, original_indices = sort.tag_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(original_indices, [4, 6, 5, 0, 1, 2, 3])

    def test_tag_sort_empty_list(self):
        arr = []
        sorted_arr, original_indices = sort.tag_sort(arr)
        self.assertEqual(sorted_arr, [])
        self.assertEqual(original_indices, [])


class TestBinaryTree(unittest.TestCase):
    def test_avl_insert_balances_tree(self):
        root = None
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            root = sort.BinaryTree.AVL.insert(root, key)
        self.assertEqual(sort.BinaryTree.AVL.pre_order(root), "30 20 10 25 40 50")

    def test_avl_delete_balances_tree(self):
        root = None
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            root = sort.BinaryTree.AVL.insert(root, key)
        root = sort.BinaryTree.AVL.delete(root, 40)
        self.assertEqual(sort.BinaryTree.AVL.pre_order(root), "30 20 10 25 50")

    def test_degenerate_tree_inserts_correctly(self):
        tree = sort.BinaryTree.Degenerate()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        self.assertEqual(tree.traverse(), "10 -> 20 -> 30 -> 40 -> 50 -> 25 -> None")

    def test_degenerate_tree_deletes_correctly(self):
        tree = sort.BinaryTree.Degenerate()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        tree.delete(30)
        self.assertEqual(tree.traverse(), "10 -> 20 -> 40 -> 50 -> 25 -> None")

    def test_perfect_tree_creates_correctly(self):
        tree = sort.BinaryTree.Perfect(3)
        tree.create()
        self.assertEqual(tree.return_list(), [0, 1, 2, 3, 4, 5, 6])

    def test_red_black_tree_inserts_correctly(self):
        tree = sort.BinaryTree.RedBlackTree()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            tree.insert(key)
        self.assertEqual(str(tree), "[10, 20, 25, 30, 40, 50]")

    def test_bplus_tree_inserts_correctly(self):
        tree = sort.BinaryTree.BPlusTree(t=3)
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            tree.insert(key)
        self.assertTrue(tree.search(6))
        self.assertFalse(tree.search(15))

    def test_bplus_tree_traverses_correctly(self):
        tree = sort.BinaryTree.BPlusTree(t=3)
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
        tree = sort.BinaryTree.SegmentTree(data)
        self.assertEqual(tree.tree[tree.n:], data)

    def test_segment_tree_updates_correctly(self):
        data = [1, 3, 5, 7, 9, 11]
        tree = sort.BinaryTree.SegmentTree(data)
        tree.update(1, 10)
        self.assertEqual(tree.query(1, 1), 10)

    def test_segment_tree_queries_correctly(self):
        data = [1, 3, 5, 7, 9, 11]
        tree = sort.BinaryTree.SegmentTree(data)
        self.assertEqual(tree.query(1, 3), 15)

    def test_default_tree_inserts_correctly(self):
        tree = sort.BinaryTree.Default()
        root = None
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            root = tree.insert(root, key)
        sorted_list = []
        tree.inorder_traversal(root, sorted_list)
        self.assertEqual(sorted_list, [5, 6, 7, 10, 12, 17, 20, 30])

    def test_default_tree_sorts_correctly(self):
        tree = sort.BinaryTree.Default()
        arr = [10, 20, 5, 6, 12, 30, 7, 17]
        sorted_arr = tree.tree_sort(arr)
        self.assertEqual(sorted_arr, [5, 6, 7, 10, 12, 17, 20, 30])


class TestsortingString(unittest.TestCase):
    # Default String sort
    def test_alphabetically_sorts_correctly(self):
        arr = ["banana", "apple", "cherry"]
        sorted_arr = sort.String.alphabetically(arr)
        self.assertEqual(sorted_arr, ["apple", "banana", "cherry"])

    def test_alphabetically_sorts_reverse_correctly(self):
        arr = ["banana", "apple", "cherry"]
        sorted_arr = sort.String.alphabetically(arr, reverse=True)
        self.assertEqual(sorted_arr, ["cherry", "banana", "apple"])

    def test_alphabetically_handles_empty_list(self):
        arr = []
        sorted_arr = sort.String.alphabetically(arr)
        self.assertEqual(sorted_arr, [])

    # Empty Splits
    def test_split_empty(self):
        arr = []
        sorted_arr = sort.String.and_integer(arr)
        self.assertEqual(sorted_arr, ([], []))

    # Default Splits
    def test_split_strings_only_sorted(self):
        arr = ["banana", "apple", "cherry"]
        sorted_arr = sort.String.and_integer(arr)
        self.assertEqual(sorted_arr, ([], ["apple", "banana", "cherry"]))

    def test_split_integers_strings_sorted(self):
        arr = [1, 2, "banana", "apple", "cherry", 3]
        sorted_arr = sort.String.and_integer(arr)
        self.assertEqual(sorted_arr, ([1, 2, 3], ["apple", "banana", "cherry"]))

    def test_split_integers_only_sorted(self):
        arr = [1, 2, 3]
        sorted_arr = sort.String.and_integer(arr)
        self.assertEqual(sorted_arr, ([1, 2, 3], []))

    # Reverse Splits
    def test_split_strings_only_reverse_sorted(self):
        arr = ["banana", "apple", "cherry"]
        sorted_arr = sort.String.and_integer(arr, reverse=True)
        self.assertEqual(sorted_arr, ([], ["cherry", "banana", "apple"]))

    def test_split_integers_strings_reverse_sorted(self):
        arr = [1, 2, "banana", "apple", "cherry", 3]
        sorted_arr = sort.String.and_integer(arr, reverse=True)
        self.assertEqual(sorted_arr, ([3, 2, 1], ["cherry", "banana", "apple"]))

    def test_split_integers_only_reverse_sorted(self):
        arr = [1, 2, 3]
        sorted_arr = sort.String.and_integer(arr, reverse=True)
        self.assertEqual(sorted_arr, ([3, 2, 1], []))

    # Default No_String_sort Splits
    def test_split_strings_only_unsorted(self):
        arr = ["banana", "apple", "cherry"]
        sorted_arr = sort.String.and_integer(arr, sort_strings=False)
        self.assertEqual(sorted_arr, ([], ["banana", "apple", "cherry"]))

    def test_split_integers_strings_sorted_only_integers(self):
        arr = [1, 2, "banana", "apple", "cherry", 3]
        sorted_arr = sort.String.and_integer(arr, sort_strings=False)
        self.assertEqual(sorted_arr, ([1, 2, 3], ["banana", "apple", "cherry"]))

    # Reverse No_String_sort Splits
    def test_split_strings_only_reverse_unsorted(self):
        arr = ["banana", "apple", "cherry"]
        sorted_arr = sort.String.and_integer(arr, reverse=True, sort_strings=False)
        self.assertEqual(sorted_arr, ([], ["cherry", "apple", "banana"]))

    def test_split_integers_strings_reverse_sorted_only_integers(self):
        arr = [1, 2, "banana", "apple", "cherry", 3]
        sorted_arr = sort.String.and_integer(arr, reverse=True, sort_strings=False)
        self.assertEqual(sorted_arr, ([3, 2, 1], ["cherry", "apple", "banana"]))

    # Default No_Int_sort Splits
    def test_split_integers_only_unsorted(self):
        arr = [3, 1, 2]
        sorted_arr = sort.String.and_integer(arr, sort_integers=False)
        self.assertEqual(sorted_arr, ([3, 1, 2], []))

    def test_split_integers_strings_sorted_only_strings(self):
        arr = [3, 2, "banana", "apple", "cherry", 1]
        sorted_arr = sort.String.and_integer(arr, sort_integers=False)
        self.assertEqual(sorted_arr, ([3, 2, 1], ["apple", "banana", "cherry"]))

    # Reverse No_Int_sort Splits
    def test_split_integers_only_reverse_unsorted(self):
        arr = [3, 1, 2]
        sorted_arr = sort.String.and_integer(arr, reverse=True, sort_integers=False)
        self.assertEqual(sorted_arr, ([2, 1, 3], []))

    def test_split_integers_strings_reverse_sorted_only_strings(self):
        arr = [1, 3, "banana", "apple", "cherry", 2]
        sorted_arr = sort.String.and_integer(arr, reverse=True, sort_integers=False)
        self.assertEqual(sorted_arr, ([2, 3, 1], ["cherry", "banana", "apple"]))

    # Default No sort Splits
    def test_split_integers_strings_no_sort(self):
        arr = [3, 2, "banana", "apple", "cherry", 1]
        sorted_arr = sort.String.and_integer(
            arr, sort_integers=False, sort_strings=False
        )
        self.assertEqual(sorted_arr, ([3, 2, 1], ["banana", "apple", "cherry"]))

    # Reverse No sort Splits
    def test_split_integers_strings_reverse_no_sort(self):
        arr = [1, 3, "banana", "apple", "cherry", 2]
        sorted_arr = sort.String.and_integer(
            arr, reverse=True, sort_integers=False, sort_strings=False
        )
        self.assertEqual(sorted_arr, ([2, 3, 1], ["cherry", "apple", "banana"]))
