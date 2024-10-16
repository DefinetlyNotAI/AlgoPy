import unittest

from algopy import find


class TestFind(unittest.TestCase):
    def test_largest_number_in_array(self):
        self.assertEqual(find.InArray.largest_number([1, 2, 3, 4, 5]), 5)

    def test_largest_number_in_empty_array(self):
        self.assertIsNone(find.InArray.largest_number([]))

    def test_largest_number_in_none_array(self):
        with self.assertRaises(Exception):
            find.InArray.largest_number(None)

    def test_smallest_number_in_array(self):
        self.assertEqual(find.InArray.smallest_number([1, 2, 3, 4, 5]), 1)

    def test_smallest_number_in_empty_array(self):
        self.assertIsNone(find.InArray.smallest_number([]))

    def test_smallest_number_in_none_array(self):
        with self.assertRaises(Exception):
            find.InArray.smallest_number(None)

    def test_index_all_occurrences(self):
        self.assertEqual(find.InArray.Objects.index_all([1, 2, 3, 2, 4], 2), [1, 3])

    def test_index_all_occurrences_not_found(self):
        self.assertEqual(find.InArray.Objects.index_all([1, 2, 3, 4], 5), [])

    def test_index_all_occurrences_none_input(self):
        with self.assertRaises(Exception):
            find.InArray.Objects.index_all(None, 2)

    def test_index_first_occurrence(self):
        self.assertEqual(find.InArray.Objects.index([1, 2, 3, 2, 4], 2), 1)

    def test_index_first_occurrence_not_found(self):
        self.assertFalse(find.InArray.Objects.index([1, 2, 3, 4], 5))

    def test_index_first_occurrence_none_input(self):
        with self.assertRaises(Exception):
            find.InArray.Objects.index(None, 2)

    def test_longest_word_in_sentence(self):
        self.assertEqual(find.InSentence.longest_word("The quick brown fox"), "quick")

    def test_longest_word_in_empty_sentence(self):
        self.assertEqual(find.InSentence.longest_word(""), "")

    def test_longest_word_in_none_sentence(self):
        with self.assertRaises(Exception):
            find.InSentence.longest_word(None)

    def test_shortest_word_in_sentence(self):
        self.assertEqual(find.InSentence.shortest_word("The quick brown fox"), "The")

    def test_shortest_word_in_empty_sentence(self):
        self.assertEqual(find.InSentence.shortest_word(""), "")

    def test_shortest_word_in_none_sentence(self):
        with self.assertRaises(Exception):
            find.InSentence.shortest_word(None)

    def test_word_exists_in_sentence(self):
        self.assertTrue(find.InSentence.Word.exists("The quick brown fox", "quick"))

    def test_word_does_not_exist_in_sentence(self):
        self.assertFalse(find.InSentence.Word.exists("The quick brown fox", "slow"))

    def test_word_exists_in_none_sentence(self):
        with self.assertRaises(Exception):
            find.InSentence.Word.exists(None, "quick")

    def test_count_word_occurrences(self):
        self.assertEqual(
            find.InSentence.Word.occurrences("The quick brown fox", "the"), 1
        )

    def test_count_word_occurrences_none_input(self):
        with self.assertRaises(Exception):
            find.InSentence.Word.occurrences(None, "the")

    def test_total_vowels_in_word(self):
        self.assertEqual(find.InWord.total_vowels("hello"), 2)

    def test_total_vowels_in_none_word(self):
        with self.assertRaises(Exception):
            find.InWord.total_vowels(None)


if __name__ == "__main__":
    unittest.main()
