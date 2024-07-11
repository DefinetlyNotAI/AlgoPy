"""
Handles both integers and floats seamlessly, converting between types as needed.
Gracefully ignores non-numeric elements without crashing, enhancing reliability.
Interactive input method allows for easy testing and experimentation.
Sorts lists efficiently and finds largest/smallest elements with minimal overhead.
Finds the number of vowels in a word.
Either totally, or by vowel.
Includes special words that have y as either an active vowel or as a passive vowel.

TIME COMPLEXITY = O(n / log n ) [Find.largest] [Find.smallest]
TIME COMPLEXITY = O(m*n) [Find.total_vowels] [Find.every_vowel]
TIME COMPLEXITY = O(n) [Find.value_index]

SPACE COMPLEXITY = O(n) [Find.largest] [Find.smallest]
SPACE COMPLEXITY = O(1) [Find.value_index] [Find.total_vowels] [Find.every_vowel]
"""

# Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life


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

    def __sort(self, List):
        if List is None:
            List = self.__input_list()

        try:
            converted_list = sorted(
                float(item) for item in List if isinstance(item, (int, float))
            )
            final_list = [
                int(item) if item.is_integer() else item for item in converted_list
            ]
            return final_list
        except ValueError:
            return None

    @staticmethod
    def __input_list():
        List = []
        while True:
            try:
                nAmountNos = int(input("How many numbers: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        for _ in range(nAmountNos):
            while True:
                try:
                    nNo = float(input("Give me a number: "))
                    List.append(nNo)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        return List

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

    @staticmethod
    def __value_index(array, Word):
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == Word:
                return True  # Return True if the value matches
        return False  # Return False if the value was not found in the list

    def largest(self, List=None):
        largeList = self.__sort(List)

        if largeList is None:
            raise ValueError("List contains non-integer elements.")

        return largeList[-1] if largeList else None

    def smallest(self, List=None):
        smallList = self.__sort(List)

        if smallList is None:
            raise ValueError("List contains non-integer elements.")

        return smallList[0] if smallList else None

    def total_vowels(self, Word=None):
        if Word is None:
            Word = input("Enter a word: ")
        vowels = self.__vowel_y(Word)
        vowel_count = sum(1 for char in Word if char in vowels)
        return vowel_count

    def every_vowel(self, Word=None):
        if Word is None:
            Word = input("Enter a word: ")
        result = ""
        vowels = self.__vowel_y(Word, True)
        for vowel in vowels:
            result += self.__count_character(Word, vowel) + "\n"
        return result.rstrip("\n")

    @staticmethod
    def value_index(array, value_to_find):
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == value_to_find:
                return index  # Return the index if the value matches
        return False  # Return False if the value was not found in the list


"""
# Example Setup
find = Find()

# Example List
list_place = [17, 5.0, "hi", 65.03, 32.0, -4, -5.8]

# Example Usage
print(find.largest(list_place))
print(find.smallest(list_place))
print(find.value_index(list_place, 32.0))
print(find.every_vowel("Hola"))
print(find.total_vowels("Hola"))
"""
