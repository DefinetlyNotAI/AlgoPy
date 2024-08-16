"""
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
  - [Convert.dec_to_roman]
  - [Convert.roman_to_dec]
  - [Find.total_vowels]
  - [Find.every_vowel]
  - [Convert.bin_to_dec]
  - [Convert.bin_to_hex]
  - [Convert.hex_to_bin]
  - [Convert.hex_to_dec]

- **O(log n)**:
  - [Convert.dec_to_hex]
  - [Convert.dec_to_bin]

- **O(n log n)**:
  - [Find.largest]
  - [Find.smallest]
  - [Sort.using_quicksort]
  - [Sort.using_merge_sort]

- **O(n * m)**:
  - [Convert.dec_to_ascii]

- **O(n^2)**:
  - [Sort.using_selection]
  - [Sort.using_bubble]
  - [Sort.using_insertion]


### Space Complexity
- O(1):
  - [Find.value_index]
  - [Find.total_vowels]
  - [Find.every_vowel]
  - [Sort.using_selection]
  - [Sort.using_bubble]
  - [Sort.using_insertion]
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

- O(n):
  - [Find.largest]
  - [Find.smallest]
  - [Log.info]
  - [Log.warning]
  - [Log.error]
  - [Log.critical]
  - [Sort.using_merge_sort]
  - [Validate.email]

- O(log n):
  - [Sort.using_quicksort]
"""

# TODO replace errors with raise, remove colorlog except with Log class

# Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life
from datetime import datetime
import os
import colorlog


class LOG:
    def __init__(self, filename="Server.log", DEBUG=False, debug_color="cyan", info_color="green", warning_color="yellow", error_color="red", critical_color="red", colorlog_fmt_parameters="%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"):
        """
        Initializes a new instance of the LOG class.

        IMPORTANT: This class requires colorlog to be installed and also uses it in the INFO level,
        To use the debug level, set DEBUG to True.

        If you are using colorlog, DO NOT INITIALIZE IT MANUALLY, USE THE LOG CLASS PARAMETER'S INSTEAD.
        Sorry for any inconvenience that may arise.

        Args:
            filename (str, optional): The name of the log file. Defaults to "Server.log".
            DEBUG (bool, optional): Whether to use the debug level. Defaults to False (which uses the INFO level).
            debug_color (str, optional): The color of the debug level. Defaults to "cyan".
            info_color (str, optional): The color of the info level. Defaults to "green".
            warning_color (str, optional): The color of the warning level. Defaults to "yellow".
            error_color (str, optional): The color of the error level. Defaults to "red".
            critical_color (str, optional): The color of the critical level. Defaults to "red".
            colorlog_fmt_parameters (str, optional): The format of the log message. Defaults to "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s".

        Returns:
            None
        """
        # Configure colorlog for logging messages with colors
        logger = colorlog.getLogger()
        if DEBUG:
            logger.setLevel(colorlog.DEBUG)  # Set the log level to DEBUG to capture all relevant logs
        else:
            logger.setLevel(colorlog.INFO)  # Set the log level to INFO to capture all relevant logs
        handler = colorlog.StreamHandler()
        formatter = colorlog.ColoredFormatter(
            colorlog_fmt_parameters,
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": debug_color,
                "INFO": info_color,
                "WARNING": warning_color,
                "ERROR": error_color,
                "CRITICAL": critical_color,
            },
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.filename = str(filename)
        if not os.path.exists(self.filename):
            self.__only("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|")
            self.__only("|     Timestamp     |  LOG Level  |" + " " * 71 + "LOG Messages" + " " * 71 + "|")
        self.__only("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|")

    @staticmethod
    def __timestamp():
        """
        Returns the current timestamp as a string in the format 'YYYY-MM-DD HH:MM:SS'.

        Returns:
            str: The current timestamp.
        """
        now = datetime.now()
        time = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"
        return time

    def __only(self, message):
        with open(self.filename, "a") as f:
            f.write(f"{message}\n")

    @staticmethod
    def __pad_message(message):
        """
        Adds spaces to the end of a message until its length is exactly 153 characters.

        Parameters:
        - message (str): The input message string.

        Returns:
        - str: The padded message with a length of exactly 153 characters.
        """
        # Calculate the number of spaces needed
        num_spaces = 153 - len(message)

        if num_spaces > 0:
            # If the message is shorter than 153 characters, add spaces to the end
            padded_message = message + ' ' * num_spaces
        else:
            # If the message is already longer than 153 characters, truncate it to the first 153 characters
            padded_message = message[:150]
            padded_message += "..."

        padded_message += "|"
        return padded_message

    def info(self, message):
        """
        Logs an informational message to the log file.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        colorlog.info(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > INFO:     | {self.__pad_message(message)}\n")

    def warning(self, message):
        """
        Logs a warning message to the log file.

        Args:
            message (str): The warning message to be logged.

        Returns:
            None
        """
        colorlog.warning(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > WARNING:  | {self.__pad_message(message)}\n")

    def error(self, message):
        """
        Logs an error message to the log file.

        Args:
            message (str): The error message to be logged.

        Returns:
            None
        """
        colorlog.error(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > ERROR:    | {self.__pad_message(message)}\n")

    def critical(self, message):
        """
        Writes a critical message to the log file.

        Args:
            message (str): The critical message to be logged.

        Returns:
            None
        """
        colorlog.critical(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > CRITICAL: | {self.__pad_message(message)}\n")


class Find:
    def __init__(self, show_errors=True):
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
        self.error_level = show_errors

    def __sort(self, List):
        """
        Sorts a list of numbers, converting them to floats if needed. Returns the sorted list.
        """
        if List is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
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

    def __vowel_y(self, string=None, only_lowercase=False):
        """
        Determines the vowels in a given string, taking into account special cases for the letter 'y'.

        Parameters:
            string (str): The input string.
            only_lowercase (bool, optional): Whether to consider only lowercase vowels. Defaults to False.

        Returns:
            str: The vowels present in the string, taking into account special cases for 'y'.
        """
        if string is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
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
        if List is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
        largeList = self.__sort(List)
        if largeList is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
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
        if List is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
        smallList = self.__sort(List)
        if smallList is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
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
            if self.error_level:
                colorlog.error("No input given.")
            return False
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
            if self.error_level:
                colorlog.error("No input given.")
            return False
        result = ""
        vowels = self.__vowel_y(Word, True)
        for vowel in vowels:
            result += self.__count_character(Word, vowel) + "\n"
        return result.rstrip("\n")

    def value_index(self, array=None, value_to_find=None):
        """
        A function to find the index of a specific value in an array.

        Parameters:
            array (list): The array to search in.
            value_to_find (Any): The value to search for.

        Returns:
            int or bool: The index of the value in the array if found, False otherwise.
        """
        if array is None or value_to_find is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
        # Iterate over the list with enumerate to get both index and value
        for index, value in enumerate(array):
            if value == value_to_find:
                return index  # Return the index if the value matches
        return False  # Return False if the value was not found in the list


class Sort:
    def __init__(self, show_errors=True):
        self.error_level = show_errors

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

    def using_quick_sort(self, Array=None):
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
            if self.error_level:
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
        return self.using_quick_sort(left) + middle + self.using_quick_sort(right)

    def using_merge_sort(self, Array=None):
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
            if self.error_level:
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

    def using_selection_sort(self, Array=None):
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
            if self.error_level:
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

    def using_bubble_sort(self, Array=None):
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
            if self.error_level:
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

    def using_insertion_sort(self, Array=None):
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
            if self.error_level:
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
    def __init__(self, show_errors=True):
        """
        Initialize the Validate object with a list of common domains and domain variants.

        Parameters:
            show_errors (bool): Flag to enable or disable warnings. Default is True.
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
        self.error_level = show_errors

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
            if self.error_level:
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
            if self.error_level:
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
        self.memory_dict = {
            'Bit': 1,
            'Byte': 8,
            'KB': 8 * 1000,
            'MB': 8 * (1000 ** 2),
            'GB': 8 * (1000 ** 3),
            'TB': 8 * (1000 ** 4),
            'PB': 8 * (1000 ** 5),
            'KiB': 8 * 1024,
            'MiB': 8 * (1024 ** 2),
            'GiB': 8 * (1024 ** 3),
            'TiB': 8 * (1024 ** 4),
            'PiB': 8 * (1024 ** 5),
            'Kb': 1000,
            'Mb': 1000 ** 2,
            'Gb': 1000 ** 3,
            'Tb': 1000 ** 4,
            'Pb': 1000 ** 5,
            'Kib': 1024,
            'Mib': 1024 ** 2,
            'Gib': 1024 ** 3,
            'Tib': 1024 ** 4,
            'Pib': 1024 ** 5,
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
        self.error_level = show_errors

    def dec_to_roman(self, num=None):
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

    def roman_to_dec(self, roman=None):
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

    def dec_to_ascii(self, Number=None):
        """
        Generate ASCII art based on the input number and return the ASCII art as a string.

        Parameters:
            Number (str or int, optional): The number to be converted to ASCII art.

        Returns:
            str: The ASCII art representation of the input number.
        """
        if Number is None:
            if self.error_level:
                colorlog.error("No input given.")
            return False
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

    def __check_input_type(self, value, expected_type):
        """Checks if the input value is of the expected type."""
        if not isinstance(value, expected_type):
            if self.error_level:
                colorlog.error(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return False
        return True

    def bin_to_hex(self, Binary_Number=None):
        """
        Converts a binary number to hexadecimal.

        Args:
            Binary_Number (str) (int): The binary number as a string.

        Returns:
            str: The hexadecimal representation of the binary number, or False if an error occurred.
        """
        if Binary_Number is None:
            if self.error_level:
                colorlog.error("Conversion failed: No binary number provided")
            return False
        Binary_Number = str(Binary_Number)
        if not self.__check_input_type(Binary_Number, str):
            return False
        try:
            Hexadecimal_Number = hex(int(Binary_Number, 2))[2:]  # Remove the '0x' prefix
            return Hexadecimal_Number.upper()
        except ValueError as e:
            if self.error_level:
                colorlog.error(f"Conversion failed: {e}")
            return False

    def bin_to_dec(self, Binary_Number=None):
        """
        Converts a binary number to decimal.

        Args:
            Binary_Number (str) (int): The binary number as a string.

        Returns:
            int: The decimal representation of the binary number, or False if an error occurred.
        """
        if Binary_Number is None:
            if self.error_level:
                colorlog.error("Conversion failed: No binary number provided")
            return False
        Binary_Number = str(Binary_Number)
        if not self.__check_input_type(Binary_Number, str):
            return False
        try:
            return int(Binary_Number, 2)
        except ValueError as e:
            if self.error_level:
                colorlog.error(f"Conversion failed: {e}")
            return False

    def dec_to_hex(self, Decimal_Number=None):
        """
        Converts a decimal number to hexadecimal.

        Args:
            Decimal_Number (int) (str): The decimal number.

        Returns:
            str: The hexadecimal representation of the decimal number, or False if an error occurred.
        """
        Decimal_Number = int(Decimal_Number)
        if Decimal_Number is None:
            if self.error_level:
                colorlog.error("Conversion failed: No decimal number provided")
            return False
        if not self.__check_input_type(Decimal_Number, (int, str)):
            return False
        try:
            Hexadecimal_Number = hex(Decimal_Number)[2:]  # Remove the '0x' prefix
            return Hexadecimal_Number.upper()
        except ValueError as e:
            if self.error_level:
                colorlog.error(f"Conversion failed: {e}")
            return False

    def dec_to_bin(self, Decimal_Number=None):
        """
        Converts a decimal number to binary.

        Args:
            Decimal_Number (int) (str): The decimal number.

        Returns:
            str: The binary representation of the decimal number, or False if an error occurred.
        """
        Decimal_Number = int(Decimal_Number)
        if Decimal_Number is None:
            if self.error_level:
                colorlog.error("Conversion failed: No decimal number provided")
            return False
        if not self.__check_input_type(Decimal_Number, (int, str)):
            return False
        try:
            Binary_Number = bin(Decimal_Number)[2:]  # Remove the '0b' prefix
            return Binary_Number
        except ValueError as e:
            if self.error_level:
                colorlog.error(f"Conversion failed: {e}")
            return False

    def hex_to_bin(self, Hexadecimal_Number=None):
        """
        Converts a hexadecimal number to binary.

        Args:
            Hexadecimal_Number (str): The hexadecimal number as a string.

        Returns:
            str: The binary representation of the hexadecimal number, or False if an error occurred.
        """
        if Hexadecimal_Number is None:
            if self.error_level:
                colorlog.error("Conversion failed: No hexadecimal number provided")
            return False
        if not self.__check_input_type(Hexadecimal_Number, str):
            return False
        try:
            Binary_Number = bin(int(Hexadecimal_Number, 16))[2:]  # Remove the '0b' prefix
            return Binary_Number
        except ValueError as e:
            if self.error_level:
                colorlog.error(f"Conversion number system conversion failed: {e}")
            return False

    def hex_to_dec(self, Hexadecimal_Number=None):
        """
        Converts a hexadecimal number to decimal.

        Args:
            Hexadecimal_Number (str): The hexadecimal number as a string.

        Returns:
            int: The decimal representation of the hexadecimal number, or False if an error occurred.
        """
        if Hexadecimal_Number is None:
            if self.error_level:
                colorlog.error("Conversion failed: No hexadecimal number provided")
            return False
        if not self.__check_input_type(Hexadecimal_Number, str):
            return False
        try:
            return int(Hexadecimal_Number, 16)
        except ValueError as e:
            if self.error_level:
                colorlog.error(f"Conversion failed: {e}")
            return False

    def memory(self, number=None, input_unit=None, output_unit=None):
        """
        Converts a given number from one memory unit to another.

        Capital Letters are used for memory units.
        Memory units must use a small case letter for the letter `i` if using base 1024. (KibiByte)
        Memory units must use a small case letter for the letter `b` if using bits. (KiloBit / KibiBit)
        Memory units must use capital letters other than those 2 rules.
        Bit and Byte are the only exception and are written fully with only the first letter capitalised.
        Examples: KB, KiB, Kb and Kib
        Reaches until PiB

        Args:
            number (int): The number to be converted.
            input_unit (str): The unit of the given number. Must exist in `memory_dict`.
            output_unit (str): The desired unit for the converted number. Must exist in `memory_dict`.

        Raises:
            ValueError: If the input number is not an integer, or if either the input or output unit does not exist in `memory_dict`.

        Returns:
            str: The converted number with two decimal places and the output unit.

        """
        # Ensure the inputs are valid
        if number is None or input_unit is None or output_unit is None:
            if self.error_level:
                colorlog.error("Invalid input. Number, input_unit, and output_unit must all be provided.")
            return False
        if not isinstance(number, int) or input_unit not in self.memory_dict or output_unit not in self.memory_dict:
            if self.error_level:
                colorlog.error("Invalid input. Number must be an integer, and both units must exist in memory_dict.")
            return False

        # Step 1 & 2: Convert the number to bits
        input_factor = self.memory_dict[input_unit]
        number_in_bits = number * input_factor

        # Step 3 & 4: Convert back to the desired unit
        output_factor = self.memory_dict[output_unit]
        final_number = number_in_bits / output_factor

        # Step 5: Return the final converted value as a string
        return f"{final_number:.2f} {output_unit}"
