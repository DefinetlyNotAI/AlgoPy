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

