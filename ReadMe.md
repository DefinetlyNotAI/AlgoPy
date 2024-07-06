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

### Installation

You can install **AlgoPy** using pip:

```bash
pip install AlgoPy
```

Or, if you're developing locally and have cloned the repository:

```bash
pip install .
```

## Usage

Here's a brief overview of how to use some of the main features of **AlgoPy**.

### Logging

To log an informational message:

```python
from AlgoPy.logger import LoggerDB

logger = LoggerDB(filename="app.log")
logger.info("Application started successfully.")
```

### Sorting and Searching

To sort an array using the quicksort algorithm:

```python
from AlgoPy.sorting_and_searching import SortingAndSearching

algorithms = SortingAndSearching()
data = [64, 34, "s", 25, "a", 12, 10, 22, 11, 90]
sorted_data = algorithms.quicksort(data.copy())
print(sorted_data)
```

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

**MyLibrary** is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
