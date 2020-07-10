"""Implement quick sort in Python.
Input a list.
Output a sorted list.
https://visualgo.net/en/sorting
"""
from typing import List
from random import randint


def quick_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    # print('Pivot = {}'.format(pivot))
    for curr in array:
        if curr < pivot:
            smaller.append(curr)
        elif curr == pivot:
            equal.append(curr)
        else:
            larger.append(curr)
    return quick_sort(smaller) + equal + quick_sort(larger)


def main():
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(quick_sort(test))
    # print(test)


if __name__ == '__main__':
    main()
