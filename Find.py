

# Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life


class Find:
    def __init__(self):
        """
        Words that have y as either an active vowel or as a passive vowel
        """
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
        """
        Sorts a list of numbers, converting them to floats if needed. Returns the sorted list.
        """
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
        """
        Prompts the user to input a list of numbers.

        Returns:
            List[float]: The list of numbers entered by the user.

        Raises:
            ValueError: If the user enters an invalid input for the number of numbers or for each individual number.
        """
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
        """
        Determines the vowels in a given string, taking into account special cases for the letter 'y'.

        Parameters:
            string (str): The input string.
            only_lowercase (bool, optional): Whether to consider only lowercase vowels. Defaults to False.

        Returns:
            str: The vowels present in the string, taking into account special cases for 'y'.
        """
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
        """
        Counts the occurrences of a given character in a word.

        Parameters:
            Word (str): The word to search for the character.
            Vowel (str): The character to count.

        Returns:
            str: A string containing the character and its count.
        """
        # Counter
        count = 0

        # For loop to find length of word
        for i in range(len(Word)):
            if Word[i] == Vowel:
                count += 1

        return f"{Vowel} {count}"

    @staticmethod
    def __value_index(array, Word):
        """
        Check if a given value exists in an array.

        Parameters:
            array (list): The array to search in.
            Word (Any): The value to search for.

        Returns:
            bool: True if the value is found in the array, False otherwise.
        """
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == Word:
                return True  # Return True if the value matches
        return False  # Return False if the value was not found in the list

    def largest(self, List=None):
        """
        Sorts a list of integers and returns the largest element from the list.

        Parameters:
            List (list): List of integers to find the largest element from.

        Returns:
            int or None: The largest element from the list if it contains only integers, None otherwise.
        """
        largeList = self.__sort(List)

        if largeList is None:
            raise ValueError("List contains non-integer elements.")

        return largeList[-1] if largeList else None

    def smallest(self, List=None):
        """
        Find the smallest element in a list of integers.

        Parameters:
            List (list, optional): The list of integers to find the smallest element from. Defaults to None.

        Returns:
            int or None: The smallest element from the list if it contains only integers, None otherwise.

        Raises:
            ValueError: If the list contains non-integer elements.
        """
        smallList = self.__sort(List)

        if smallList is None:
            raise ValueError("List contains non-integer elements.")

        return smallList[0] if smallList else None

    def total_vowels(self, Word=None):
        """
        Find the total number of vowels in a given word.

        Parameters:
            Word (str, optional): The input word to count vowels from. Defaults to None.

        Returns:
            int: The total count of vowels in the input word.
        """
        if Word is None:
            Word = input("Enter a word: ")
        vowels = self.__vowel_y(Word)
        vowel_count = sum(1 for char in Word if char in vowels)
        return vowel_count

    def every_vowel(self, Word=None):
        """
        Find the total number of vowels in a given word.

        Parameters:
            Word (str, optional): The input word to count vowels from. Defaults to None.

        Returns:
            int: The total count of vowels in the input word.
        """
        if Word is None:
            Word = input("Enter a word: ")
        result = ""
        vowels = self.__vowel_y(Word, True)
        for vowel in vowels:
            result += self.__count_character(Word, vowel) + "\n"
        return result.rstrip("\n")

    @staticmethod
    def value_index(array, value_to_find):
        """
        A function to find the index of a specific value in an array.

        Parameters:
            array (list): The array to search in.
            value_to_find (Any): The value to search for.

        Returns:
            int or bool: The index of the value in the array if found, False otherwise.
        """
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
