import math
import random
import threading
import time
from heapq import heappush, heappop
from typing import Optional, List


class Sort:
    class String:
        @classmethod
        def and_integer(
                cls,
                arr: list[int | str],
                reverse: bool = False,
                sort_integers: bool = True,
                sort_strings: bool = True,
        ) -> tuple[list[int], list[str]]:
            """
            Splits a list into integers and strings, sorts them separately, and optionally reverses the order.

            Args:
                arr (list[int | str]): The list containing integers and strings.
                reverse (bool): If True, reverses the order of the sorted lists.
                sort_integers (bool): If True, sorts the integers.
                sort_strings (bool): If True, sorts the strings.

            Returns:
                tuple[list[int], list[str]]: A tuple containing the sorted integers and strings.
            """
            str_list = [x for x in arr if isinstance(x, str)]
            int_list = [x for x in arr if isinstance(x, int)]
            if sort_strings:
                str_list = cls.alphabetically(str_list)
            if sort_integers:
                int_list = Sort.QuickSort.default(int_list)
            if reverse:
                int_list.reverse()
                str_list.reverse()
            return int_list, str_list

        @staticmethod
        def alphabetically(arr: list[str], reverse: bool = False) -> list[str]:
            """
            Sorts a list of strings alphabetically.

            Args:
                arr (list[str]): The list of strings to sort.
                reverse (bool): If True, sorts the list in reverse order.

            Returns:
                list[str]: The sorted list of strings.
            """
            if not arr:
                return []
            if reverse:
                return sorted([str(item) for item in arr], reverse=True)
            return sorted([str(item) for item in arr])

    class BubbleSort:
        @staticmethod
        def default(arr: list[int]) -> list[int]:
            """
            Sorts a list of integers using the bubble sort algorithm.

            Args:
                arr (list[int]): The list of integers to sort.

            Returns:
                list[int]: The sorted list of integers.
            """
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        @staticmethod
        def with_flag(arr: list[int]) -> list[int]:
            """
            Sorts a list of integers using the bubble sort algorithm with a flag to detect sorted lists.

            Args:
                arr (list[int]): The list of integers to sort.

            Returns:
                list[int]: The sorted list of integers.
            """
            n = len(arr)
            for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                if not swapped:
                    break
            return arr

    class QuickSort:
        @classmethod
        def dual_pivot(cls, arr: list[int], low: int, high: int) -> list[int]:
            """
            Sorts a list of integers using the dual-pivot quicksort algorithm.

            Args:
                arr (list[int]): The list of integers to sort.
                low (int): The starting index of the list to sort.
                high (int): The ending index of the list to sort.

            Returns:
                list[int]: The sorted list of integers.
            """

            def partition(arr, low, high):
                if arr[low] > arr[high]:
                    arr[low], arr[high] = arr[high], arr[low]
                j = k = low + 1
                g = high - 1
                p = arr[low]
                q = arr[high]
                while k <= g:
                    if arr[k] < p:
                        arr[j], arr[k] = arr[k], arr[j]
                        j += 1
                    elif arr[k] >= q:
                        while arr[g] > q and k < g:
                            g -= 1
                        arr[k], arr[g] = arr[g], arr[k]
                        g -= 1
                        if arr[k] < p:
                            arr[j], arr[k] = arr[k], arr[j]
                            j += 1
                    k += 1
                j -= 1
                g += 1
                arr[low], arr[j] = arr[j], arr[low]
                arr[high], arr[g] = arr[g], arr[high]
                return j, g

            if low < high:
                lp, rp = partition(arr, low, high)
                cls.dual_pivot(arr, low, lp - 1)
                cls.dual_pivot(arr, lp + 1, rp - 1)
                cls.dual_pivot(arr, rp + 1, high)
            return arr

        @staticmethod
        def default(arr: list[int]) -> list[int]:
            """
            Sorts a list of integers using the default quicksort algorithm.

            Args:
                arr (list[int]): The list of integers to sort.

            Returns:
                list[int]: The sorted list of integers.
            """

            def partition(low, high):
                pivot = arr[high]
                i = low - 1
                for j in range(low, high):
                    if arr[j] <= pivot:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                return i + 1

            def quick_sort_recursive(low, high):
                if low < high:
                    pi = partition(low, high)
                    quick_sort_recursive(low, pi - 1)
                    quick_sort_recursive(pi + 1, high)

            quick_sort_recursive(0, len(arr) - 1)
            return arr

    class MergeSort:
        @classmethod
        def way3(cls, arr: list[int]) -> list[int]:
            """
            Sorts a list of integers using the 3-way merge sort algorithm.

            Args:
                arr (list[int]): The list of integers to sort.

            Returns:
                list[int]: The sorted list of integers.
            """

            def _3way(left, middle, right):
                result = []
                while left or middle or right:
                    min_val = min(
                        left[0] if left else float("inf"),
                        middle[0] if middle else float("inf"),
                        right[0] if right else float("inf"),
                    )
                    if left and min_val == left[0]:
                        result.append(left.pop(0))
                    elif middle and min_val == middle[0]:
                        result.append(middle.pop(0))
                    else:
                        result.append(right.pop(0))
                return result

            if len(arr) < 2:
                return arr
            third = len(arr) // 3
            left = cls.way3(arr[:third])
            middle = cls.way3(arr[third: 2 * third])
            right = cls.way3(arr[2 * third:])
            return _3way(left, middle, right)

        @classmethod
        def default(cls, arr: list[int]) -> list[int]:
            """
            Sorts a list of integers using the default merge sort algorithm.

            Args:
                arr (list[int]): The list of integers to sort.

            Returns:
                list[int]: The sorted list of integers.
            """
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                cls.default(left_half)
                cls.default(right_half)

                i = j = k = 0

                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1
            return arr

    class BogoSort:
        @staticmethod
        def __is_sorted(arr: list[int]) -> bool:
            """
            Checks if a list of integers is sorted.

            Args:
                arr (list[int]): The list of integers to check.

            Returns:
                bool: True if the list is sorted, False otherwise.
            """
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        @classmethod
        def default(cls, arr: list[int]) -> list[int]:
            """
            Sorts a list of integers using the bogo sort algorithm.

            Args:
                arr (list[int]): The list of integers to sort.

            Returns:
                list[int]: The sorted list of integers.
            """
            while not cls.__is_sorted(arr):
                random.shuffle(arr)
            return arr

        @classmethod
        def duo(cls, arr: list[int]) -> list[int]:
            """
            Sorts a list of integers using the duo bogo sort algorithm.

            Args:
                arr (list[int]): The list of integers to sort.

            Returns:
                list[int]: The sorted list of integers.
            """

            def bogosort(arr: list[int]):
                while not cls.__is_sorted(arr):
                    random.shuffle(arr)

            for i in range(len(arr)):
                if not cls.__is_sorted(arr[: i + 1]):
                    bogosort(arr[: i + 1])
            return arr

    @staticmethod
    def selection_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the selection sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the insertion sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def heap_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the heap sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """

        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[i] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(i, 0)
        return arr

    @staticmethod
    def radix_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the radix sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        if not arr:
            return arr

        def counting_sort(exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]

        max1 = max(arr)
        exp = 1
        while max1 // exp > 0:
            counting_sort(exp)
            exp *= 10
        return arr

    @staticmethod
    def counting_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the counting sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        if not arr:
            return arr
        max_val = max(arr)
        m = max_val + 1
        count = [0] * m

        for a in arr:
            count[a] += 1

        i = 0
        for a in range(m):
            for _ in range(count[a]):
                arr[i] = a
                i += 1
        return arr

    @classmethod
    def bucket_sort(cls, arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the bucket sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        if len(arr) == 0:
            return arr

        bucket_count = len(arr)
        max_val = max(arr)
        min_val = min(arr)

        buckets = [[] for _ in range(bucket_count)]

        for i in range(len(arr)):
            idx = int(bucket_count * (arr[i] - min_val) / (max_val - min_val + 1))
            buckets[idx].append(arr[i])

        for i in range(bucket_count):
            buckets[i] = cls.insertion_sort(buckets[i])

        result = []
        for i in range(bucket_count):
            result.extend(buckets[i])

        return result

    @staticmethod
    def shell_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the shell sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    @staticmethod
    def cocktail_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the cocktail sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            start += 1
        return arr

    @staticmethod
    def comb_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the comb sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """

        def get_next_gap(gap):
            gap = (gap * 10) // 13
            if gap < 1:
                return 1
            return gap

        n = len(arr)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            gap = get_next_gap(gap)
            swapped = False

            for i in range(0, n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
        return arr

    @staticmethod
    def gnome_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the gnome sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        n = len(arr)
        index = 0

        while index < n:
            if index == 0 or arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1
        return arr

    @staticmethod
    def pancake_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the pancake sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """

        def flip(arr, i):
            """
            Reverses the order of the first i+1 elements in the array.

            Args:
                arr (list[int]): The list of integers.
                i (int): The index up to which to reverse the elements.
            """
            start = 0
            while start < i:
                arr[start], arr[i] = arr[i], arr[start]
                start += 1
                i -= 1

        def find_max(arr, n):
            """
            Finds the index of the maximum element in the first n elements of the array.

            Args:
                arr (list[int]): The list of integers.
                n (int): The number of elements to consider.

            Returns:
                int: The index of the maximum element.
            """
            mi = 0
            for i in range(0, n):
                if arr[i] > arr[mi]:
                    mi = i
            return mi

        n = len(arr)
        for curr_size in range(n, 1, -1):
            mi = find_max(arr, curr_size)
            if mi != curr_size - 1:
                flip(arr, mi)
                flip(arr, curr_size - 1)
        return arr

    @classmethod
    def stooge_sort(cls, arr: list[int], left: int = 0, right: int = None) -> list[int]:
        """
        Sorts a list of integers using the stooge sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.
            left (int): The starting index of the list to sort.
            right (int): The ending index of the list to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        if right is None:
            right = len(arr) - 1

        if left >= right:
            return arr

        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        if right - left + 1 > 2:
            t = (right - left + 1) // 3
            cls.stooge_sort(arr, left, right - t)
            cls.stooge_sort(arr, left + t, right)
            cls.stooge_sort(arr, left, right - t)
        return arr if arr else None

    @staticmethod
    def cycle_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the cycle sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        writes = 0

        for cycleStart in range(0, len(arr) - 1):
            item = arr[cycleStart]

            pos = cycleStart
            for i in range(cycleStart + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            if pos == cycleStart:
                continue

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1

            while pos != cycleStart:
                pos = cycleStart
                for i in range(cycleStart + 1, len(arr)):
                    if arr[i] < item:
                        pos += 1

                while item == arr[pos]:
                    pos += 1
                arr[pos], item = item, arr[pos]
                writes += 1
        return arr

    @staticmethod
    def library_sort(arr: list) -> list[int] | list[None]:
        """
        Sorts a list of integers using the library sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int] | list[None]: The sorted list of integers or None if the list is empty.
        """
        if len(arr) <= 1:
            return arr

        sorted_arr = [None] * (2 * len(arr))
        sorted_arr[0] = arr[0]
        length = 1

        for i in range(1, len(arr)):
            pos = min(length, i + 1)
            while pos > 0 and (
                    sorted_arr[pos - 1] is None or sorted_arr[pos - 1] > arr[i]
            ):
                pos -= 1
            for j in range(length, pos, -1):
                sorted_arr[j] = sorted_arr[j - 1]
            sorted_arr[pos] = arr[i]
            length += 1

        return [x for x in sorted_arr if x is not None]

    @staticmethod
    def strand_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the strand sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """

        def merge(left, right):
            """
            Merges two sorted lists into one sorted list.

            Args:
                left (list[int]): The first sorted list.
                right (list[int]): The second sorted list.

            Returns:
                list[int]: The merged sorted list.
            """
            result = []
            while len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            result += left
            result += right
            return result

        if len(arr) == 0:
            return arr

        result = []

        while len(arr) != 0:
            i = 0
            sublist = [arr.pop(0)]
            while i < len(arr):
                if arr[i] > sublist[-1]:
                    sublist.append(arr.pop(i))
                else:
                    i += 1

            result = merge(result, sublist)
        return result

    @staticmethod
    def tim_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the tim sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        return sorted(arr)

    @staticmethod
    def block_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the block sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        if len(arr) == 0:
            return arr
        num_blocks = int(len(arr) ** 0.5)
        blocks = [[] for _ in range(num_blocks)]

        for x in arr:
            blocks[int(x * num_blocks / (max(arr) + 1))].append(x)

        for i in range(num_blocks):
            blocks[i].sort()

        sorted_arr = []
        for block in blocks:
            sorted_arr.extend(block)

        return sorted_arr

    @staticmethod
    def tournament_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the tournament sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """

        def play_tournament(arr):
            """
            Plays a tournament to find the smallest element in the array.

            Args:
                arr (list[int]): The list of integers.

            Returns:
                tuple[int, list[int]]: The smallest element and the remaining elements.
            """
            if len(arr) == 1:
                return arr[0], []
            mid = len(arr) // 2
            left_winner, left_remaining = play_tournament(arr[:mid])
            right_winner, right_remaining = play_tournament(arr[mid:])
            if left_winner < right_winner:
                return left_winner, right_remaining + [right_winner] + left_remaining
            else:
                return right_winner, left_remaining + [left_winner] + right_remaining

        sorted_arr = []
        remaining = arr
        while remaining:
            winner, remaining = play_tournament(remaining)
            sorted_arr.append(winner)
        return sorted_arr

    @staticmethod
    def intro_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the introspective sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """

        def _intro_sort(arr, start, end, max_depth):
            """
            Helper function for performing introspective sort.

            Args:
                arr (list[int]): The list of integers to sort.
                start (int): The starting index of the list to sort.
                end (int): The ending index of the list to sort.
                max_depth (int): The maximum depth for recursion.
            """
            if end - start <= 1:
                return
            elif max_depth == 0:
                heapsort(arr, start, end)
            else:
                pivot = partition(arr, start, end)
                _intro_sort(arr, start, pivot, max_depth - 1)
                _intro_sort(arr, pivot + 1, end, max_depth - 1)

        def partition(arr, start, end):
            """
            Partitions the list around a pivot element.

            Args:
                arr (list[int]): The list of integers to partition.
                start (int): The starting index of the list to partition.
                end (int): The ending index of the list to partition.

            Returns:
                int: The index of the pivot element.
            """
            pivot = arr[start]
            left = start + 1
            right = end - 1
            done = False
            while not done:
                while left <= right and arr[left] <= pivot:
                    left += 1
                while arr[right] >= pivot and right >= left:
                    right -= 1
                if right < left:
                    done = True
                else:
                    arr[left], arr[right] = arr[right], arr[left]
            arr[start], arr[right] = arr[right], arr[start]
            return right

        def heapsort(arr, start, end):
            """
            Sorts a portion of the list using heap sort.

            Args:
                arr (list[int]): The list of integers to sort.
                start (int): The starting index of the list to sort.
                end (int): The ending index of the list to sort.
            """
            heap = []
            for i in range(start, end):
                heappush(heap, arr[i])
            for i in range(start, end):
                arr[i] = heappop(heap)

        if len(arr) == 0 or not arr:
            return arr
        max_depth = int(math.log2(len(arr))) * 2
        _intro_sort(arr, 0, len(arr), max_depth)
        return arr

    @classmethod
    def un_shuffle_sort(cls, arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the un-shuffle sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        if len(arr) <= 1:
            return arr

        evens = arr[::2]
        odds = arr[1::2]

        sorted_evens = cls.un_shuffle_sort(evens)
        sorted_odds = cls.un_shuffle_sort(odds)

        result = []
        while sorted_evens or sorted_odds:
            if sorted_evens and (not sorted_odds or sorted_evens[0] <= sorted_odds[0]):
                result.append(sorted_evens.pop(0))
            else:
                result.append(sorted_odds.pop(0))

        return result

    @staticmethod
    def sleep_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the sleep sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        result = []

        def sleep_and_append(x):
            """
            Sleeps for a duration equal to the value and appends the value to the result list.

            Args:
                x (int): The value to sleep for and append.
            """
            time.sleep(x)
            result.append(x)

        threads = [threading.Thread(target=sleep_and_append, args=(x,)) for x in arr]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        return result

    @staticmethod
    def stupid_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the stupid sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        i = 0
        while i < len(arr):
            if i == 0 or arr[i] >= arr[i - 1]:
                i += 1
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        return arr

    @staticmethod
    def slow_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the slow sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """

        def _slow_sort(arr, i, j):
            """
            Helper function for performing slow sort.

            Args:
                arr (list[int]): The list of integers to sort.
                i (int): The starting index of the list to sort.
                j (int): The ending index of the list to sort.
            """
            if i >= j:
                return
            m = (i + j) // 2
            _slow_sort(arr, i, m)
            _slow_sort(arr, m + 1, j)
            if arr[m] > arr[j]:
                arr[m], arr[j] = arr[j], arr[m]
            _slow_sort(arr, i, j - 1)

        _slow_sort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def odd_even_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the odd-even sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        n = len(arr)
        sorted_arr = False
        while not sorted_arr:
            sorted_arr = True
            for i in range(1, n - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    sorted_arr = False
            for i in range(0, n - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    sorted_arr = False
        return arr

    @staticmethod
    def bingo_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the bingo sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        n = len(arr)
        while n > 0:
            new_n = 0
            for i in range(1, n):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    new_n = i
            n = new_n
        return arr

    @staticmethod
    def pigeonhole_sort(arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the pigeonhole sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            list[int]: The sorted list of integers.
        """
        if not arr:
            return arr
        min_val = min(arr)
        max_val = max(arr)
        size = max_val - min_val + 1

        holes = [0] * size
        for x in arr:
            holes[x - min_val] += 1

        i = 0
        for count in range(size):
            while holes[count] > 0:
                arr[i] = count + min_val
                i += 1
                holes[count] -= 1
        return arr

    @staticmethod
    def tag_sort(arr: list[int]) -> tuple[list[int], list[int]]:
        """
        Sorts a list of integers using the tag sort algorithm.

        Args:
            arr (list[int]): The list of integers to sort.

        Returns:
            tuple[list[int], list[int]]: A tuple containing the sorted list of integers and the original indices.
        """
        tagged_arr = list(enumerate(arr))
        tagged_arr.sort(key=lambda x: x[1])
        sorted_arr = [x[1] for x in tagged_arr]
        original_arr = [x[0] for x in tagged_arr]
        return sorted_arr, original_arr

    class BinaryTree:
        class _Node:
            """
            Represents a node in a binary tree.

            Attributes:
                value (int): The value stored in the node.
                left (Optional[Sort.BinaryTree._Node]): The left child of the node.
                right (Optional[Sort.BinaryTree._Node]): The right child of the node.
                key (int): The key of the node, same as value.
            """

            def __init__(self, value: int) -> None:
                self.value: int = value
                self.left: Optional[Sort.BinaryTree._Node] = None
                self.right: Optional[Sort.BinaryTree._Node] = None
                self.key: int = value

        class _AVLNode:
            """
            Represents a node in an AVL tree.

            Attributes:
                key (int): The key stored in the node.
                left (Optional[Sort.BinaryTree._AVLNode]): The left child of the node.
                right (Optional[Sort.BinaryTree._AVLNode]): The right child of the node.
                height (int): The height of the node.
            """

            def __init__(self, key: int) -> None:
                self.key: int = key
                self.left: Optional[Sort.BinaryTree._AVLNode] = None
                self.right: Optional[Sort.BinaryTree._AVLNode] = None
                self.height: int = 1

        class _RBNode:
            """
            Represents a node in a Red-Black tree.

            Attributes:
                data (Optional[int]): The data stored in the node.
                color (str): The color of the node, either "red" or "black".
                left (Optional[Sort.BinaryTree._RBNode]): The left child of the node.
                right (Optional[Sort.BinaryTree._RBNode]): The right child of the node.
                parent (Optional[Sort.BinaryTree._RBNode]): The parent of the node.
            """

            def __init__(self, data: Optional[int], color: str = "red") -> None:
                self.data: Optional[int] = data
                self.color: str = color
                self.left: Optional[Sort.BinaryTree._RBNode] = None
                self.right: Optional[Sort.BinaryTree._RBNode] = None
                self.parent: Optional[Sort.BinaryTree._RBNode] = None

        class _BPlusTreeNode:
            """
            Represents a node in a B+ tree.

            Attributes:
                is_leaf (bool): Indicates if the node is a leaf.
                keys (List[int]): The keys stored in the node.
                children (List[Sort.BinaryTree._BPlusTreeNode]): The children of the node.
            """

            def __init__(self, is_leaf: bool = False) -> None:
                self.is_leaf: bool = is_leaf
                self.keys: List[int] = []
                self.children: List[Sort.BinaryTree._BPlusTreeNode] = []

        class AVL:
            @classmethod
            def insert(cls, root, key: int):
                """
                Inserts a key into the AVL tree and balances the tree if necessary.

                Args:
                    root (Sort.BinaryTree._AVLNode): The root of the AVL tree.
                    key (int): The key to insert.

                Returns:
                    Sort.BinaryTree._AVLNode: The new root of the AVL tree.
                """
                if not isinstance(root, Sort.BinaryTree._AVLNode) and root is not None:
                    raise TypeError(
                        "Root must be an instance of Sort.BinaryTree._AVLNode"
                    )
                if not root:
                    return Sort.BinaryTree._AVLNode(key)
                if key < root.key:
                    root.left = cls.insert(root.left, key)
                else:
                    root.right = cls.insert(root.right, key)

                root.height = 1 + max(
                    cls._Get.height(root.left), cls._Get.height(root.right)
                )
                balance = cls._Get.balance(root)

                if balance > 1:
                    if key < root.left.key:
                        return cls.__right_rotate(root)
                    root.left = cls.__left_rotate(root.left)
                    return cls.__right_rotate(root)
                if balance < -1:
                    if key > root.right.key:
                        return cls.__left_rotate(root)
                    root.right = cls.__right_rotate(root.right)
                    return cls.__left_rotate(root)

                return root

            @classmethod
            def delete(cls, root, key: int):
                """
                Deletes a key from the AVL tree and balances the tree if necessary.

                Args:
                    root (Sort.BinaryTree._AVLNode): The root of the AVL tree.
                    key (int): The key to delete.

                Returns:
                    Sort.BinaryTree._AVLNode: The new root of the AVL tree.
                """
                if not isinstance(root, Sort.BinaryTree._AVLNode):
                    raise TypeError(
                        "Root must be an instance of Sort.BinaryTree._AVLNode"
                    )
                if not root:
                    return root
                if key < root.key:
                    root.left = cls.delete(root.left, key)
                elif key > root.key:
                    root.right = cls.delete(root.right, key)
                else:
                    if not root.left:
                        return root.right
                    if not root.right:
                        return root.left

                    temp = cls.__min_value_node(root.right)
                    root.key = temp.key
                    root.right = cls.delete(root.right, temp.key)

                root.height = 1 + max(
                    cls._Get.height(root.left), cls._Get.height(root.right)
                )
                balance = cls._Get.balance(root)

                if balance > 1:
                    if cls._Get.balance(root.left) >= 0:
                        return cls.__right_rotate(root)
                    root.left = cls.__left_rotate(root.left)
                    return cls.__right_rotate(root)
                if balance < -1:
                    if cls._Get.balance(root.right) <= 0:
                        return cls.__left_rotate(root)
                    root.right = cls.__right_rotate(root.right)
                    return cls.__left_rotate(root)

                return root

            @classmethod
            def __rotate(cls, z, direction: str):
                """
                Rotates the subtree rooted at z in the specified direction.

                Args:
                    z (Sort.BinaryTree._AVLNode): The root of the subtree to rotate.
                    direction (str): The direction to rotate ('left' or 'right').

                Returns:
                    Sort.BinaryTree._AVLNode: The new root of the rotated subtree.
                """
                if not isinstance(z, Sort.BinaryTree._AVLNode):
                    raise TypeError("Z must be an instance of Sort.BinaryTree._AVLNode")
                y = getattr(z, direction)
                setattr(
                    z,
                    direction,
                    getattr(y, "left" if direction == "right" else "right"),
                )
                setattr(y, "left" if direction == "right" else "right", z)
                z.height = 1 + max(cls._Get.height(z.left), cls._Get.height(z.right))
                y.height = 1 + max(cls._Get.height(y.left), cls._Get.height(y.right))
                return y

            @classmethod
            def __left_rotate(cls, z):
                """
                Performs a left rotation on the subtree rooted at z.

                Args:
                    z (Sort.BinaryTree._AVLNode): The root of the subtree to rotate.

                Returns:
                    Sort.BinaryTree._AVLNode: The new root of the rotated subtree.
                """
                if not isinstance(z, Sort.BinaryTree._AVLNode):
                    raise TypeError("Z must be an instance of Sort.BinaryTree._AVLNode")
                return cls.__rotate(z, "right")

            @classmethod
            def __right_rotate(cls, z):
                """
                Performs a right rotation on the subtree rooted at z.

                Args:
                    z (Sort.BinaryTree._AVLNode): The root of the subtree to rotate.

                Returns:
                    Sort.BinaryTree._AVLNode: The new root of the rotated subtree.
                """
                if not isinstance(z, Sort.BinaryTree._AVLNode):
                    raise TypeError("Z must be an instance of Sort.BinaryTree._AVLNode")
                return cls.__rotate(z, "left")

            @classmethod
            def pre_order(cls, root) -> str:
                """
                Returns a string representation of the pre-order traversal of the AVL tree.

                Args:
                    root (Sort.BinaryTree._AVLNode): The root of the AVL tree.

                Returns:
                    str: The pre-order traversal of the AVL tree.
                """
                if not isinstance(root, Sort.BinaryTree._AVLNode):
                    raise TypeError(
                        "Root must be an instance of Sort.BinaryTree._AVLNode"
                    )
                result: List[str] = []
                cls._pre_order_helper(root, result)
                return " ".join(result)

            @classmethod
            def _pre_order_helper(cls, root, result: List[str]) -> None:
                """
                Helper function for pre-order traversal.

                Args:
                    root (Sort.BinaryTree._AVLNode): The root of the AVL tree.
                    result (List[str]): The list to store the traversal result.
                """
                if not isinstance(root, Sort.BinaryTree._AVLNode) and root is not None:
                    raise TypeError(
                        "Root must be an instance of Sort.BinaryTree._AVLNode"
                    )
                if root:
                    result.append(str(root.key))
                    cls._pre_order_helper(root.left, result)
                    cls._pre_order_helper(root.right, result)

            @classmethod
            def __min_value_node(cls, root):
                """
                Finds the node with the minimum key in the subtree rooted at root.

                Args:
                    root (Sort.BinaryTree._AVLNode): The root of the subtree.

                Returns:
                    Sort.BinaryTree._AVLNode: The node with the minimum key.
                """
                if not isinstance(root, Sort.BinaryTree._AVLNode):
                    raise TypeError(
                        "Root must be an instance of Sort.BinaryTree._AVLNode"
                    )
                while root.left:
                    root = root.left
                return root

            class _Get:
                @staticmethod
                def height(root) -> int:
                    """
                    Returns the height of the node.

                    Args:
                        root (Sort.BinaryTree._AVLNode): The node to get the height of.

                    Returns:
                        int: The height of the node.
                    """
                    if (
                            not isinstance(root, Sort.BinaryTree._AVLNode)
                            and root is not None
                    ):
                        raise TypeError(
                            "Root must be an instance of Sort.BinaryTree._AVLNode"
                        )
                    return root.height if root else 0

                @classmethod
                def balance(cls, root):
                    """
                    Returns the balance factor of the node.

                    Args:
                        root (Sort.BinaryTree._AVLNode): The node to get the balance factor of.

                    Returns:
                        int: The balance factor of the node.
                    """
                    if not isinstance(root, Sort.BinaryTree._AVLNode):
                        raise TypeError(
                            "Root must be an instance of Sort.BinaryTree._AVLNode"
                        )
                    return cls.height(root.left) - cls.height(root.right) if root else 0

        class Degenerate:
            """
            Represents a degenerate (linked list-like) binary tree.
            """

            @classmethod
            def __init__(cls) -> None:
                """
                Initializes the Degenerate tree with an empty root.
                """
                cls.root: Optional[Sort.BinaryTree._Node] = None

            @classmethod
            def insert(cls, key: int) -> None:
                """
                Inserts a key into the degenerate tree.

                Args:
                    key (int): The key to insert.
                """
                if not cls.root:
                    cls.root = Sort.BinaryTree._Node(key)
                else:
                    current = cls.root
                    while current.right:
                        current = current.right
                    current.right = Sort.BinaryTree._Node(key)

            @classmethod
            def search(cls, key: int) -> bool:
                """
                Searches for a key in the degenerate tree.

                Args:
                    key (int): The key to search for.

                Returns:
                    bool: True if the key is found, False otherwise.
                """
                current = cls.root
                while current:
                    if current.key == key:
                        return True
                    current = current.right
                return False

            @classmethod
            def delete(cls, key: int) -> None:
                """
                Deletes a key from the degenerate tree.

                Args:
                    key (int): The key to delete.
                """
                if not cls.root:
                    return
                if cls.root.key == key:
                    cls.root = cls.root.right
                    return
                current = cls.root
                while current.right:
                    if current.right.key == key:
                        current.right = current.right.right
                        return
                    current = current.right

            @classmethod
            def traverse(cls) -> str:
                """
                Traverses the degenerate tree and returns a string representation.

                Returns:
                    str: A string representation of the tree.
                """
                result: List[str] = []
                current = cls.root
                while current:
                    result.append(str(current.key))
                    current = current.right
                result.append("None")
                return " -> ".join(result)

        class Perfect:
            """
            Represents a perfect binary tree.
            """

            @classmethod
            def __init__(cls, height: int) -> None:
                """
                Initializes the Perfect binary tree with a given height.

                Args:
                    height (int): The height of the perfect binary tree.
                """
                cls.height: int = height
                cls.nodes: List[Optional[Sort.BinaryTree._Node]] = [None] * (
                        2 ** height - 1
                )

            @classmethod
            def create(cls) -> None:
                """
                Creates the perfect binary tree.
                """
                cls.__create(0)

            @classmethod
            def __create(cls, index: int) -> None:
                """
                Recursively creates nodes for the perfect binary tree.

                Args:
                    index (int): The current index in the nodes list.
                """
                if index < len(cls.nodes):
                    cls.__create(2 * index + 1)
                    cls.nodes[index] = Sort.BinaryTree._Node(index)
                    cls.__create(2 * index + 2)

            @classmethod
            def return_tree(cls) -> str:
                """
                Returns a string representation of the perfect binary tree.

                Returns:
                    str: The string representation of the tree.
                """
                levels: List[List[Optional[Sort.BinaryTree._Node]]] = []
                cls.__print_tree(0, 0, levels)
                return cls.__format_tree(levels)

            @staticmethod
            def __format_tree(levels) -> str:
                """
                Formats the levels of the tree into a string.

                Args:
                    levels (list): The levels of the tree.

                Returns:
                    str: The formatted string representation of the tree.
                """
                if not isinstance(levels, list) or not all(
                        isinstance(level, list) for level in levels
                ):
                    raise TypeError(
                        "levels must be an instance of Sort.BinaryTree._Node"
                    )
                if not levels:
                    return ""
                tree_str = ""
                max_width = len(
                    " ".join(str(node.value) if node else "None" for node in levels[-1])
                )
                for level in levels:
                    level_str = " ".join(
                        str(node.value) if node else "None" for node in level
                    )
                    tree_str += level_str.center(max_width) + "\n"
                return tree_str.replace("None", " ")

            @classmethod
            def return_list(cls) -> List[Optional[int]]:
                """
                Returns a list of node values in the perfect binary tree.

                Returns:
                    list[Optional[int]]: The list of node values.
                """
                return [node.value if node else None for node in cls.nodes]

            @classmethod
            def __print_tree(cls, index: int, level: int, levels) -> None:
                """
                Recursively prints the tree levels.

                Args:
                    index (int): The current index in the nodes list.
                    level (int): The current level in the tree.
                    levels (list): The list to store the levels of the tree.
                """
                if index < len(cls.nodes):
                    if len(levels) == level:
                        levels.append([])
                    levels[level].append(cls.nodes[index])
                    cls.__print_tree(2 * index + 1, level + 1, levels)
                    cls.__print_tree(2 * index + 2, level + 1, levels)

        class RedBlackTree:
            """
            Represents a Red-Black Tree.
            """

            @classmethod
            def __init__(cls) -> None:
                """
                Initializes the Red-Black Tree with a NIL node.
                """
                cls.NIL: Sort.BinaryTree._RBNode = Sort.BinaryTree._RBNode(
                    data=None, color="black"
                )
                cls.root: Sort.BinaryTree._RBNode = cls.NIL

            @classmethod
            def insert(cls, key: int) -> None:
                """
                Inserts a new node with the given key into the Red-Black Tree.

                Args:
                    key (int): The key to insert.
                """
                new_node = Sort.BinaryTree._RBNode(key)
                new_node.left = cls.NIL
                new_node.right = cls.NIL
                parent: Optional[Sort.BinaryTree._RBNode] = None
                current: Sort.BinaryTree._RBNode = cls.root

                while current != cls.NIL:
                    parent = current
                    if new_node.data < current.data:
                        current = current.left
                    else:
                        current = current.right

                new_node.parent = parent
                if not parent:
                    cls.root = new_node
                elif new_node.data < parent.data:
                    parent.left = new_node
                else:
                    parent.right = new_node

                new_node.color = "red"
                cls.insert_fixup(new_node)

            @classmethod
            def insert_fixup(cls, node) -> None:
                """
                Fixes the Red-Black Tree after insertion to maintain its properties.

                Args:
                    node (Sort.BinaryTree._RBNode): The node to fix up.
                """
                if not isinstance(node, Sort.BinaryTree._RBNode):
                    raise TypeError(
                        "node must be an instance of Sort.BinaryTree._RBNode"
                    )
                while node != cls.root and node.parent.color == "red":
                    if node.parent == node.parent.parent.left:
                        uncle = node.parent.parent.right
                        if uncle.color == "red":
                            node.parent.color = "black"
                            uncle.color = "black"
                            node.parent.parent.color = "red"
                            node = node.parent.parent
                        else:
                            if node == node.parent.right:
                                node = node.parent
                                cls.left_rotate(node)
                            node.parent.color = "black"
                            node.parent.parent.color = "red"
                            cls.right_rotate(node.parent.parent)
                    else:
                        uncle = node.parent.parent.left
                        if uncle.color == "red":
                            node.parent.color = "black"
                            uncle.color = "black"
                            node.parent.parent.color = "red"
                            node = node.parent.parent
                        else:
                            if node == node.parent.left:
                                node = node.parent
                                cls.right_rotate(node)
                            node.parent.color = "black"
                            node.parent.parent.color = "red"
                            cls.left_rotate(node.parent.parent)
                cls.root.color = "black"

            @classmethod
            def rotate(cls, node, direction: str) -> None:
                """
                Rotates the subtree rooted at the given node in the specified direction.

                Args:
                    node (Sort.BinaryTree._RBNode): The root of the subtree to rotate.
                    direction (str): The direction to rotate ('left' or 'right').
                """
                if not isinstance(node, Sort.BinaryTree._RBNode):
                    raise TypeError(
                        "node must be an instance of Sort.BinaryTree._RBNode"
                    )
                opposite = "left" if direction == "right" else "right"
                child = getattr(node, direction)
                setattr(node, direction, getattr(child, opposite))
                if getattr(child, opposite) != cls.NIL:
                    getattr(child, opposite).parent = node
                child.parent = node.parent
                if not node.parent:
                    cls.root = child
                elif node == getattr(node.parent, opposite):
                    setattr(node.parent, opposite, child)
                else:
                    setattr(node.parent, direction, child)
                setattr(child, opposite, node)
                node.parent = child

            @classmethod
            def left_rotate(cls, x) -> None:
                """
                Performs a left rotation on the subtree rooted at the given node.

                Args:
                    x (Sort.BinaryTree._RBNode): The root of the subtree to rotate.
                """
                if not isinstance(x, Sort.BinaryTree._RBNode):
                    raise TypeError("x must be an instance of Sort.BinaryTree._RBNode")
                cls.rotate(x, "right")

            @classmethod
            def right_rotate(cls, y) -> None:
                """
                Performs a right rotation on the subtree rooted at the given node.

                Args:
                    y (Sort.BinaryTree._RBNode): The root of the subtree to rotate.
                """
                if not isinstance(y, Sort.BinaryTree._RBNode):
                    raise TypeError("y must be an instance of Sort.BinaryTree._RBNode")
                cls.rotate(y, "left")

            @classmethod
            def __repr__(cls) -> str:
                """
                Returns a string representation of the Red-Black Tree.

                Returns:
                    str: A string representation of the tree.
                """

                def recurse(node: Sort.BinaryTree._RBNode) -> List[Optional[int]]:
                    if node == cls.NIL:
                        return []
                    return recurse(node.left) + [node.data] + recurse(node.right)

                return str(recurse(cls.root))

        class BPlusTree:
            """
            Represents a B+ Tree.

            Attributes:
                root (Sort.BinaryTree._BPlusTreeNode): The root node of the B+ tree.
                t (int): The minimum degree of the B+ tree.
            """

            @classmethod
            def __init__(cls, t: int = 3) -> None:
                """
                Initializes the B+ tree with a given minimum degree.

                Args:
                    t (int): The minimum degree of the B+ tree. Default is 3.
                """
                cls.root: Sort.BinaryTree._BPlusTreeNode = (
                    Sort.BinaryTree._BPlusTreeNode(is_leaf=True)
                )
                cls.t: int = t

            @classmethod
            def insert(cls, key: int) -> None:
                """
                Inserts a key into the B+ tree.

                Args:
                    key (int): The key to insert.
                """
                root = cls.root
                if len(root.keys) == (2 * cls.t) - 1:
                    temp = Sort.BinaryTree._BPlusTreeNode()
                    cls.root = temp
                    temp.children.append(root)
                    cls.split_child(temp, 0)
                    cls.insert_non_full(temp, key)
                else:
                    cls.insert_non_full(root, key)

            @classmethod
            def insert_non_full(cls, node, key: int) -> None:
                """
                Inserts a key into a non-full node of the B+ tree.

                Args:
                    node (Sort.BinaryTree._BPlusTreeNode): The node to insert the key into.
                    key (int): The key to insert.
                """
                if not isinstance(node, Sort.BinaryTree._BPlusTreeNode):
                    raise TypeError(
                        "node must be an instance of Sort.BinaryTree._BPlusTreeNode"
                    )
                if node.is_leaf:
                    node.keys.append(key)
                    node.keys.sort()
                else:
                    i = len(node.keys) - 1
                    while i >= 0 and key < node.keys[i]:
                        i -= 1
                    i += 1
                    if len(node.children[i].keys) == (2 * cls.t) - 1:
                        cls.split_child(node, i)
                        if key > node.keys[i]:
                            i += 1
                    cls.insert_non_full(node.children[i], key)

            @classmethod
            def split_child(cls, node, i: int) -> None:
                """
                Splits a child node of the B+ tree.

                Args:
                    node (Sort.BinaryTree._BPlusTreeNode): The node whose child is to be split.
                    i (int): The index of the child to split.
                """
                if not isinstance(node, Sort.BinaryTree._BPlusTreeNode):
                    raise TypeError(
                        "node must be an instance of Sort.BinaryTree._BPlusTreeNode"
                    )
                t = cls.t
                y = node.children[i]
                z = Sort.BinaryTree._BPlusTreeNode(is_leaf=y.is_leaf)
                node.children.insert(i + 1, z)
                node.keys.insert(i, y.keys[t - 1])
                z.keys = y.keys[t: (2 * t) - 1]
                y.keys = y.keys[0: t - 1]
                if not y.is_leaf:
                    z.children = y.children[t: (2 * t)]
                    y.children = y.children[0:t]

            @classmethod
            def search(cls, key: int, node=None) -> bool:
                """
                Searches for a key in the B+ tree.

                Args:
                    key (int): The key to search for.
                    node (Sort.BinaryTree._BPlusTreeNode, optional): The node to start the search from. Defaults to None.

                Returns:
                    bool: True if the key is found, False otherwise.
                """
                if (
                        not isinstance(node, Sort.BinaryTree._BPlusTreeNode)
                        and node is not None
                ):
                    raise TypeError(
                        "node must be an instance of Sort.BinaryTree._BPlusTreeNode"
                    )
                if not node:
                    node = cls.root
                i = 0
                while i < len(node.keys) and key > node.keys[i]:
                    i += 1
                if i < len(node.keys) and key == node.keys[i]:
                    return True
                if node.is_leaf:
                    return False
                return cls.search(key, node.children[i])

            @classmethod
            def traverse(cls, node=None, level: int = 0) -> List[str]:
                """
                Traverses the B+ tree and returns a list of strings representing the keys at each level.

                Args:
                    node (Sort.BinaryTree._BPlusTreeNode, optional): The node to start the traversal from. Defaults to None.
                    level (int): The current level in the tree. Defaults to 0.

                Returns:
                    List[str]: A list of strings representing the keys at each level.
                """
                if (
                        not isinstance(node, Sort.BinaryTree._BPlusTreeNode)
                        and node is not None
                ):
                    raise TypeError(
                        "node must be an instance of Sort.BinaryTree._BPlusTreeNode"
                    )
                if not node:
                    node = cls.root
                result = [f"Level {level}: " + " ".join(str(key) for key in node.keys)]
                if not node.is_leaf:
                    for child in node.children:
                        result.extend(cls.traverse(child, level + 1))
                return result

        class SegmentTree:
            """
            Represents a Segment Tree.

            Attributes:
                n (int): The size of the input data.
                tree (List[int]): The segment tree represented as a list.
            """

            @classmethod
            def __init__(cls, data: List[int]) -> None:
                """
                Initializes the Segment Tree with the given data.

                Args:
                    data (List[int]): The input data to build the segment tree from.
                """
                cls.n: int = len(data)
                cls.tree: List[int] = [0] * (2 * cls.n)
                cls.__build(data)

            @classmethod
            def __build(cls, data: List[int]) -> None:
                """
                Builds the segment tree from the given data.

                Args:
                    data (List[int]): The input data to build the segment tree from.
                """
                for i in range(cls.n):
                    cls.tree[cls.n + i] = data[i]
                for i in range(cls.n - 1, 0, -1):
                    cls.tree[i] = cls.tree[i * 2] + cls.tree[i * 2 + 1]

            @classmethod
            def update(cls, pos: int, value: int) -> None:
                """
                Updates the value at the given position in the segment tree.

                Args:
                    pos (int): The position to update.
                    value (int): The new value to set.
                """
                pos += cls.n
                cls.tree[pos] = value
                while pos > 1:
                    pos //= 2
                    cls.tree[pos] = cls.tree[2 * pos] + cls.tree[2 * pos + 1]

            @classmethod
            def query(cls, left: int, right: int) -> int:
                """
                Queries the sum of the values in the given range [left, right] in the segment tree.

                Args:
                    left (int): The left index of the range.
                    right (int): The right index of the range.

                Returns:
                    int: The sum of the values in the given range.
                """
                left += cls.n
                right += cls.n
                sum_query = 0
                while left <= right:
                    if left % 2 == 1:
                        sum_query += cls.tree[left]
                        left += 1
                    if right % 2 == 0:
                        sum_query += cls.tree[right]
                        right -= 1
                    left //= 2
                    right //= 2
                return sum_query

        class Default:
            def insert(self, root, key: int):
                """
                Inserts a key into the binary tree.

                Args:
                    root (Sort.BinaryTree._Node): The root node of the binary tree.
                    key (int): The key to insert.

                Returns:
                    Sort.BinaryTree._Node: The new root of the binary tree.
                """
                if not isinstance(root, Sort.BinaryTree._Node) and root is not None:
                    raise TypeError("root must be an instance of Sort.BinaryTree._Node")
                if root is None:
                    return Sort.BinaryTree._Node(key)
                if key < root.value:
                    root.left = self.insert(root.left, key)
                else:
                    root.right = self.insert(root.right, key)
                return root

            def inorder_traversal(self, root, sorted_list: List[int]) -> None:
                """
                Performs an inorder traversal of the binary tree and appends the values to the sorted list.

                Args:
                    root (Sort.BinaryTree._Node): The root node of the binary tree.
                    sorted_list (List[int]): The list to append the values to.
                """
                if not isinstance(root, Sort.BinaryTree._Node) and root is not None:
                    raise TypeError("root must be an instance of Sort.BinaryTree._Node")
                if root:
                    self.inorder_traversal(root.left, sorted_list)
                    sorted_list.append(root.value)
                    self.inorder_traversal(root.right, sorted_list)

            def tree_sort(self, arr: List[int]) -> List[int]:
                """
                Sorts a list of integers using the tree sort algorithm.

                Args:
                    arr (List[int]): The list of integers to sort.

                Returns:
                    List[int]: The sorted list of integers.
                """
                if not arr:
                    return arr
                root = Sort.BinaryTree._Node(arr[0])
                for value in arr[1:]:
                    self.insert(root, value)
                sorted_list: List[int] = []
                self.inorder_traversal(root, sorted_list)
                return sorted_list
