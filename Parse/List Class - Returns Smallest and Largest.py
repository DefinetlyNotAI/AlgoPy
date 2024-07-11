r"""
Handles both integers and floats seamlessly, converting between types as needed.
Gracefully ignores non-numeric elements without crashing, enhancing reliability.
Interactive input method allows for easy testing and experimentation.
Sorts lists efficiently and finds largest/smallest elements with minimal overhead.

COMPLEXITY = O(n \ log n ) [largest] and [smallest]
COMPLEXITY = O(n) [value_index]

SPACE COMPLEXITY = O(n) [largest] and [smallest]
SPACE COMPLEXITY = O(1) [value_index]

Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life
"""


class Find:
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

    @staticmethod
    def value_index(array, value_to_find):
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == value_to_find:
                return index  # Return the index if the value matches
        return False  # Return False if the value was not found in the list


"""
from --- import *

find = Find()
list_place = [17, 5.0, "hi", 65.03, 32.0, -4, -5.8]
print(find.largest(list_place))
print(find.smallest(list_place))
print(find.value_from_list(list_place, 32.0))
print(find.every_vowel("Hola"))
print(find.total_vowels("Hola"))
"""
