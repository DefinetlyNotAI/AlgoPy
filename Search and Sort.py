class Sort:
    def __init__(self):
        pass

    @staticmethod
    def selection(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if str(arr[j]) < str(arr[min_index]):
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

    @staticmethod
    def bubble(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if str(arr[j]) > str(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def insertion(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and str(key) < str(arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if str(x) < str(pivot)]
        middle = [x for x in arr if str(x) == str(pivot)]
        right = [x for x in arr if str(x) > str(pivot)]
        return self.quicksort(left) + middle + self.quicksort(right)

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

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


class Search:
    @staticmethod
    def binary_search(arr, x):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif str(arr[mid]) < str(x):
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Refactor variable names, docstring
