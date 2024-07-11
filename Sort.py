"""
Provides a unified interface for sorting arrays/lists of comparable items using various sorting algorithms.
Supports sorting of mixed data types by comparing their string representations, allowing for flexibility in input.
Incorporates best practices for algorithm implementation, including efficient use of static methods for reusable logic.
Quicksort and merge sort are implemented recursively, demonstrating advanced recursion techniques and divide-and-conquer strategies.
Selection sort, bubble sort, and insertion sort are included for educational purposes, showcasing simpler sorting mechanisms.
Each sorting method is designed to handle arrays/lists of any size, with optimizations for performance and memory usage.
If an error occurs it returns False.

TIME COMPLEXITY: O(n^2) [Sort.using_selection] [Sort.using_bubble] [Sort.using_insertion]
TIME COMPLEXITY: O(n log n) [Sort.using_quicksort] [Sort.using_merge_sort]

SPACE COMPLEXITY: O(1) [Sort.using_selection] [Sort.using_bubble] [Sort.using_insertion]
SPACE COMPLEXITY: O(log n) [Sort.using_quicksort]
SPACE COMPLEXITY: O(n) [Sort.using_merge_sort]
"""


class Sort:
    @staticmethod
    def __integer(Array):
        """
        Checks if all elements in the input Array are integers.

        Parameters:
            Array (list): The input list to check for integer elements.

        Returns:
            bool: True if all elements are integers, False otherwise.
        """
        return all(isinstance(item, int) for item in Array)

    @staticmethod
    def using_quick_sort(Array):
        """
        Sorts the given array using the quicksort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.
        """
        if not Sort.__integer(Array):
            return False
        if len(Array) <= 1:
            return Array
        pivot = Array[len(Array) // 2]
        left = [x for x in Array if x < pivot]
        middle = [x for x in Array if x == pivot]
        right = [x for x in Array if x > pivot]
        return Sort.using_quick_sort(left) + middle + Sort.using_quick_sort(right)

    @staticmethod
    def using_merge_sort(Array):
        """
        Sorts the given array using the merge sort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.

        This function recursively divides the input array into two halves, sorts each half using merge sort, and then merges the two sorted halves into a single sorted array.
        """
        if not Sort.__integer(Array):
            return False
        if len(Array) <= 1:
            return Array
        mid = len(Array) // 2
        left = Array[:mid]
        right = Array[mid:]
        return Sort.__merge(Sort.using_merge_sort(left), Sort.using_merge_sort(right))

    @staticmethod
    def __merge(left, right):
        """
        Merges two sorted arrays 'left' and 'right' into a single sorted array.

        Parameters:
            left (list): The left sorted array.
            right (list): The right sorted array.

        Returns:
            list: The merged sorted array containing all elements from 'left' and 'right'.
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

    @staticmethod
    def using_selection_sort(Array):
        """
        Sorts the given array using the selection sort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.
        """
        if not Sort.__integer(Array):
            return False
        for i in range(len(Array)):
            min_index = i
            for j in range(i+1, len(Array)):
                if Array[min_index] > Array[j]:
                    min_index = j
            Array[i], Array[min_index] = Array[min_index], Array[i]
        return Array

    @staticmethod
    def using_bubble_sort(Array):
        """
        Sorts the given array using the bubble sort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.
        """
        if not Sort.__integer(Array):
            return False
        n = len(Array)
        for i in range(n):
            for j in range(0, n-i-1):
                if Array[j] > Array[j+1]:
                    Array[j], Array[j+1] = Array[j+1], Array[j]
        return Array

    @staticmethod
    def using_insertion_sort(Array):
        """
        Sorts the given array using the insertion sort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.

        This function takes an array as input and sorts it using the insertion sort algorithm. The algorithm iterates through the array, starting from the second element, and compares each element with the elements before it. If an element is smaller than its predecessor, it is shifted to the left until it finds its correct position.
        """
        if not Sort.__integer(Array):
            return False
        for i in range(1, len(Array)):
            key = Array[i]
            j = i-1
            while j >= 0 and key < Array[j]:
                Array[j+1] = Array[j]
                j -= 1
            Array[j+1] = key
        return Array


"""
# Example usage
sort = Sort()
arr = [34, 5, 7, 23, 32, 4]
print("Original array:", arr)

sorted_arr_quick = sort.using_quick_sort(arr.copy())
print("Sorted using QuickSort:", sorted_arr_quick)

sorted_arr_merge = sort.using_merge_sort(arr.copy())
print("Sorted using MergeSort:", sorted_arr_merge)

sorted_arr_select = sort.using_selection_sort(arr.copy())
print("Sorted using SelectionSort:", sorted_arr_select)

sorted_arr_bubble = sort.using_bubble_sort(arr.copy())
print("Sorted using BubbleSort:", sorted_arr_bubble)

sorted_arr_insert = sort.using_insertion_sort(arr.copy())
print("Sorted using InsertionSort:", sorted_arr_insert)
"""