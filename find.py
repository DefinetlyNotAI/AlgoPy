class Find:
    class InArray:
        @staticmethod
        def __sort(List: list) -> list[int | float]:
            if List is None:
                raise Exception("No input given.")
            converted_list = sorted(float(item) for item in List if isinstance(item, (int, float)))
            return [int(item) if item.is_integer() else item for item in converted_list]

        @classmethod
        def largest_number(cls, List: list[int | float]) -> int | float:
            if List is None:
                raise Exception("No input given.")
            sorted_list = cls.__sort(List)
            return sorted_list[-1] if sorted_list else None

        @classmethod
        def smallest_number(cls, List: list[int | float]) -> int | float:
            if List is None:
                raise Exception("No input given.")
            sorted_list = cls.__sort(List)
            return sorted_list[0] if sorted_list else None

        class Objects:
            @staticmethod
            def index_all(List: list, value_to_find: any) -> list[int]:
                if List is None or value_to_find is None:
                    raise Exception("No input given.")
                return [index for index, value in enumerate(List) if value == value_to_find]

            @staticmethod
            def index(List: list, value_to_find: any) -> int | bool:
                if List is None or value_to_find is None:
                    raise Exception("No input given.")
                try:
                    return List.index(value_to_find)
                except ValueError:
                    return False

    class InSentence:
        @staticmethod
        def longest_word(text: str) -> str:
            if text is None:
                raise Exception("No input given.")
            words = text.split()
            return max(words, key=len) if words else ""

        @staticmethod
        def shortest_word(text: str) -> str:
            if text is None:
                raise Exception("No input given.")
            words = text.split()
            return min(words, key=len) if words else ""

        class Word:
            @staticmethod
            def exists(text: str, word_to_find: str) -> bool:
                if text is None or word_to_find is None:
                    raise Exception("No input given.")
                return word_to_find in text

            @staticmethod
            def occurrences(text: str, word_to_count: str) -> int:
                if text is None or word_to_count is None:
                    raise Exception("No input given.")
                return text.lower().split().count(word_to_count.lower())

    class InWord:
        @classmethod
        def total_vowels(cls, Word: str) -> int:
            if Word is None:
                raise Exception("No input given.")
            vowels = cls.__vowel_y(Word)
            return sum(1 for char in Word if char in vowels)

        @staticmethod
        def __vowel_y(string: str, only_lowercase=False) -> str:
            if string is None:
                raise Exception("No input given.")
            if string in [
                "Cry", "Dry", "Gym", "Hymn", "Lynx", "Myth", "Pry", "Rhythm", "Shy", "Spy", "Spry", "Sync", "Try",
                "Why",
                "City", "Party", "Fly", "Shy", "Wary", "Worthwhile", "Type", "Typical", "Thyme", "Cyst", "Symbol",
                "System",
                "Lady", "Pretty", "Very", "Deny", "Daddy", "Quickly",
            ]:
                return "aeiouy" if only_lowercase else "aeiouyAEIOUY"
            return "aeiou" if only_lowercase else "aeiouAEIOU"
