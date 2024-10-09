import bisect
import random
import math
from heapq import heappush, heappop
import threading
import time


class Sort:
    class BubbleSort:
        @staticmethod
        def default(arr: list) -> list:
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        @staticmethod
        def with_flag(arr: list) -> list:
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
        def dual_pivot(cls, arr: list, low: int, high: int) -> list:
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
        def default(arr: list) -> list:
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
        def way3(cls, arr: list) -> list:
            def _3way(left, middle, right):
                result = []
                while left or middle or right:
                    min_val = min(left[0] if left else float('inf'),
                                  middle[0] if middle else float('inf'),
                                  right[0] if right else float('inf'))
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
            middle = cls.way3(arr[third:2 * third])
            right = cls.way3(arr[2 * third:])
            return _3way(left, middle, right)

        @classmethod
        def default(cls, arr: list) -> list:
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
        def __is_sorted(arr: list) -> bool:
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        @classmethod
        def default(cls, arr: list) -> list:
            while not cls.__is_sorted(arr):
                random.shuffle(arr)
            return arr

        @classmethod
        def duo(cls, arr: list) -> list:
            def bogosort(arr: list):
                while not cls.__is_sorted(arr):
                    random.shuffle(arr)

            for i in range(len(arr)):
                if not cls.__is_sorted(arr[:i + 1]):
                    bogosort(arr[:i + 1])
            return arr

    @staticmethod
    def selection_sort(arr: list) -> list:
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr: list) -> list:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def heap_sort(arr: list) -> list:
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
    def radix_sort(arr: list) -> list:
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
    def counting_sort(arr: list) -> list:
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
    def bucket_sort(cls, arr: list) -> list:
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
    def shell_sort(arr: list) -> list:
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
    def cocktail_sort(arr: list) -> list:
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
    def comb_sort(arr: list) -> list:
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
    def gnome_sort(arr: list) -> list:
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
    def pancake_sort(arr: list) -> list:
        def flip(arr, i):
            start = 0
            while start < i:
                arr[start], arr[i] = arr[i], arr[start]
                start += 1
                i -= 1

        def find_max(arr, n):
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
    def stooge_sort(cls, arr: list, left: int = 0, right: int = None) -> list | None:
        if right is None:
            right = len(arr) - 1

        if left >= right:
            return

        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        if right - left + 1 > 2:
            t = (right - left + 1) // 3
            cls.stooge_sort(arr, left, right - t)
            cls.stooge_sort(arr, left + t, right)
            cls.stooge_sort(arr, left, right - t)
        return arr

    @staticmethod
    def bitonic_sort(arr: list, up=True) -> list:
        def bitonic_merge(arr, low, cnt, up):
            if cnt > 1:
                k = cnt // 2
                for i in range(low, low + k):
                    if (up and arr[i] > arr[i + k]) or (not up and arr[i] < arr[i + k]):
                        arr[i], arr[i + k] = arr[i + k], arr[i]
                bitonic_merge(arr, low, k, up)
                bitonic_merge(arr, low + k, k, up)

        def bitonic_sort_recursive(arr, low, cnt, up):
            if cnt > 1:
                k = cnt // 2
                bitonic_sort_recursive(arr, low, k, True)
                bitonic_sort_recursive(arr, low + k, k, False)
                bitonic_merge(arr, low, cnt, up)

        bitonic_sort_recursive(arr, 0, len(arr), up)
        return arr

    @staticmethod
    def cycle_sort(arr: list) -> list:
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
    def library_sort(arr: list) -> list:
        if len(arr) <= 1:
            return arr

        sorted_arr = [None] * (2 * len(arr))
        sorted_arr[0] = arr[0]
        length = 1

        for i in range(1, len(arr)):
            pos = min(length, i + 1)
            while pos > 0 and (sorted_arr[pos - 1] is None or sorted_arr[pos - 1] > arr[i]):
                pos -= 1
            for j in range(length, pos, -1):
                sorted_arr[j] = sorted_arr[j - 1]
            sorted_arr[pos] = arr[i]
            length += 1

        return [x for x in sorted_arr if x is not None]

    @staticmethod
    def patience_sort(arr: list) -> list:
        piles = []
        for x in arr:
            new_pile = [x]
            i = bisect.bisect_left(piles, new_pile)
            if i != len(piles):
                piles[i].append(x)
            else:
                piles.append(new_pile)

        result = []
        while piles:
            smallest_pile = min(piles, key=lambda p: p[-1])
            result.append(smallest_pile.pop())
            if not smallest_pile:
                piles.remove(smallest_pile)
        return result[::-1]

    @staticmethod
    def strand_sort(arr: list) -> list:
        def merge(left, right):
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
    def tim_sort(arr: list) -> list:
        return sorted(arr)

    @staticmethod
    def block_sort(arr: list) -> list:
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
    def tournament_sort(arr: list) -> list:
        def play_tournament(arr):
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
    def spread_sort(arr: list) -> list:
        def _spread_sort(arr, start, end):
            if end - start < 2:
                return arr[start:end]
            mid = start + (end - start) // 2
            _spread_sort(arr, start, mid)
            _spread_sort(arr, mid, end)
            return _spread_merge(arr, start, mid, end)

        def _spread_merge(arr, start, mid, end):
            left = arr[start:mid]
            right = arr[mid:end]
            i = j = 0
            for k in range(start, end):
                if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1

        return _spread_sort(arr, 0, len(arr))

    @staticmethod
    def intro_sort(arr: list) -> list:
        def _intro_sort(arr, start, end, max_depth):
            if end - start <= 1:
                return
            elif max_depth == 0:
                heapsort(arr, start, end)
            else:
                pivot = partition(arr, start, end)
                _intro_sort(arr, start, pivot, max_depth - 1)
                _intro_sort(arr, pivot + 1, end, max_depth - 1)

        def partition(arr, start, end):
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
            heap = []
            for i in range(start, end):
                heappush(heap, arr[i])
            for i in range(start, end):
                arr[i] = heappop(heap)

        max_depth = int(math.log2(len(arr))) * 2
        _intro_sort(arr, 0, len(arr), max_depth)
        return arr

    @classmethod
    def un_shuffle_sort(cls, arr: list) -> list:
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
    def sleep_sort(arr: list) -> list:
        result = []

        def sleep_and_append(x):
            time.sleep(x)
            result.append(x)

        threads = [threading.Thread(target=sleep_and_append, args=(x,)) for x in arr]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        return result

    @staticmethod
    def stupid_sort(arr: list) -> list:
        i = 0
        while i < len(arr):
            if i == 0 or arr[i] >= arr[i - 1]:
                i += 1
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        return arr

    @staticmethod
    def slow_sort(arr: list) -> list:
        def _slow_sort(arr, i, j):
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
    def odd_even_sort(arr: list) -> list:
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
    def smooth_sort(arr: list) -> list:
        def sift(lo, hi):
            while hi - lo > 1:
                if arr[hi - 1] > arr[hi]:
                    hi -= 1
                if arr[hi] <= arr[lo]:
                    break
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo = hi
                hi = 2 * lo + 1

        def trinkle(lo, hi):
            while lo < hi:
                if arr[hi] <= arr[lo]:
                    break
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo = hi
                hi = 2 * lo + 1
            sift(lo, hi)

        def semi_trinkle(lo, hi):
            if lo < hi:
                arr[lo], arr[hi] = arr[hi], arr[lo]
                trinkle(lo, hi)

        def smooth_sort(arr: list) -> list:
            lo, hi = 0, 1
            while hi < len(arr):
                if hi - lo == 1:
                    sift(lo, hi)
                else:
                    trinkle(lo, hi)
                    semi_trinkle(lo, hi)
                hi += 1
            while lo < len(arr):
                sift(lo, len(arr) - 1)
                lo += 1
            return arr

        return smooth_sort(arr)

    @staticmethod
    def bingo_sort(arr: list) -> list:
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
    def pigeonhole_sort(arr: list) -> list:
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
    def tag_sort(arr: list) -> tuple[list, list[int]]:
        tagged_arr = list(enumerate(arr))
        tagged_arr.sort(key=lambda x: x[1])
        sorted_arr = [x[1] for x in tagged_arr]
        original_arr = [x[0] for x in tagged_arr]
        return sorted_arr, original_arr

    @staticmethod
    def flash_sort(arr: list) -> list:
        n = len(arr)
        if n == 0:
            return arr
        m = int(0.45 * n)
        min_val = min(arr)
        max_val = max(arr)
        if min_val == max_val:
            return arr
        line = [0] * m
        for num in arr:
            line[int((m - 1) * (num - min_val) / (max_val - min_val))] += 1
        for i in range(1, m):
            line[i] += line[i - 1]
        move = 0
        j = 0
        k = m - 1
        while move < n - 1:
            while j > line[k] - 1:
                j += 1
                k = int((m - 1) * (arr[j] - min_val) / (max_val - min_val))
            flash = arr[j]
            while j != line[k]:
                k = int((m - 1) * (flash - min_val) / (max_val - min_val))
                hold = arr[line[k] - 1]
                arr[line[k] - 1] = flash
                flash = hold
                line[k] -= 1
                move += 1
        return arr

    class Tournament:
        def __init__(self, data):
            self.data = data
            self.sorted_data = self.tournament_sort(data)

        @staticmethod
        def tournament_sort(data):
            if not data:
                return []

            while len(data) > 1:
                next_round = []
                for i in range(0, len(data), 2):
                    if i+1 < len(data):
                        next_round.append(max(data[i], data[i+1]))
                    else:
                        next_round.append(data[i])
                data = next_round

            return data

    class BinaryTree:
        class _Node:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        class _AVLNode:
            def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None
                self.height = 1

        class _RBNode:
            def __init__(self, data, color="red"):
                self.data = data
                self.color = color
                self.left = None
                self.right = None
                self.parent = None

        class _BPlusTreeNode:
            def __init__(self, is_leaf=False):
                self.is_leaf = is_leaf
                self.keys = []
                self.children = []

        class AVL:
            @classmethod
            def insert(cls, root, key):
                if not root:
                    return Sort.BinaryTree._AVLNode(key)
                if key < root.key:
                    root.left = cls.insert(root.left, key)
                else:
                    root.right = cls.insert(root.right, key)

                root.height = 1 + max(cls.Get.height(root.left), cls.Get.height(root.right))
                balance = cls.Get.balance(root)

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
            def delete(cls, root, key):
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

                root.height = 1 + max(cls.Get.height(root.left), cls.Get.height(root.right))
                balance = cls.Get.balance(root)

                if balance > 1:
                    if cls.Get.balance(root.left) >= 0:
                        return cls.__right_rotate(root)
                    root.left = cls.__left_rotate(root.left)
                    return cls.__right_rotate(root)
                if balance < -1:
                    if cls.Get.balance(root.right) <= 0:
                        return cls.__left_rotate(root)
                    root.right = cls.__right_rotate(root.right)
                    return cls.__left_rotate(root)

                return root

            @classmethod
            def __rotate(cls, z, direction):
                y = getattr(z, direction)
                setattr(z, direction, getattr(y, 'left' if direction == 'right' else 'right'))
                setattr(y, 'left' if direction == 'right' else 'right', z)
                z.height = 1 + max(cls.Get.height(z.left), cls.Get.height(z.right))
                y.height = 1 + max(cls.Get.height(y.left), cls.Get.height(y.right))
                return y

            @classmethod
            def __left_rotate(cls, z):
                return cls.__rotate(z, 'right')

            @classmethod
            def __right_rotate(cls, z):
                return cls.__rotate(z, 'left')

            @classmethod
            def pre_order(cls, root):
                result = []
                cls._pre_order_helper(root, result)
                return " ".join(result)

            @classmethod
            def _pre_order_helper(cls, root, result):
                if root:
                    result.append(str(root.key))
                    cls._pre_order_helper(root.left, result)
                    cls._pre_order_helper(root.right, result)

            @classmethod
            def __min_value_node(cls, root):
                while root.left:
                    root = root.left
                return root

            class Get:
                @staticmethod
                def height(root):
                    return root.height if root else 0

                @classmethod
                def balance(cls, root):
                    return cls.height(root.left) - cls.height(root.right) if root else 0

        class Complete:
            @classmethod
            def __init__(cls):
                cls.root = None

            @classmethod
            def insert(cls, value):
                if not cls.root:
                    cls.root = Sort.BinaryTree._Node(value)
                else:
                    cls.__insert_recursive(cls.root, value)

            @classmethod
            def __insert_recursive(cls, node, value):
                if value < node.value:
                    if not node.left:
                        node.left = Sort.BinaryTree._Node(value)
                    else:
                        cls.__insert_recursive(node.left, value)
                else:
                    if not node.right:
                        node.right = Sort.BinaryTree._Node(value)
                    else:
                        cls.__insert_recursive(node.right, value)

            @classmethod
            def delete(cls, value):
                cls.root = cls.__delete_recursive(cls.root, value)

            @classmethod
            def __delete_recursive(cls, node, value):
                if not node:
                    return node
                if value < node.value:
                    node.left = cls.__delete_recursive(node.left, value)
                elif value > node.value:
                    node.right = cls.__delete_recursive(node.right, value)
                else:
                    if not node.left:
                        return node.right
                    if not node.right:
                        return node.left
                    temp = cls.__min_value_node(node.right)
                    node.value = temp.value
                    node.right = cls.__delete_recursive(node.right, temp.value)
                return node

            @staticmethod
            def __min_value_node(node):
                while node.left:
                    node = node.left
                return node

            @classmethod
            def traverse(cls):
                result = []
                cls.__inorder_traversal_recursive(cls.root, result)
                return result

            @classmethod
            def __inorder_traversal_recursive(cls, node, result):
                if node:
                    cls.__inorder_traversal_recursive(node.left, result)
                    result.append(node.value)
                    cls.__inorder_traversal_recursive(node.right, result)

        class Degenerate:
            @classmethod
            def __init__(cls):
                cls.root = None

            @classmethod
            def insert(cls, key):
                if not cls.root:
                    cls.root = Sort.BinaryTree._Node(key)
                else:
                    current = cls.root
                    while current.right:
                        current = current.right
                    current.right = Sort.BinaryTree._Node(key)

            @classmethod
            def search(cls, key):
                current = cls.root
                while current:
                    if current.key == key:
                        return True
                    current = current.right
                return False

            @classmethod
            def delete(cls, key):
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
            def traverse(cls):
                result = []
                current = cls.root
                while current:
                    result.append(str(current.key))
                    current = current.right
                result.append("None")
                return " -> ".join(result)

        class Perfect:
            @classmethod
            def __init__(cls, height):
                cls.height = height
                cls.nodes = [None] * (2 ** height - 1)

            @classmethod
            def create(cls):
                cls.__create(0)

            @classmethod
            def __create(cls, index):
                if index < len(cls.nodes):
                    cls.__create(2 * index + 1)
                    # noinspection PyTypeChecker
                    cls.nodes[index] = Sort.BinaryTree._Node(index)
                    cls.__create(2 * index + 2)

            @classmethod
            def return_tree(cls):
                levels = []
                cls.__print_tree(0, 0, levels)
                return cls.__format_tree(levels)

            @staticmethod
            def __format_tree(levels):
                if not levels:
                    return ""
                tree_str = ""
                max_width = len(" ".join(str(node.value) if node else "None" for node in levels[-1]))
                for level in levels:
                    level_str = " ".join(str(node.value) if node else "None" for node in level)
                    tree_str += level_str.center(max_width) + "\n"
                return tree_str.replace("None", " ")

            @classmethod
            def return_list(cls):
                return [node.value if node else None for node in cls.nodes]

            @classmethod
            def __print_tree(cls, index, level, levels):
                if index < len(cls.nodes):
                    if len(levels) == level:
                        levels.append([])
                    levels[level].append(cls.nodes[index])
                    cls.__print_tree(2 * index + 1, level + 1, levels)
                    cls.__print_tree(2 * index + 2, level + 1, levels)

        class RedBlackTree:
            @classmethod
            def __init__(cls):
                cls.NIL = Sort.BinaryTree._RBNode(data=None, color="black")
                cls.root = cls.NIL

            @classmethod
            def insert(cls, key):
                new_node = Sort.BinaryTree._RBNode(key)
                new_node.left = cls.NIL
                new_node.right = cls.NIL
                parent = None
                current = cls.root

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
            def insert_fixup(cls, node):
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
            def rotate(cls, node, direction):
                opposite = 'left' if direction == 'right' else 'right'
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
            def left_rotate(cls, x):
                cls.rotate(x, 'right')

            @classmethod
            def right_rotate(cls, y):
                cls.rotate(y, 'left')

            @classmethod
            def __repr__(cls):
                def recurse(node):
                    if node == cls.NIL:
                        return []
                    return recurse(node.left) + [node.data] + recurse(node.right)

                return str(recurse(cls.root))

        class BPlusTree:
            @classmethod
            def __init__(cls, t=3):
                cls.root = Sort.BinaryTree._BPlusTreeNode(is_leaf=True)
                cls.t = t

            @classmethod
            def insert(cls, key):
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
            def insert_non_full(cls, node, key):
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
            def split_child(cls, node, i):
                t = cls.t
                y = node.children[i]
                z = Sort.BinaryTree._BPlusTreeNode(is_leaf=y.is_leaf)
                node.children.insert(i + 1, z)
                node.keys.insert(i, y.keys[t - 1])
                z.keys = y.keys[t:(2 * t) - 1]
                y.keys = y.keys[0:t - 1]
                if not y.is_leaf:
                    z.children = y.children[t:(2 * t)]
                    y.children = y.children[0:t]

            @classmethod
            def search(cls, key, node=None):
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
            def traverse(cls, node=None, level=0):
                if not node:
                    node = cls.root
                result = [f"Level {level}: " + " ".join(str(key) for key in node.keys)]
                if not node.is_leaf:
                    for child in node.children:
                        result.extend(cls.traverse(child, level + 1))
                return result

        class SegmentTree:
            @classmethod
            def __init__(cls, data):
                cls.n = len(data)
                cls.tree = [0] * (2 * cls.n)
                cls.__build(data)

            @classmethod
            def __build(cls, data):
                for i in range(cls.n):
                    cls.tree[cls.n + i] = data[i]
                for i in range(cls.n - 1, 0, -1):
                    cls.tree[i] = cls.tree[i * 2] + cls.tree[i * 2 + 1]

            @classmethod
            def update(cls, pos, value):
                pos += cls.n
                cls.tree[pos] = value
                while pos > 1:
                    pos //= 2
                    cls.tree[pos] = cls.tree[2 * pos] + cls.tree[2 * pos + 1]

            @classmethod
            def query(cls, left, right):
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
            def insert(self, root, key):
                if root is None:
                    return Sort.BinaryTree._Node(key)
                if key < root.value:
                    root.left = self.insert(root.left, key)
                else:
                    root.right = self.insert(root.right, key)
                return root

            def inorder_traversal(self, root, sorted_list):
                if root:
                    self.inorder_traversal(root.left, sorted_list)
                    sorted_list.append(root.value)
                    self.inorder_traversal(root.right, sorted_list)

            def tree_sort(self, arr):
                if not arr:
                    return arr
                root = Sort.BinaryTree._Node(arr[0])
                for value in arr[1:]:
                    self.insert(root, value)
                sorted_list = []
                self.inorder_traversal(root, sorted_list)
                return sorted_list
