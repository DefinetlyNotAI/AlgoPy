"""
Provides a unified interface for sorting arrays/lists of comparable items using various sorting algorithms.
Supports sorting of mixed data types by comparing their string representations, allowing for flexibility in input.
Incorporates best practices for algorithm implementation, including efficient use of static methods for reusable logic.
Quicksort and merge sort are implemented recursively, demonstrating advanced recursion techniques and divide-and-conquer strategies.
Selection sort, bubble sort, and insertion sort are included for educational purposes, showcasing simpler sorting mechanisms.
Each sorting method is designed to handle arrays/lists of any size, with optimizations for performance and memory usage.


TIME COMPLEXITY: O(n^2) [Sort.using_selection] [Sort.using_bubble] [Sort.using_insertion]
TIME COMPLEXITY: O(n log n) [Sort.using_quicksort] [Sort.using_merge_sort]

SPACE COMPLEXITY: O(1) [Sort.using_selection] [Sort.using_bubble] [Sort.using_insertion]
SPACE COMPLEXITY: O(log n) [Sort.using_quicksort]
SPACE COMPLEXITY: O(n) [Sort.using_merge_sort]
"""


class Sort:
    @staticmethod
    def using_selection(Array):
        for i in range(len(Array)):
            min_index = i
            for j in range(i + 1, len(Array)):
                if str(Array[j]) < str(Array[min_index]):
                    min_index = j

            Array[i], Array[min_index] = Array[min_index], Array[i]
        return Array

    @staticmethod
    def using_bubble(Array):
        n = len(Array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if str(Array[j]) > str(Array[j + 1]):
                    Array[j], Array[j + 1] = Array[j + 1], Array[j]
        return Array

    @staticmethod
    def using_insertion(Array):
        for i in range(1, len(Array)):
            key = Array[i]
            j = i - 1
            while j >= 0 and str(key) < str(Array[j]):
                Array[j + 1] = Array[j]
                j -= 1
            Array[j + 1] = key
        return Array

    def using_quicksort(self, Array):
        if len(Array) <= 1:
            return Array
        pivot = Array[len(Array) // 2]
        left = [x for x in Array if str(x) < str(pivot)]
        middle = [x for x in Array if str(x) == str(pivot)]
        right = [x for x in Array if str(x) > str(pivot)]
        return self.using_quicksort(left) + middle + self.using_quicksort(right)

    def using_merge_sort(self, Array):
        if len(Array) > 1:
            mid = len(Array) // 2
            L = Array[:mid]
            R = Array[mid:]

            self.using_merge_sort(L)
            self.using_merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if str(L[i]) < str(R[j]):
                    Array[k] = L[i]
                    i += 1
                else:
                    Array[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                Array[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                Array[k] = R[j]
                j += 1
                k += 1

        return Array


# Sample array containing integers and strings
sort = Sort()
sample_array = [1, 37, 5, 78, 99, 5]

# Using selection sort
print("Selection Sort:")
print(sort.using_selection(sample_array.copy()))

# Using bubble sort
print("\nBubble Sort:")
print(sort.using_bubble(sample_array.copy()))

# Using insertion sort
print("\nInsertion Sort:")
print(sort.using_insertion(sample_array.copy()))

# Using quicksort
print("\nQuicksort:")
print(sort.using_quicksort(sample_array.copy()))

# Using merge sort
print("\nMerge Sort:")
print(sort.using_merge_sort(sample_array.copy()))
