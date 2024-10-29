import math
import random
import threading
import time
from heapq import heappush, heappop


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
