# AlgoPy

## Overview

**AlgoPy** is a comprehensive collection of utilities designed to streamline various tasks in software development. It includes robust logging capabilities and efficient algorithms for sorting and searching data structures. Whether you're building applications or maintaining systems, **MyLibrary** offers tools to enhance productivity and reliability.

## Features

- Powerful logging system for tracking application events and errors.
- Efficient sorting and searching algorithms for quick data manipulation.
- Easy-to-use API for rapid integration into projects.

## Getting Started

To get started with **AlgoPy**, follow these steps:

### Prerequisites

Ensure you have Python installed on your system. **AlgoPy** supports Python versions 3.6 and above.


## Usage

Here's a brief overview of how to use some of the main features of **AlgoPy**.

### Table of Contents

- [Validate](#validate)
- [Convert](#convert)
- [Find](#find)
- [Log](#log)
- [Sort](#sort)

### Validate

The `Validate` class provides methods to check the validity of various inputs.

```python
from algopy import Validate

validate = Validate(warnings=True)
if validate.email("example@secret.com"):
    print("Valid")
else:
    print("Invalid")
```

### Convert

The `Convert` class offers functions to convert between numbers and Roman numerals, as well as ASCII representations.

```python
from algopy import Convert

convert = Convert(show_errors=False)

print(convert.to_roman(5000))
print(convert.to_number("MMMCMXCIX"))
print(convert.to_ascii(3000))  # Optional, leave empty for dynamic user input
```

### Find

The `Find` class includes methods for searching and analyzing lists.

```python
from algopy import Find

find = Find()

list_place = [17, 5.0, "hi", 65.03, 32.0, -4, -5.8]

print(find.largest(list_place))
print(find.smallest(list_place))
print(find.value_index(list_place, 32.0))
print(find.every_vowel("Hola"))
print(find.total_vowels("Hola"))
```

### Log

The `Log` class facilitates logging messages with different severity levels.

```python
from algopy import Log

log = Log(filename="NAME.EXTENSION", max_size="SIZE")  # Change 'NAME.EXTENSION' to your desired filename

log.info("This is an informational message.")
log.warning("This is a warning message.")
log.error("This is an error message.")
log.critical("This is a critical message.")
```

### Sort

The `Sort` class provides various sorting algorithms to sort arrays.

```python
from algopy import Sort

sort = Sort()
arr = [34, 5, 7, 23, 32, 4]

print("Original array:", arr)

sorted_arr_quick = sort.using_quick_sort(arr.copy())
print("Sorted using QuickSort:", sorted_arr_quick)

sorted_arr_merge = sort.using_merge_sort(arr.copy())
print("Sorted using MergeSort:", sorted_arr_merge)

sorted_arr_select = sort.using_selection_sort(arr.copy())
print("Sorted using SelectionSort:", sorted_arr_select)

sorted_arr_bubble = sort.using_bubble_sort(arr.copy())
print("Sorted using BubbleSort:", sorted_arr_bubble)

sorted_arr_insert = sort.using_insertion_sort(arr.copy())
print("Sorted using InsertionSort:", sorted_arr_insert)
```

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

**AlgoPy** is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
