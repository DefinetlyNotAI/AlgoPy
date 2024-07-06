from datetime import datetime
import os


class LoggerDB:
    def __init__(self, filename="Server.log", max_size=100):
        """
        Initialize the Logger class.

        This method initializes the Logger class and allows setting the filename attribute through initialization parameters. It also checks if the file exists and creates it if it doesn't.

        Parameters:
            filename (str): The name of the log file. Defaults to 'Server.log'.
            max_size (int): The maximum size of the log file in bytes. Defaults to 100.

        Returns:
            None
        """
        # Use the provided filename or default to 'Server.log'
        self.filename = str(filename)
        self.size = int(max_size)

        # Check if the file exists and create it if it doesn't
        if not os.path.exists(self.filename):
            with open(self.filename, "w"):
                pass  # Empty file content is fine here since we append logs

    @staticmethod
    def timestamp():
        """
        Get the current date and time and format it as a string in the format 'YYYY-MM-DD HH:MM:SS'.

        Returns:
            str: The formatted timestamp.
        """
        # Get the current date and time
        now = datetime.now()

        # Format the timestamp as a string
        time = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"

        return time

    def remove(self):
        """
        Removes the log file if it exists and is larger than the maximum size.

        Returns:
            None
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                line_count = sum(1 for line in file)
            if line_count > self.size:
                os.remove(self.filename)

    def info(self, message):
        """
        Writes an informational message to the log file.

        Parameters:
            message (str): The informational message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"INFO: {message} at {self.timestamp()}\n")

    def warning(self, message):
        """
        Writes a warning message to the log file.

        Parameters:
            message (str): The warning message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"WARNING: {message} at {self.timestamp()}\n")

    def error(self, message):
        """
        Writes an error message to the log file.

        Parameters:
            message (str): The error message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"ERROR: {message} at {self.timestamp()}\n")

    def critical(self, message):
        """
        Writes an error message to the log file.

        Parameters:
            message (str): The error message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"CRITICAL: {message} at {self.timestamp()}\n")


class SortingAndSearching:
    def __init__(self):
        pass

    @staticmethod
    def selection_sort(arr):
        """Sorts the input list using the Selection Sort algorithm, handling mixed types."""
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if str(arr[j]) < str(arr[min_index]):
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

    @staticmethod
    def bubble_sort(arr):
        """Sorts the input list using the Bubble Sort algorithm, handling mixed types."""
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if str(arr[j]) > str(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def insertion_sort(arr):
        """Sorts the input list using the Insertion Sort algorithm, handling mixed types."""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and str(key) < str(arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def binary_search(arr, x):
        """Returns True if x is present in arr[], else False."""
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

    def quicksort(self, arr):
        """Implements the Quicksort algorithm, handling mixed types."""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if str(x) < str(pivot)]
        middle = [x for x in arr if str(x) == str(pivot)]
        right = [x for x in arr if str(x) > str(pivot)]
        return self.quicksort(left) + middle + self.quicksort(right)

    def merge_sort(self, arr):
        """Implements the Merge Sort algorithm, handling mixed types."""
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


'''
# Example usage
algorithm = SortingAndSearching()
arr = [64, 34, "s", 25, "a", 12, 10, 22, 11, 90]

# Selection Sort
algorithm.selection_sort(arr)
print("Sorted array after Selection Sort:", arr)

# Bubble Sort
algorithm.bubble_sort(arr)
print("Sorted array after Bubble Sort:", arr)

# Insertion Sort
algorithm.insertion_sort(arr)
print("Sorted array after Insertion Sort:", arr)

# Binary Search
value_to_find = "INPUT VALUE"
index = algorithm.binary_search(arr, value_to_find)
if index != -1:
    print(f"Element {value_to_find} is present at index {index} or position {index + 1}")
else:
    print(f"Element {value_to_find} is not present in array")

# Quicksort
sorted_arr = algorithm.quicksort(arr.copy())
print("Sorted array after Quicksort:", sorted_arr)

# Merge Sort
algorithm.merge_sort(arr)
print("Sorted array after Merge Sort:", arr)
'''

'''
Example usage:

logger = LoggerDB(filename="NAME.EXTENSION", max_size=SIZE)  # Change 'NAME.EXTENSION' to your desired filename
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
'''
