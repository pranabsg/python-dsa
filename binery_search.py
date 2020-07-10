"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
from typing import List


def binary_search(input_array: List[int], value: int) -> int:
    left = 0
    right = len(input_array) - 1
    while left <= right:
        root = (left + right) // 2
        if input_array[root] == value:
            return root
        elif input_array[root] < value:
            left = root + 1
        else:
            right = root - 1
    return -1


def main():
    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 9
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))


if __name__ == '__main__':
    main()
