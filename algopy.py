"""
------------------------------------------------------------------------------------------------------------------------

N = number of elements to process.
M = difference between the largest number and smallest number in the list.
K = integers length of the largest number in the list.
H = height of the tree.

### Time Complexity
- **O(1)**:
  - [Log.info]
  - [Log.warning]
  - [Log.error]
  - [Log.critical]
  - [Convert.memory]

- **O(n)**:
  - [Find.value_index]
  - [Validate.email]
  - [Validate.url]
  - [Validate.phone_number]
  - [Validate.CreditCard()]
  - [Convert.dec_to_roman]
  - [Convert.roman_to_dec]
  - [Find.total_vowels]
  - [Find.every_vowel]
  - [Convert.bin_to_dec]
  - [Convert.bin_to_hex]
  - [Convert.hex_to_bin]
  - [Convert.hex_to_dec]
  - [Sort.LinkedList().append]
  - [Sort.LinkedList().return_elements]
  - [Sort.TreeNode().sort]

- **O(n + m)**:
  - [Sort.using_counting_sort]

- **O(log n)**:
  - [Convert.dec_to_hex]
  - [Convert.dec_to_bin]

- **O(n log n)**:
  - [Find.largest]
  - [Find.smallest]
  - [Sort.using_quicksort]
  - [Sort.using_merge_sort]
  - [Sort.using_heap_sort]

- **O(n * k)**:
  - [Convert.dec_to_ascii]
  - [Sort.using_radix_sort]

- **O(n^2)**:
  - [Sort.using_selection]
  - [Sort.using_bubble]
  - [Sort.using_insertion]
  - [Sort.LinkedList().using_bubble]

- **O((n+1)! / 2) OR Unbounded(infinite)**:
  - [Sort.using_bogo_sort]

------------------------------------------------------------------------------------------------------------------------

### Space Complexity
- O(1):
  - [Find.value_index]
  - [Find.total_vowels]
  - [Find.every_vowel]
  - [Sort.using_selection]
  - [Sort.using_bubble]
  - [Sort.using_insertion]
  - [Sort.using_heap_sort]
  - [Convert.dec_to_ascii]
  - [Convert.dec_to_roman]
  - [Convert.roman_to_dec]
  - [Convert.bin_to_dec]
  - [Convert.bin_to_hex]
  - [Convert.hex_to_bin]
  - [Convert.hex_to_dec]
  - [Convert.dec_to_hex]
  - [Convert.dec_to_bin]
  - [Convert.memory]
  - [Sort.using_bogo_sort]
  - [Validate.email]
  - [Validate.url]
  - [Validate.phone_number]
  - [Validate.CreditCard()]
  - [Sort.LinkedList().using_bubble]
  - [Sort.LinkedList().append]

- O(n):
  - [Find.largest]
  - [Find.smallest]
  - [Log.info]
  - [Log.warning]
  - [Log.error]
  - [Log.critical]
  - [Sort.using_merge_sort]
  - [Sort.LinkedList().return_elements]

- O(h):
  - [Sort.TreeNode().sort]

- **O(n + k)**:
  - [Sort.using_radix_sort]

- **O(n + m)**:
  - [Sort.using_counting_sort]

- O(log n):
  - [Sort.using_quicksort]

------------------------------------------------------------------------------------------------------------------------
"""

# Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life


# Separate these files as an actual library
import heapq
import random
import re
import inspect
import os
from datetime import datetime
import colorlog
import logging


# TODO Redo all Algopy to include the following:
#     Binary trees
#       Complete binary tree
#       Balanced binary tree
#       Perfect binary tree
#       Degenerate binary tree
#       Degenerate or pathological tree
#       AVL tree
#       Binary search tree
#       Red-black tree
#       B+ tree
#       Segment tree
#       Skewed binary tree
#       Almost complete binary tree
#    Graphs
#       Adjacency matrix
#       Adjacency list
#       Incidence matrix
#       Edge list
#       Graph traversal
#       Breadth-first search
#       Depth-first search
#       Dijkstra's algorithm
#       Bellman-Ford algorithm
#       Floyd-Warshall algorithm
#       Prim's algorithm
#       Kruskal's algorithm
#       Topological sort
#       Strongly connected components
#       Minimum spanning tree
#       Shortest path
#       Travelling salesman problem
#       Maximum flow
#       Minimum cut
#       Eulerian path
#       Hamiltonian cycle
#       Graph coloring
#       Bipartite graph
#       Planar graph
#       Graph isomorphism
#       Graph automorphism
#    Sorting
#    Bubble sort
#    Selection sort
#    Insertion sort
#    Merge sort
#    Quick sort
#    Heap sort
#    Radix sort
#    Counting sort
#    Bucket sort
#    Shell sort
#    Cocktail sort
#    Comb sort
#    Gnome sort
#    Pancake sort
#    Stooge sort
#    Bitonic sort
#    Bogo sort
#    Cycle sort
#    Library sort
#    Patience sort
#    Smooth sort
#    Strand sort
#    Timsort
#    Block sort
#    Tournament sort
#    Spreadsort
#    Introsort
#    Unshuffle sort
#    Sleep sort
#    Bogosort
#    Stupid sort
#    Slowsort
#    Bogobogosort
#    Bubblesort with flag
#    Cocktail shaker sort
#    Comb sort
#    Gnome sort
#    Odd-even sort
#    Quick sort
#    Selection sort
#    Stooge sort
#    Strand sort
#    Tree sort
#    Cycle sort
#    Library sort
#    Patience sort
#    Smooth sort
#    Timsort
#    Block sort
#    Tournament sort
#    Spreadsort
#    Introsort
#    Unshuffle sort
#    Sleep sort
#    Bogosort
#    Stupid sort
#    Slowsort
#    Bogobogosort
#    Bubblesort with flag
#    Cocktail shaker sort
#    Comb sort
#    Gnome sort
#    Odd-even sort
#    Quick sort
#    Selection sort
#    Stooge sort
#    Strand sort
#    Tree sort
#    Cycle sort
#    Library sort
#    Patience sort
#    Smooth sort
#    Timsort
#    Block sort
#    Tournament sort
#    Spreadsort
#    Introsort
#    Unshuffle sort
#    Sleep sort
#    Bogosort
#    Stupid sort
#    Slowsort
#    Bogobogosort
#    Bubblesort with flag
#    Cocktail shaker sort
#    Comb sort
#    Gnome sort
#    Odd
#    Selection Sort
#    Bubble Sort
#    Insertion Sort
#    Merge Sort
#    Quick Sort
#    Heap Sort
#    Counting Sort
#    Radix Sort
#    Bucket Sort
#    Bingo Sort Algorithm
#    ShellSort
#    TimSort
#    Comb Sort
#    Pigeonhole Sort
#    Cycle Sort
#    Cocktail Sort
#    Strand Sort
#    Bitonic Sort
#    Pancake sorting
#    BogoSort or Permutation Sort
#    Gnome Sort
#    Sleep Sort – The King of Laziness
#    Structure Sorting in C++
#    Stooge Sort
#    Tag Sort (To get both sorted and original)
#    Tree Sort
#    Odd-Even Sort / Brick Sort
#    3-way Merge Sort
#    Dual-Pivot Quicksort
#    Flashsort
#    Smoothsort


# DONE
class Log:
    """
    A logging class that supports colored output using the colorlog library.
    """

    def __init__(self, config: dict = None):
        """
        Initializes the Log class with the given configuration.

        :param config: A dictionary containing configuration options.
        """
        config = config or {
            "filename": "AlgoPy.log",
            "use_colorlog": True,
            "log_level": "INFO",
            "debug_color": "cyan",
            "info_color": "green",
            "warning_color": "yellow",
            "error_color": "red",
            "critical_color": "red",
            "exception_color": "red",
            "colorlog_fmt_parameters": "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        }
        self.EXCEPTION_LOG_LEVEL = 45
        self.INTERNAL_LOG_LEVEL = 15
        logging.addLevelName(self.EXCEPTION_LOG_LEVEL, "EXCEPTION")
        logging.addLevelName(self.INTERNAL_LOG_LEVEL, "INTERNAL")
        self.color = config.get("use_colorlog", True)
        self.filename = config.get("filename", "AlgoPy.log")
        if self.color:
            logger = colorlog.getLogger()
            logger.setLevel(getattr(logging, config["log_level"].upper(), logging.INFO))
            handler = colorlog.StreamHandler()
            log_colors = {
                "INTERNAL": "cyan",
                "DEBUG": config.get("debug_color", "cyan"),
                "INFO": config.get("info_color", "green"),
                "WARNING": config.get("warning_color", "yellow"),
                "ERROR": config.get("error_color", "red"),
                "CRITICAL": config.get("critical_color", "red"),
                "EXCEPTION": config.get("exception_color", "red"),
            }

            formatter = colorlog.ColoredFormatter(
                config.get(
                    "colorlog_fmt_parameters",
                    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
                ),
                log_colors=log_colors,
            )

            handler.setFormatter(formatter)
            logger.addHandler(handler)
            try:
                getattr(logging, config["log_level"].upper())
            except AttributeError as AE:
                self.__internal(
                    f"Log Level {config['log_level']} not found, setting default level to INFO -> {AE}"
                )

        if not os.path.exists(self.filename):
            self.newline()
            self.raw(
                "|     Timestamp     |  LOG Level  |"
                + " " * 71
                + "LOG Messages"
                + " " * 71
                + "|"
            )
        self.newline()

    @staticmethod
    def __timestamp() -> str:
        """
        Returns the current timestamp as a string.

        :return: Current timestamp in 'YYYY-MM-DD HH:MM:SS' format.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def __pad_message(message: str) -> str:
        """
        Pads or truncates the message to fit the log format.

        :param message: The log message to be padded or truncated.
        :return: The padded or truncated message.
        """
        return (
            message + " " * (153 - len(message))
            if len(message) < 153
            else message[:150] + "..."
        ) + "|"

    def raw(self, message: str):
        """
        Logs a raw message directly to the log file.

        :param message: The raw message to be logged.
        """
        frame = inspect.stack()[1]
        if frame.function == "<module>":
            self.__internal(
                f"Raw message called from a non-function - This is not recommended"
            )
        with open(self.filename, "a") as f:
            f.write(f"{message}\n")

    def newline(self):
        """
        Logs a newline separator in the log file.
        """
        with open(self.filename, "a") as f:
            f.write("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|" + "\n")

    def info(self, message: str):
        """
        Logs an info message.

        :param message: The info message to be logged.
        """
        if self.color:
            colorlog.info(message)
        self.raw(f"[{self.__timestamp()}] > INFO:     | {self.__pad_message(message)}")

    def warning(self, message: str):
        """
        Logs a warning message.

        :param message: The warning message to be logged.
        """
        if self.color:
            colorlog.warning(message)
        self.raw(f"[{self.__timestamp()}] > WARNING:  | {self.__pad_message(message)}")

    def error(self, message: str):
        """
        Logs an error message.

        :param message: The error message to be logged.
        """
        if self.color:
            colorlog.error(message)
        self.raw(f"[{self.__timestamp()}] > ERROR:    | {self.__pad_message(message)}")

    def critical(self, message: str):
        """
        Logs a critical message.

        :param message: The critical message to be logged.
        """
        if self.color:
            colorlog.critical(message)
        self.raw(f"[{self.__timestamp()}] > CRITICAL: | {self.__pad_message(message)}")

    def debug(self, message: str):
        """
        Logs a debug message. If the message is "*-*", it logs a separator line.

        :param message: The debug message to be logged.
        """
        if message == "*-*":
            self.raw("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 152 + "|")
        else:
            colorlog.debug(message)

    def string(self, message: str, Type: str):
        """
        Logs a message with a specified type. Supported types are 'err', 'warn', and 'crit'.

        :param message: The message to be logged.
        :param Type: The type of the log message.
        """
        type_map = {"err": "error", "warn": "warning", "crit": "critical"}
        Type = type_map.get(Type.lower(), Type)
        try:
            getattr(self, Type.lower())(message)
        except AttributeError as AE:
            self.__internal(f"A wrong Log Type was called: {Type} not found. -> {AE}")
            getattr(self, "Debug".lower())(message)

    def exception(self, message: str):
        """
        Logs an exception message.

        :param message: The exception message to be logged.
        """
        if self.color:
            colorlog.log(self.EXCEPTION_LOG_LEVEL, message)
        self.raw(f"[{self.__timestamp()}] > EXCEPTION:| {self.__pad_message(message)}")

    def __internal(self, message: str):
        """
        Logs an internal message.

        :param message: The internal message to be logged.
        """
        if self.color:
            colorlog.log(self.INTERNAL_LOG_LEVEL, message)


class Sort:
    def __init__(self):
        """
        Initializes an instance of the class.

        The Sort class provides implementations of various sorting algorithms,
        including quick sort, merge sort, selection sort, bubble sort, insertion sort,
        heap sort, radix sort, counting sort, bogo sort, and linked list sorts.
        Each method sorts an array of integers or floats.

        It also includes sorting for linked lists and binary trees.
        With a way to also create them.

        The most powerful class in AlgoPy.

        """
        pass

    @staticmethod
    def __is_sorted(Array: list[int | float]) -> bool:
        """
        Checks if the elements in a given array are sorted in ascending order.

        Args:
            Array (list[int | float]): A list containing integers and/or floats.

        Returns:
            bool: True if the array is sorted, False otherwise.
        """
        return all(Array[i] <= Array[i + 1] for i in range(len(Array) - 1))

    @staticmethod
    def __merge(left: list[int | float], right: list[int | float]) -> list[int | float]:
        """
        Merges two sorted lists into a single sorted list.

        This function takes two lists of integers or floats as input,
        merges them into a single list, and returns the merged list.
        The merged list is sorted in ascending order.

        Args:
            left (list[int | float]): The first sorted list to merge.
            right (list[int | float]): The second sorted list to merge.

        Returns:
            list[int | float]: The merged sorted list.
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def using_quick_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the quicksort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        if self.__is_sorted(Array):
            return Array

        if len(Array) <= 1:
            return Array
        pivot = Array[len(Array) // 2]
        left = [x for x in Array if x < pivot]
        middle = [x for x in Array if x == pivot]
        right = [x for x in Array if x > pivot]
        return self.using_quick_sort(left) + middle + self.using_quick_sort(right)

    def using_merge_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the merge sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        if self.__is_sorted(Array):
            return Array

        if len(Array) <= 1:
            return Array
        mid = len(Array) // 2
        left = Array[:mid]
        right = Array[mid:]
        return Sort.__merge(self.using_merge_sort(left), self.using_merge_sort(right))

    def using_selection_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the selection sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        if self.__is_sorted(Array):
            return Array

        for i in range(len(Array)):
            min_index = i
            for j in range(i + 1, len(Array)):
                if Array[min_index] > Array[j]:
                    min_index = j
            Array[i], Array[min_index] = Array[min_index], Array[i]
        return Array

    def using_bubble_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the bubble sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        if self.__is_sorted(Array):
            return Array

        n = len(Array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if Array[j] > Array[j + 1]:
                    Array[j], Array[j + 1] = Array[j + 1], Array[j]
        return Array

    def using_insertion_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the insertion sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        if self.__is_sorted(Array):
            return Array

        for i in range(1, len(Array)):
            key = Array[i]
            j = i - 1
            while j >= 0 and key < Array[j]:
                Array[j + 1] = Array[j]
                j -= 1
            Array[j + 1] = key
        return Array

    def using_heap_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the heap sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        if self.__is_sorted(Array):
            return Array

        heapq.heapify(Array)
        return [heapq.heappop(Array) for _ in range(len(Array))]

    def using_radix_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the radix sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        if self.__is_sorted(Array):
            return Array

        max_value = max(Array)
        max_exponent = len(str(max_value))
        for exponent in range(max_exponent):
            digits = [[] for _ in range(10)]
            for num in Array:
                digit = (num // 10 ** exponent) % 10
                digits[digit].append(num)
            Array = []
            for digit_list in digits:
                Array.extend(digit_list)
        return Array

    def using_counting_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the counting sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")
        if self.__is_sorted(Array):
            return Array
        max_value = max(Array)
        min_value = min(Array)
        range_of_elements = max_value - min_value + 1
        count = [0] * range_of_elements
        output = [0] * len(Array)
        for num in Array:
            count[num - min_value] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        for num in reversed(Array):
            output[count[num - min_value] - 1] = num
            count[num - min_value] -= 1
        return output

    def using_bogo_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the bogo sort algorithm.

        Don't actually use this - It's a joke

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None or contains non-integer values.
        """
        if Array is None:
            raise Exception("No input given.")

        while not self.__is_sorted(Array):
            random.shuffle(Array)

        return Array

    def using_stalin_sort(self, Array: list[int | float]) -> list[int | float]:
        """
        Sorts an array of integers or floats using the Stalin sort algorithm.

        Args:
            Array (list[int | float]): The input array to be sorted.

        Returns:
            list[int | float]: The sorted array.

        Raises:
            Exception: If the input array is None.
        """
        # Base case: If the list is empty or has only one element, it's already sorted.
        if Array is None:
            raise Exception("No input given. No input can be eliminated.")

        # Find the minimum element in the list
        min_value = min(Array)

        # Remove all occurrences of the minimum value from the list
        Array = [x for x in Array if x != min_value]

        # Recursively sort the rest of the list
        return [min_value] + self.using_stalin_sort(Array)

    @classmethod
    class LinkedList:
        def __init__(self, Data=None):
            """
            Initializes a new instance of the LinkedList class.

            Creates a new linked list node with the given data.

            Usage:
                linked_list = Sort.LinkedList()
                linked_list.append(5)
                linked_list.append(15)
                linked_list.append(3)
                linked_list.append(12)
                linked_list.append(9)
                linked_list.using_bubble()

            This method will sort the linked list in ascending order, based on the data stored in the nodes,
            of the linked list.

            Args:
                Data (any, optional): The data to be stored in the linked list node. Defaults to None.

            Returns:
                None
            """
            self.head = None
            self.data = Data
            self.next = None

        def __merge(self, start, mid, end):
            """
            Recursively merges two sorted linked lists into a single sorted linked list.

            Args:
                start (LinkedList): The starting node of the first linked list.
                mid (LinkedList): The ending node of the first linked list.
                end (LinkedList): The ending node of the second linked list.

            Returns:
                LinkedList: The merged and sorted linked list.
            """
            if start is None:
                return end
            if end is None:
                return start

            if start.data <= end.data:
                start.next = self.__merge(start.next, mid, end)
            else:
                end.next = self.__merge(start, mid, end)
                start, end = end, start

            return start

        def append(self, data: int | float) -> None:
            """
            Adds a new node to the end of the linked list.

            Args:
                data (int | float): The data to be stored in the new node.

            Returns:
                None
            """
            if not self.head:
                self.head = Sort().LinkedList(data)
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = Sort().LinkedList(data)

        def return_elements(self) -> list[int | float]:
            """
            Returns a list of elements in the linked list.

            Returns:
                list[int | float]: A list of elements in the linked list.
            """
            elements = []
            current_node = self.head
            while current_node:
                elements.append(current_node.data)
                current_node = current_node.next
            return elements

        def using_bubble(self) -> None:
            """
            Sorts a linked list in ascending order using the bubble sort algorithm.

            This function iterates through the linked list, repeatedly swapping adjacent nodes if they are in the wrong order.
            The process is repeated until no more swaps are needed, indicating that the list is sorted.

            Returns:
                None
            """
            if self.head is None:
                return

            swapped = True
            while swapped:
                swapped = False
                current = self.head
                while current.next is not None:
                    if current.data > current.next.data:
                        current.data, current.next.data = (
                            current.next.data,
                            current.data,
                        )
                        swapped = True
                    current = current.next

    @classmethod
    class BinaryTree:
        def __init__(self, val=0, left=None, right=None):
            """
            Initializes a new instance of the BinaryTree class.

            Usage:
                # Define nodes for the binary tree
                sort_node = Sort.BinaryTree
                root = sort_node(5)  # root is the beginning of the binary tree
                root.left = sort_node(3)
                root.right = sort_node(7)
                root.left.left = sort_node(2)
                root.left.right = sort_node(4)
                root.right.left = sort_node(6)
                root.right.right = sort_node(8)

                # Now, let's sort the values in the binary tree using the sort method
                sorted_values = root.sort(root)  # root is the beginning of the binary tree, you can change this to any branch like root.left to only sort and show the values in the left branch
                print(sorted_values)

            This method will sort the binary tree in ascending order properly

            Args:
                val (int | float, optional): The value of the node. Defaults to 0.
                left (Sort.BinaryTree, optional): The left child node. Defaults to None.
                right (Sort.BinaryTree, optional): The right child node. Defaults to None.

            Returns:
                None
            """
            self.val = val
            self.left = left
            self.right = right

        def sort(self, root) -> list[int | float]:
            """
            Sorts a binary tree in-order and returns a list of the sorted values.

            Args:
                root (Sort.BinaryTree): The root node of the binary tree.

            Returns:
                list[int | float]: A list of the sorted values in the binary tree.
            """
            if root is None:
                return []

            left_values = self.sort(root.left)
            values = [root.val]
            right_values = self.sort(root.right)

            return left_values + values + right_values


# DONE
class Validate:
    @staticmethod
    def this_email(email_address: str) -> bool:
        """
        Validates an email address against a set of predefined rules.

        Args:
            email_address (str): The email address to be validated.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        if len(email_address) < 1 or len(email_address) > 320:
            return False
        if " " in email_address:
            return False
        pattern = re.compile(r"^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        return bool(pattern.search(email_address))

    @staticmethod
    def this_url(url_string: str) -> bool:
        """
        Validates a URL against a set of predefined rules.

        Args:
            url_string (str): The URL to be validated.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        if " " in url_string:
            return False
        pattern = re.compile(r"^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*/?$")
        return bool(pattern.search(url_string))

    @staticmethod
    def this_phone_number(phone_number: int | str) -> bool:
        """
        Validates a phone number against a set of predefined rules.

        Args:
            phone_number (int | str): The phone number to be validated.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        pattern = re.compile(r"^\+?[0-9]{1,3}?[ -]?[0-9]{1,3}?[ -]?[0-9]{1,4}$")
        return bool(pattern.match(str(phone_number)))

    class CreditCard:
        def __init__(self):
            """
            Validates a card number using the Luhn algorithm.
            Specify in specifics inside the class.

            Returns a boolean value if the card number is valid or not.
            """
            pass

        @staticmethod
        def __luhn_algorithm(card_number: int) -> bool:
            """
            Validates a card number using the Luhn algorithm.

            Args:
                card_number (int): The card number to validate.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            num_list = [int(digit) for digit in str(card_number)]
            num_list.reverse()
            total = 0
            for i, num in enumerate(num_list):
                doubled = num * 2
                if doubled > 9:
                    doubled -= 9
                total += doubled
            return total % 10 == 0

        @classmethod
        def american_express(cls, card_number: int) -> bool:
            """
            Validates American Express card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(("34", "37"))
                    and 15 <= len(str(card_number)) <= 16
            )

        @classmethod
        def china_unionpay(cls, card_number: int) -> bool:
            """
            Validates China UnionPay card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(
                        (
                            "62",
                            "64",
                            "65",
                            "66",
                            "67",
                            "68",
                            "69",
                            "92",
                            "93",
                            "94",
                            "95",
                            "96",
                            "97",
                            "98",
                            "99",
                        )
                    )
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def dankort(cls, card_number: int) -> bool:
            """
            Validates Dankort card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("49")
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def diners_club(cls, card_number: int) -> bool:
            """
            Validates Diners Club International card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(("36", "38"))
                    and 14 <= len(str(card_number)) <= 19
            )

        @classmethod
        def discover(cls, card_number: int) -> bool:
            """
            Validates Discover card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(
                        (
                            "6011",
                            "6221",
                            "6222",
                            "6223",
                            "623",
                            "624",
                            "625",
                            "626",
                            "627",
                            "628",
                            "641",
                            "642",
                            "643",
                            "644",
                            "645",
                            "646",
                            "647",
                            "648",
                            "649",
                            "65",
                            "66",
                            "67",
                            "68",
                            "69",
                            "71",
                            "72",
                            "73",
                            "74",
                            "75",
                            "76",
                            "77",
                            "78",
                            "79",
                        )
                    )
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def jcb(cls, card_number: int) -> bool:
            """
            Validates JCB card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("35")
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def maestro(cls, card_number: int) -> bool:
            """
            Validates Maestro card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(
                        (
                            "50",
                            "51",
                            "52",
                            "53",
                            "54",
                            "55",
                            "56",
                            "57",
                            "58",
                            "60",
                            "61",
                            "62",
                            "63",
                            "64",
                            "65",
                            "66",
                            "67",
                            "68",
                            "69",
                            "70",
                            "71",
                            "72",
                            "73",
                            "74",
                            "75",
                            "76",
                            "77",
                            "78",
                            "79",
                        )
                    )
                    and 12 <= len(str(card_number)) <= 19
            )

        @classmethod
        def mastercard(cls, card_number: int) -> bool:
            """
            Validates Mastercard card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith(("51", "52", "53", "54", "55", "56", "57", "58", "59"))
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def visa(cls, card_number: int) -> bool:
            """
            Validates Visa card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("4")
                    and 13 <= len(str(card_number)) <= 16
            )

        @classmethod
        def visa_electron(cls, card_number: int) -> bool:
            """
            Validates Visa Electron card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith(("40", "41", "42", "43", "44", "45", "46", "47", "48", "49"))
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def v_pay(cls, card_number: int) -> bool:
            """
            Validates V Pay card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(str(card_number)).startswith("28")
                    and 16 <= len(str(str(card_number)))
            )

        @classmethod
        def any(cls, card_number: int) -> bool:
            """
            Validates any card number just by passing it to the Luhn algorithm.
            """
            return cls.__luhn_algorithm(card_number)


# DONE
class Convert:
    class Binary:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        @classmethod
        def to_hex(cls, Binary_Number: int) -> str:
            if Binary_Number is None:
                raise Exception("No binary number provided")
            cls.__check_input_type(str(Binary_Number), str)
            return hex(int(str(Binary_Number), 2))[2:].upper()

        @classmethod
        def to_dec(cls, Binary_Number: int) -> int:
            if Binary_Number is None:
                raise Exception("No binary number provided")
            cls.__check_input_type(str(Binary_Number), str)
            return int(str(Binary_Number), 2)

    class Decimal:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        @staticmethod
        def to_roman(Number: int) -> str:
            mapping = {
                1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
            }
            if Number is None or Number < 1:
                raise Exception("Invalid input.")
            result = ""
            for num, roman in sorted(mapping.items(), reverse=True):
                while Number >= num:
                    result += roman
                    Number -= num
            return result

        @staticmethod
        def to_ascii(Number: int | str) -> str:
            digits = [
                ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "],
                [" * ", "** ", " * ", " * ", " * ", " * ", "***"],
                [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"],
                [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "],
                ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "],
                ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "],
                [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "],
                ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "],
                [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "],
                [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
            ]
            Number = str(Number)
            if Number is None:
                raise Exception("No input given.")
            ascii_art_lines = ["".join(digits[int(digit)][i] + "  " for digit in Number) for i in range(7)]
            return "\n".join(ascii_art_lines)

        @classmethod
        def to_hex(cls, Decimal_Number: int) -> str:
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            cls.__check_input_type(Decimal_Number, (int, str))
            return hex(Decimal_Number)[2:].upper()

        @classmethod
        def to_bin(cls, Decimal_Number: int) -> int:
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            cls.__check_input_type(Decimal_Number, (int, str))
            return int(bin(Decimal_Number)[2:])

    class Hexadecimal:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        @classmethod
        def to_bin(cls, Hexadecimal_Number: str) -> int:
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            cls.__check_input_type(Hexadecimal_Number, str)
            return int(bin(int(Hexadecimal_Number, 16))[2:])

        @classmethod
        def to_dec(cls, Hexadecimal_Number: str) -> int:
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            cls.__check_input_type(Hexadecimal_Number, str)
            return int(Hexadecimal_Number, 16)

    class Roman:
        @staticmethod
        def to_dec(Roman: str) -> int:
            roman_to_numerical = {
                "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
            }
            if not isinstance(Roman, str):
                raise Exception("Input must be a string.")
            elif not Roman.isupper():
                raise Exception("Input must be uppercase.")
            elif Roman is None:
                raise Exception("Input cannot be None.")
            i, num = 0, 0
            Roman = Roman.upper()
            while i < len(Roman):
                if i + 1 < len(Roman) and Roman[i: i + 2] in roman_to_numerical:
                    num += roman_to_numerical[Roman[i: i + 2]]
                    i += 2
                else:
                    num += roman_to_numerical[Roman[i]]
                    i += 1
            return num

    class Celsius:
        @staticmethod
        def to_fahrenheit(celsius: float | int) -> float:
            if celsius is None:
                raise Exception("No temperature provided")
            return (celsius * 9 / 5) + 32

        @staticmethod
        def to_kelvin(celsius: float | int) -> float:
            if celsius is None:
                raise Exception("No temperature provided")
            return celsius + 273.15

    class Kelvin:
        @staticmethod
        def to_celsius(kelvin: float | int) -> float:
            if kelvin is None:
                raise Exception("No temperature provided")
            return kelvin - 273.15

        @staticmethod
        def to_fahrenheit(kelvin: float | int) -> float:
            if kelvin is None:
                raise Exception("No temperature provided")
            return (kelvin - 273.15) * 9 / 5 + 32

    class Fahrenheit:
        @staticmethod
        def to_kelvin(fahrenheit: float | int) -> float:
            if fahrenheit is None:
                raise Exception("No temperature provided")
            return (fahrenheit - 32) * 5 / 9 + 273.15

        @staticmethod
        def to_celsius(fahrenheit: float | int) -> float:
            if fahrenheit is None:
                raise Exception("No temperature provided")
            return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def memory(number: int, input_unit: str, output_unit: str) -> str:
        memory_dict = {
            "bit": 1, "byte": 8, "kilobyte": 8000, "megabyte": 8 * (1000 ** 2), "gigabyte": 8 * (1000 ** 3),
            "terrabyte": 8 * (1000 ** 4), "petabyte": 8 * (1000 ** 5), "kibibyte": 8192, "mebibyte": 8 * (1024 ** 2),
            "gibibyte": 8 * (1024 ** 3), "tebibyte": 8 * (1024 ** 4), "pebibyte": 8 * (1024 ** 5),
            "kilobit": 1000, "megabit": 1000 ** 2, "gigabit": 1000 ** 3, "terrabit": 1000 ** 4, "petabit": 1000 ** 5,
            "kibibit": 1024, "mebibit": 1024 ** 2, "gibibit": 1024 ** 3, "tebibit": 1024 ** 4, "pebibit": 1024 ** 5,
            "KB": 8000, "MB": 8 * (1000 ** 2), "GB": 8 * (1000 ** 3), "TB": 8 * (1000 ** 4), "PB": 8 * (1000 ** 5),
            "KiB": 8192, "MiB": 8 * (1024 ** 2), "GiB": 8 * (1024 ** 3), "TiB": 8 * (1024 ** 4), "PiB": 8 * (1024 ** 5),
            "Kb": 1000, "Mb": 1000 ** 2, "Gb": 1000 ** 3, "Tb": 1000 ** 4, "Pb": 1000 ** 5,
            "Kib": 1024, "Mib": 1024 ** 2, "Gib": 1024 ** 3, "Tib": 1024 ** 4, "Pib": 1024 ** 5
        }
        if not all([number, input_unit, output_unit]):
            raise Exception(f"Invalid input: {number} {input_unit} -> {output_unit}")
        if input_unit == output_unit:
            return f"{number} {output_unit}"
        input_unit = input_unit.lower() if len(input_unit) > 3 and input_unit.lower() != "bit" else input_unit
        output_unit = output_unit.lower() if len(output_unit) > 3 and output_unit.lower() != "bit" else output_unit
        if not isinstance(number, int) or input_unit not in memory_dict or output_unit not in memory_dict:
            raise Exception(f"Invalid input: {number} {input_unit} -> {output_unit}")
        final_number = (number * memory_dict[input_unit]) / memory_dict[output_unit]
        return f"{final_number:.15f}".rstrip('0').rstrip('.') + f" {output_unit}"


# DONE
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

        @classmethod
        def every_vowel(cls, Word: str) -> str:
            if Word is None:
                raise Exception("No input given.")
            vowels = cls.__vowel_y(Word, True)
            # TODO Turn to json
            return "\n".join(f"{vowel} {Word.count(vowel)}" for vowel in vowels)

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
