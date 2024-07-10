r"""
Handles both integers and floats seamlessly, converting between types as needed.
Gracefully ignores non-numeric elements without crashing, enhancing reliability.
Interactive input method allows for easy testing and experimentation.
Sorts lists efficiently and finds largest/smallest elements with minimal overhead.

COMPLEXITY = O(n\log(n))

SPACE COMPLEXITY = O(n)

Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life
"""


class Find:
    def __sort(self, List):
        """
        Sorts a list of numbers in ascending order after converting all integers to floats.
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

    def largest(self, List=None):
        """
        Returns the largest element in the given list.
        """
        largeList = self.__sort(List)

        if largeList is None:
            raise ValueError("List contains non-integer elements.")

        return largeList[-1] if largeList else None

    def smallest(self, List=None):
        """
        Returns the smallest element in the given list.
        """
        smallList = self.__sort(List)

        if smallList is None:
            raise ValueError("List contains non-integer elements.")

        return smallList[0] if smallList else None

    @staticmethod
    def __input_list():
        """
        Takes given numbers from the user and adds them to a list.
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


"""
from --- import *

find = Find()
list_place = [17, 5.0, "hi", 65.03, 32.0, -4, -5.8]
print(find.largest(list_place))
print(find.smallest(list_place))
"""
