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
    def using_selection(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if str(arr[j]) < str(arr[min_index]):
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

    @staticmethod
    def using_bubble(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if str(arr[j]) > str(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def using_insertion(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and str(key) < str(arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def using_quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if str(x) < str(pivot)]
        middle = [x for x in arr if str(x) == str(pivot)]
        right = [x for x in arr if str(x) > str(pivot)]
        return self.using_quicksort(left) + middle + self.using_quicksort(right)

    def using_merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.using_merge_sort(L)
            self.using_merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if str(L[i]) < str(R[j]):
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
