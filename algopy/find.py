class Find:
    class InArray:
        @staticmethod
        def __sort(List: list) -> list[int | float]:
            """
            Sort a list of integers and floats.

            :param List: The list to sort.
            :return: A sorted list of integers and floats.
            :raises Exception: If the input list is None.
            """
            if List is None:
                raise Exception("No input given.")
            converted_list = sorted(
                float(item) for item in List if isinstance(item, (int, float))
            )
            return [int(item) if item.is_integer() else item for item in converted_list]

        @classmethod
        def largest_number(cls, List: list[int | float]) -> int | float:
            """
            Find the largest number in a list of integers and floats.

            :param List: The list to search.
            :return: The largest number in the list.
            :raises Exception: If the input list is None.
            """
            if List is None:
                raise Exception("No input given.")
            sorted_list = cls.__sort(List)
            return sorted_list[-1] if sorted_list else None

        @classmethod
        def smallest_number(cls, List: list[int | float]) -> int | float:
            """
            Find the smallest number in a list of integers and floats.

            :param List: The list to search.
            :return: The smallest number in the list.
            :raises Exception: If the input list is None.
            """
            if List is None:
                raise Exception("No input given.")
            sorted_list = cls.__sort(List)
            return sorted_list[0] if sorted_list else None

        class Objects:
            @staticmethod
            def index_all(List: list, value_to_find: any) -> list[int]:
                """
                Find all indices of a value in a list.

                :param List: The list to search.
                :param value_to_find: The value to find.
                :return: A list of indices where the value is found.
                :raises Exception: If the input list or value is None.
                """
                if List is None or value_to_find is None:
                    raise Exception("No input given.")
                return [
                    index for index, value in enumerate(List) if value == value_to_find
                ]

            @staticmethod
            def index(List: list, value_to_find: any) -> int | bool:
                """
                Find the first index of a value in a list.

                :param List: The list to search.
                :param value_to_find: The value to find.
                :return: The index of the value if found, otherwise False.
                :raises Exception: If the input list or value is None.
                """
                if List is None or value_to_find is None:
                    raise Exception("No input given.")
                try:
                    return List.index(value_to_find)
                except ValueError:
                    return False

    class InSentence:
        @staticmethod
        def longest_word(text: str) -> str:
            """
            Find the longest word in a sentence.

            :param text: The sentence to search.
            :return: The longest word in the sentence.
            :raises Exception: If the input text is None.
            """
            if text is None:
                raise Exception("No input given.")
            words = text.split()
            return max(words, key=len) if words else ""

        @staticmethod
        def shortest_word(text: str) -> str:
            """
            Find the shortest word in a sentence.

            :param text: The sentence to search.
            :return: The shortest word in the sentence.
            :raises Exception: If the input text is None.
            """
            if text is None:
                raise Exception("No input given.")
            words = text.split()
            return min(words, key=len) if words else ""

        class Word:
            @staticmethod
            def exists(text: str, word_to_find: str) -> bool:
                """
                Check if a word exists in a sentence.

                :param text: The sentence to search.
                :param word_to_find: The word to find.
                :return: True if the word exists, otherwise False.
                :raises Exception: If the input text or word is None.
                """
                if text is None or word_to_find is None:
                    raise Exception("No input given.")
                return word_to_find in text

            @staticmethod
            def occurrences(text: str, word_to_count: str) -> int:
                """
                Count the occurrences of a word in a sentence.

                :param text: The sentence to search.
                :param word_to_count: The word to count.
                :return: The number of occurrences of the word.
                :raises Exception: If the input text or word is None.
                """
                if text is None or word_to_count is None:
                    raise Exception("No input given.")
                return text.lower().split().count(word_to_count.lower())

    class InWord:
        @classmethod
        def total_vowels(cls, Word: str) -> int:
            """
            Count the total number of vowels in a word.

            :param Word: The word to search.
            :return: The total number of vowels in the word.
            :raises Exception: If the input word is None.
            """
            if Word is None:
                raise Exception("No input given.")
            vowels = cls.__vowel_y(Word)
            return sum(1 for char in Word if char in vowels)

        @staticmethod
        def __vowel_y(string: str, only_lowercase=False) -> str:
            """
            Determine the set of vowels to use, including 'y' in certain cases.

            :param string: The word to check.
            :param only_lowercase: Whether to include only lowercase vowels.
            :return: A string of vowels to use.
            :raises Exception: If the input string is None.
            """
            if string is None:
                raise Exception("No input given.")
            if string in [
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
            ]:
                return "aeiouy" if only_lowercase else "aeiouyAEIOUY"
            return "aeiou" if only_lowercase else "aeiouAEIOU"
