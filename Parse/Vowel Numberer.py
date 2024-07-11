r"""
Finds the number of vowels in a word.

Either totally, or by vowel.

Includes special words that have y as either an active vowel or as a passive vowel.

COMPLEXITY = O(m*n) [total_vowels] [every_vowel]

SPACE COMPLEXITY = O(1) [total_vowels] [every_vowel]
"""


class Find:
    def __init__(self):
        # Words that have y as either an active vowel or as a passive vowel
        self.special_y_words = [
            "Cry",
            "Dry",
            "Gym",
            "Hymn",
            "Lynx",
            "Myth",
            "Pry",
            "Rhythm",
            "Shy",
            "Spy",
            "Spry",
            "Sync",
            "Try",
            "Why",
            "City",
            "Party",
            "Fly",
            "Shy",
            "Wary",
            "Worthwhile",
            "Type",
            "Typical",
            "Thyme",
            "Cyst",
            "Symbol",
            "System",
            "Lady",
            "Pretty",
            "Very",
            "Deny",
            "Daddy",
            "Quickly",
        ]

    def __vowel_y(self, string, only_lowercase=False):
        if self.__value_index(self.special_y_words, string):
            if only_lowercase:
                vowels = "aeiouy"
            else:
                vowels = "aeiouyAEIOUY"
        else:
            if only_lowercase:
                vowels = "aeiou"
            else:
                vowels = "aeiouAEIOU"
        return vowels

    @staticmethod
    def __count_character(Word, Vowel):
        # Counter
        count = 0

        # For loop to find length of word
        for i in range(len(Word)):
            if Word[i] == Vowel:
                count += 1

        return f"{Vowel} {count}"

    def every_vowel(self, Word=None):
        if Word is None:
            Word = input("Enter a word: ")
        result = ""
        vowels = self.__vowel_y(Word, True)
        for vowel in vowels:
            result += self.__count_character(Word, vowel) + "\n"
        return result.rstrip("\n")

    @staticmethod
    def __value_index(array, Word):
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == Word:
                return True  # Return True if the value matches
        return False  # Return False if the value was not found in the list

    def total_vowels(self, Word=None):
        if Word is None:
            Word = input("Enter a word: ")
        vowels = self.__vowel_y(Word)
        vowel_count = sum(1 for char in Word if char in vowels)
        return vowel_count


# Forever loop and basic input system
find = Find()

