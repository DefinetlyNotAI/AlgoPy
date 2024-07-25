"""
Convert()
    Converts integers to Roman numerals and vice versa.
    Please note that this is not an exhaustive list of all possible Roman numerals
    that can be represented and is a mix of preset and algorithmic calculations.
    If an error occurs during the conversion process, an error message will be displayed if set to True,
    as well as the class returning False.

Log()
    Manages logging operations for applications, supporting various severity levels (info, warning, error, critical).
    Automatically rotates the log file based on size, ensuring that no single log file exceeds a specified maximum size.
    Maintains a default filename ('Server.log') unless otherwise specified during instantiation.
    Utilizes static methods for timestamp generation, promoting reusability across different instances.
    Ensures thread safety by managing file access through context managers, preventing concurrent modifications.
    Efficiently appends log messages to the file, incorporating timestamps for precise logging.
    Removes the existing log file if it exceeds the maximum size, automatically starting fresh without manual intervention.

Find()
    Handles both integers and floats seamlessly, converting between types as needed.
    Gracefully ignores non-numeric elements without crashing, enhancing reliability.
    Interactive input method allows for easy testing and experimentation.
    Sorts lists efficiently and finds largest/smallest elements with minimal overhead.
    Finds the number of vowels in a word.
    Either totally, or by vowel.
    Includes special words that have y as either an active vowel or as a passive vowel.

Sort()
    Provides a unified interface for sorting arrays/lists of comparable items using various sorting algorithms.
    Supports sorting of mixed data types by comparing their string representations, allowing for flexibility in input.
    Incorporates best practices for algorithm implementation, including efficient use of static methods for reusable logic.
    Quicksort and merge sort are implemented recursively, demonstrating advanced recursion techniques and divide-and-conquer strategies.
    Selection sort, bubble sort, and insertion sort are included for educational purposes, showcasing simpler sorting mechanisms.
    Each sorting method is designed to handle arrays/lists of any size, with optimizations for performance and memory usage.
    If an error occurs it returns False.

Validate()
    Email Validator, Super basic and static, just checks for @ and . and some usual domains.
    Returns False if email is invalid
    Returns True if email is valid
    Checks include:
            1. Ensure there is exactly one '@' symbol in the email address.
            2. Convert the email address to lowercase and check if it ends with a common domain or domain variant.
            3. Check the length constraints of the name and domain_tld.
            4. Split the email address into name and domain_tld.
            5. Split the domain_tld into domain and tld.
            6. Check if the domain is a common domain or a variant of a common domain.
            7. Special handling for .co domain.
            8. Check if the tld is a recognized domain variant.

Complexities
    TIME COMPLEXITY = O(n) [Log.info] [Log.warning] [Log.error] [Log.critical] [Find.value_index] [Validate.email]
    TIME COMPLEXITY = O(n / log n ) [Find.largest] [Find.smallest]
    TIME COMPLEXITY = O(n * log n ) [Convert.to_roman] [Convert.to_number] [Sort.using_quicksort] [Sort.using_merge_sort]
    TIME COMPLEXITY = O(n * m) [Convert.to_ascii] [Find.total_vowels] [Find.every_vowel]
    TIME COMPLEXITY = O(n ^ 2) [Sort.using_selection] [Sort.using_bubble] [Sort.using_insertion]

    SPACE COMPLEXITY = O(1) [Find.value_index] [Find.total_vowels] [Find.every_vowel] [Sort.using_selection] [Sort.using_bubble] [Sort.using_insertion] [Convert.to_ascii] [Convert.to_roman] [Convert.to_number]
    SPACE COMPLEXITY = O(n) [Find.largest] [Find.smallest] [Log.info] [Log.warning] [Log.error] [Log.critical] [Sort.using_merge_sort] [Validate.email]
    SPACE COMPLEXITY = O(log n) [Sort.using_quicksort]
"""

# Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life
from datetime import datetime
import os
import colorlog

# Configure colorlog for logging messages with colors
logger = colorlog.getLogger()
logger.setLevel(colorlog.INFO)  # Set the log level to INFO to capture all relevant logs

handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
)
handler.setFormatter(formatter)
logger.addHandler(handler)


class Log:
    def __init__(self, filename="Server.log", max_size=None):
        """
        Initializes a new instance of the Log class.

        Args:
            filename (str, optional): The name of the log file. Defaults to "Server.log".
            max_size (int, optional): The maximum size of the log file in bytes. Defaults to infinity.

        Initializes the `filename` and `size` attributes of the Log instance.
        If the log file does not exist, it creates an empty file with the specified name.

        """
        # Use the provided filename or default to 'Server.log'
        self.filename = str(filename)
        self.size = int(max_size)

        # Check if the file exists and create it if it doesn't
        if not os.path.exists(self.filename):
            with open(self.filename, "w"):
                pass  # Empty file content is fine here since we append logs

    @staticmethod
    def __timestamp():
        """
        Retrieves the current date and time and formats it into a string timestamp.

        Returns:
            str: A string representing the formatted timestamp.
        """
        # Get the current date and time
        now = datetime.now()

        # Format the timestamp as a string
        time = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"

        return time

    def __remove(self):
        """
        Remove the log file if it exists and the number of lines in the file exceeds the specified size.

        This function checks if the log file specified by the `filename` attribute exists. If it does, it opens the file in read mode and counts the number of lines in the file. If the number of lines is greater than the specified `size`, the file is removed.

        Returns:
            None
        """
        if os.path.exists(self.filename) and self.size is not None:
            with open(self.filename, "r") as file:
                line_count = sum(1 for _ in file)
            if line_count > self.size:
                os.remove(self.filename)

    def info(self, message):
        """
        Writes an information log message to the log file.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"INFO: {message} at {self.__timestamp()}\n")

    def warning(self, message):
        """
        Writes a warning log message to the log file.

        Args:
            message (str): The warning message to be logged.

        Returns:
            None
        """
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"WARNING: {message} at {self.__timestamp()}\n")

    def error(self, message):
        """
        Writes an error log message to the log file.

        Args:
            message (str): The error message to be logged.

        Returns:
            None
        """
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"ERROR: {message} at {self.__timestamp()}\n")

    def critical(self, message):
        """
        Writes a critical log message to the log file.

        Args:
            message (str): The critical message to be logged.

        Returns:
            None
        """
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"CRITICAL: {message} at {self.__timestamp()}\n")


class Find:
    def __init__(self):
        """
        Words that have y as either an active vowel or as a passive vowel
        """
        # Words that have y as either an active vowel or as a passive vowel
        self.special_y_words = [
            "Cry",
            "Dry",
            "Gym",
            "Hymn",
            "Lynx",
            "Myth",
            "Pry",
            "Rhythm",
            "Shy",
            "Spy",
            "Spry",
            "Sync",
            "Try",
            "Why",
            "City",
            "Party",
            "Fly",
            "Shy",
            "Wary",
            "Worthwhile",
            "Type",
            "Typical",
            "Thyme",
            "Cyst",
            "Symbol",
            "System",
            "Lady",
            "Pretty",
            "Very",
            "Deny",
            "Daddy",
            "Quickly",
        ]

    @staticmethod
    def __sort(List):
        """
        Sorts a list of numbers, converting them to floats if needed. Returns the sorted list.
        """
        if List is None:
            colorlog.error("No input given.")
            exit(1)
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

    def __vowel_y(self, string, only_lowercase=False):
        """
        Determines the vowels in a given string, taking into account special cases for the letter 'y'.

        Parameters:
            string (str): The input string.
            only_lowercase (bool, optional): Whether to consider only lowercase vowels. Defaults to False.

        Returns:
            str: The vowels present in the string, taking into account special cases for 'y'.
        """
        if self.__value_index(self.special_y_words, string):
            if only_lowercase:
                vowels = "aeiouy"
            else:
                vowels = "aeiouyAEIOUY"
        else:
            if only_lowercase:
                vowels = "aeiou"
            else:
                vowels = "aeiouAEIOU"
        return vowels

    @staticmethod
    def __count_character(Word, Vowel):
        """
        Counts the occurrences of a given character in a word.

        Parameters:
            Word (str): The word to search for the character.
            Vowel (str): The character to count.

        Returns:
            str: A string containing the character and its count.
        """
        # Counter
        count = 0

        # For loop to find length of word
        for i in range(len(Word)):
            if Word[i] == Vowel:
                count += 1

        return f"{Vowel} {count}"

    @staticmethod
    def __value_index(array, Word):
        """
        Check if a given value exists in an array.

        Parameters:
            array (list): The array to search in.
            Word (Any): The value to search for.

        Returns:
            bool: True if the value is found in the array, False otherwise.
        """
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == Word:
                return True  # Return True if the value matches
        return False  # Return False if the value was not found in the list

    def largest(self, List=None):
        """
        Sorts a list of integers and returns the largest element from the list.

        Parameters:
            List (list): List of integers to find the largest element from.

        Returns:
            int or None: The largest element from the list if it contains only integers, None otherwise.
        """
        largeList = self.__sort(List)

        if largeList is None:
            colorlog.error("No input given.")
            exit(1)

        return largeList[-1] if largeList else None

    def smallest(self, List=None):
        """
        Find the smallest element in a list of integers.

        Parameters:
            List (list, optional): The list of integers to find the smallest element from. Defaults to None.

        Returns:
            int or None: The smallest element from the list if it contains only integers, None otherwise.

        Raises:
            ValueError: If the list contains non-integer elements.
        """
        smallList = self.__sort(List)

        if smallList is None:
            colorlog.error("No input given.")
            exit(1)

        return smallList[0] if smallList else None

    def total_vowels(self, Word=None):
        """
        Find the total number of vowels in a given word.

        Parameters:
            Word (str, optional): The input word to count vowels from. Defaults to None.

        Returns:
            int: The total count of vowels in the input word.
        """
        if Word is None:
            colorlog.error("No input given.")
            exit(1)
        vowels = self.__vowel_y(Word)
        vowel_count = sum(1 for char in Word if char in vowels)
        return vowel_count

    def every_vowel(self, Word=None):
        """
        Find the total number of vowels in a given word.

        Parameters:
            Word (str, optional): The input word to count vowels from. Defaults to None.

        Returns:
            int: The total count of vowels in the input word.
        """
        if Word is None:
            colorlog.error("No input given.")
            exit(1)
        result = ""
        vowels = self.__vowel_y(Word, True)
        for vowel in vowels:
            result += self.__count_character(Word, vowel) + "\n"
        return result.rstrip("\n")

    @staticmethod
    def value_index(array=None, value_to_find=None):
        """
        A function to find the index of a specific value in an array.

        Parameters:
            array (list): The array to search in.
            value_to_find (Any): The value to search for.

        Returns:
            int or bool: The index of the value in the array if found, False otherwise.
        """
        if array is None or value_to_find is None:
            colorlog.error("No input given.")
            return False
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == value_to_find:
                return index  # Return the index if the value matches
        return False  # Return False if the value was not found in the list


class Sort:
    @staticmethod
    def __integer(Array=None):
        """
        Checks if all elements in the input Array are integers.

        Parameters:
            Array (list): The input list to check for integer elements.

        Returns:
            bool: True if all elements are integers, False otherwise.
        """

        return all(isinstance(item, int) for item in Array)

    @staticmethod
    def using_quick_sort(Array=None):
        """
        Sorts the given array using the quicksort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.
        """
        if Array is None:
            colorlog.error("No input given.")
            return False
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
    def using_merge_sort(Array=None):
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
        if Array is None:
            colorlog.error("No input given.")
            return False
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
    def using_selection_sort(Array=None):
        """
        Sorts the given array using the selection sort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.
        """
        if Array is None:
            colorlog.error("No input given.")
            return False
        if not Sort.__integer(Array):
            return False
        for i in range(len(Array)):
            min_index = i
            for j in range(i + 1, len(Array)):
                if Array[min_index] > Array[j]:
                    min_index = j
            Array[i], Array[min_index] = Array[min_index], Array[i]
        return Array

    @staticmethod
    def using_bubble_sort(Array=None):
        """
        Sorts the given array using the bubble sort algorithm.

        Parameters:
            Array (list): The array to be sorted.

        Returns:
            list: The sorted array.

        Raises:
            ValueError: If the input array contains non-integer elements.
        """
        if Array is None:
            colorlog.error("No input given.")
            return False
        if not Sort.__integer(Array):
            return False
        n = len(Array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if Array[j] > Array[j + 1]:
                    Array[j], Array[j + 1] = Array[j + 1], Array[j]
        return Array

    @staticmethod
    def using_insertion_sort(Array=None):
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
        if Array is None:
            colorlog.error("No input given.")
            return False
        if not Sort.__integer(Array):
            return False
        for i in range(1, len(Array)):
            key = Array[i]
            j = i - 1
            while j >= 0 and key < Array[j]:
                Array[j + 1] = Array[j]
                j -= 1
            Array[j + 1] = key
        return Array


class Validate:
    def __init__(self, warnings=True):
        """
        Initialize the Validate object with a list of common domains and domain variants.

        Parameters:
            warnings (bool): Flag to enable or disable warnings. Default is True.
        """
        self.common_domains = [
            "google.com",
            "gmail.com",
            "outlook.com",
            "yahoo.com",
        ]
        self.domain_variants = [
            ".com",
            ".net",
            ".org",
            ".io",
            ".me",
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "an",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "br",
            "bs",
            "bt",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xk",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
            "uk",
        ]
        self.warnings = warnings

    def email(self, email=None):
        """
        Validate an email address.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.

        This function checks if an email address is valid by performing the following steps:
        1. Ensure there is exactly one '@' symbol in the email address.
        2. Convert the email address to lowercase and check if it ends with a common domain or domain variant.
        3. Check the length constraints of the name and domain_tld.
        4. Split the email address into name and domain_tld.
        5. Split the domain_tld into domain and tld.
        6. Check if the domain is a common domain or a variant of a common domain.
        7. Special handling for .co domain.
        8. Check if the tld is a recognized domain variant.

        Note:
            The function assumes that the common_domains and domain_variants lists are defined in the Validate class.
        """
        if email is None:
            colorlog.error("No input given.")
            return False
        # Ensure there's exactly one '@'
        if email.count("@") != 1:
            return False
        # Convert to lowercase and check for @ and .
        if not email.lower().endswith(
                (
                        ".com",
                        ".net",
                        ".org",
                        ".io",
                        ".me",
                        "ad",
                        "ae",
                        "af",
                        "ag",
                        "ai",
                        "al",
                        "am",
                        "an",
                        "ao",
                        "aq",
                        "ar",
                        "as",
                        "at",
                        "au",
                        "aw",
                        "ax",
                        "az",
                        "ba",
                        "bb",
                        "bd",
                        "be",
                        "bf",
                        "bg",
                        "bh",
                        "bi",
                        "bj",
                        "bm",
                        "bn",
                        "bo",
                        "br",
                        "bs",
                        "bt",
                        "bw",
                        "by",
                        "bz",
                        "ca",
                        "cd",
                        "cf",
                        "cg",
                        "ch",
                        "ci",
                        "ck",
                        "cl",
                        "cm",
                        "cn",
                        "co",
                        "cr",
                        "cu",
                        "cv",
                        "cw",
                        "cx",
                        "cy",
                        "cz",
                        "de",
                        "dj",
                        "dk",
                        "dm",
                        "do",
                        "dz",
                        "ec",
                        "ee",
                        "eg",
                        "eh",
                        "er",
                        "es",
                        "et",
                        "fi",
                        "fj",
                        "fk",
                        "fm",
                        "fo",
                        "fr",
                        "ga",
                        "gb",
                        "gd",
                        "ge",
                        "gf",
                        "gg",
                        "gh",
                        "gi",
                        "gl",
                        "gm",
                        "gn",
                        "gp",
                        "gr",
                        "gt",
                        "gu",
                        "gw",
                        "gy",
                        "hk",
                        "hm",
                        "hn",
                        "hr",
                        "ht",
                        "hu",
                        "id",
                        "ie",
                        "il",
                        "im",
                        "in",
                        "io",
                        "iq",
                        "ir",
                        "is",
                        "it",
                        "je",
                        "jm",
                        "jo",
                        "jp",
                        "ke",
                        "kg",
                        "kh",
                        "ki",
                        "km",
                        "kn",
                        "kp",
                        "kr",
                        "kw",
                        "ky",
                        "kz",
                        "la",
                        "lb",
                        "lc",
                        "li",
                        "lk",
                        "lr",
                        "ls",
                        "lt",
                        "lu",
                        "lv",
                        "ly",
                        "ma",
                        "mc",
                        "md",
                        "me",
                        "mg",
                        "mh",
                        "mk",
                        "ml",
                        "mm",
                        "mn",
                        "mo",
                        "mp",
                        "mq",
                        "mr",
                        "ms",
                        "mt",
                        "mu",
                        "mv",
                        "mw",
                        "mx",
                        "my",
                        "mz",
                        "na",
                        "nc",
                        "ne",
                        "nf",
                        "ng",
                        "ni",
                        "nl",
                        "no",
                        "np",
                        "nr",
                        "nu",
                        "nz",
                        "om",
                        "pa",
                        "pe",
                        "pf",
                        "pg",
                        "ph",
                        "pk",
                        "pl",
                        "pm",
                        "pn",
                        "pr",
                        "ps",
                        "pt",
                        "pw",
                        "py",
                        "qa",
                        "re",
                        "ro",
                        "rs",
                        "ru",
                        "rw",
                        "sa",
                        "sb",
                        "sc",
                        "sd",
                        "se",
                        "sg",
                        "sh",
                        "si",
                        "sj",
                        "sk",
                        "sl",
                        "sm",
                        "sn",
                        "so",
                        "sr",
                        "ss",
                        "st",
                        "sv",
                        "sx",
                        "sy",
                        "sz",
                        "tc",
                        "td",
                        "tf",
                        "tg",
                        "th",
                        "tj",
                        "tk",
                        "tl",
                        "tm",
                        "tn",
                        "to",
                        "tr",
                        "tt",
                        "tv",
                        "tw",
                        "tz",
                        "ua",
                        "ug",
                        "um",
                        "us",
                        "uy",
                        "uz",
                        "va",
                        "vc",
                        "ve",
                        "vg",
                        "vi",
                        "vn",
                        "vu",
                        "wf",
                        "ws",
                        "xk",
                        "ye",
                        "yt",
                        "za",
                        "zm",
                        "zw",
                        "uk",
                )
        ):
            return False

        name, domain_tld = email.split("@")

        # Check for length constraints
        if len(name) > 64 or len(domain_tld) > 255:
            return False

        # Splitting domain and TLD
        domain, tld = domain_tld.split(".")

        # Checking for common domains and variants
        if domain in self.common_domains or f"{domain}.{tld}" in self.common_domains:
            return True

        # Special handling for .co
        if tld == "co":
            if len(domain) > 64:
                return False
            return True

        # Unique domain check with warning for unrecognized domains
        if tld not in self.domain_variants or domain not in self.common_domains.remove(".com"):
            if self.warnings:
                colorlog.warning(f"Unrecognized domain '{domain}.{tld}'.")
            return True

        return False


class Convert:
    def __init__(self, show_errors=True):
        """
        Initializes the Convert class with default show_errors set to True.

        Parameters:
            show_errors (bool): Flag to indicate whether to show errors. Default is True.

        Returns:
            None
        """

        self.mapping = {
            10000: "/X/",
            9000: "M/X/",
            8000: "/VIII/",
            5000: "/V/",
            4000: "M/V/",
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        self.roman_to_numerical = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "/X/": 10000,
            "M/X/": 9000,
            "/VIII/": 8000,
            "/V/": 5000,
            "M/V/": 4000,
        }

        Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]

        One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]

        Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]

        Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]

        Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]

        Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]

        Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]

        Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]

        Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]

        Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

        self.digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
        self.error_level = show_errors  # TODO, add this to all methods

    def to_roman(self, num=None):
        """
        Converts an integer to a Roman numeral representation.

        Args:
            num (int): The integer to be converted.

        Returns:
            str: The Roman numeral representation of the input integer.

        Raises:
            KeyError: If the input integer is invalid.
            Exception: If an error occurs during the conversion process.

        Notes:
            - The input integer must be greater than or equal to 1.
            - If the input integer is greater than 10,000, a warning is raised.
            - If an error occurs during the conversion process, an error message is displayed if `show_errors` is True.
        """
        if num is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
        try:
            num = int(num)
            if num <= 1:
                if self.error_level:
                    colorlog.error("Input must be greater or equal to 1.")
                return False
            if num > 10000 and self.error_level:
                colorlog.warning(
                    "Input is too large. This may result in inaccurate results."
                )

            result = ""
            for numerical, roman in sorted(self.mapping.items(), reverse=True):
                while num >= numerical:
                    result += roman
                    num -= numerical
            return result
        except KeyError as ke:
            if self.error_level:
                colorlog.error("Invalid numeral: " + str(ke))
            return False
        except Exception as e:
            if self.error_level:
                colorlog.error(str(e))
            return False

    def to_number(self, roman=None):
        """
        Converts a Roman numeral to its corresponding decimal number.

        Args:
            roman (str): The Roman numeral to be converted.

        Returns:
            int: The decimal number corresponding to the input Roman numeral.

        Raises:
            KeyError: If the input Roman numeral is invalid.
            Exception: If an error occurs during the conversion process.

        Notes:
            - The input Roman numeral must be in uppercase.
            - If the input Roman numeral is invalid, an error message is displayed if `show_errors` is True.

        """
        if not isinstance(roman, str):
            if self.error_level:
                colorlog.error("Input must be a string.")
            return False
        elif not roman.isupper():
            if self.error_level:
                colorlog.error("Input must be uppercase.")
            return False
        elif roman is None:
            if self.error_level:
                colorlog.error("Input cannot be None.")
            return False
        try:
            i = 0
            num = 0
            roman = roman.upper()
            while i < len(roman):
                if i + 1 < len(roman) and roman[i: i + 2] in self.roman_to_numerical:
                    num += self.roman_to_numerical[roman[i: i + 2]]
                    i += 2
                else:
                    num += self.roman_to_numerical[roman[i]]
                    i += 1
            return num
        except KeyError as ke:
            if self.error_level:
                colorlog.error(f"Invalid Roman numeral: {ke}")
            return False
        except Exception as e:
            if self.error_level:
                colorlog.error(str(e))
            return False

    def to_ascii(self, Number=None):
        """
        Generate ASCII art based on the input number and return the ASCII art as a string.

        Parameters:
            Number (str or int, optional): The number to be converted to ASCII art.

        Returns:
            str: The ASCII art representation of the input number.
        """
        if Number is None:
            colorlog.error("No input given.")
            exit(1)
        elif not Number.isdigit():
            try:
                Number = str(Number)
            except Exception:
                if self.error_level:
                    colorlog.error("Invalid input. Please enter a number.")
                return False

        # Initialize an empty list to store each line of the ASCII art
        ascii_art_lines = []

        for i in range(7):  # Loop through each row
            line = ""
            for j in range(
                    len(Number)
            ):  # Loop through each character (digit) in the number
                current_num = int(Number[j])
                digit = self.digits[current_num]
                line += digit[i] + "  "  # Append the current digit's row to the line
            ascii_art_lines.append(line)  # Add the completed line to the list

        # Join all lines with newline characters to form the final ASCII art string
        ascii_art = "\n".join(ascii_art_lines)

        return ascii_art
