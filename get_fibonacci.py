"""Implement a function recursively to get the desired
Fibonacci sequence value.
"""


def get_fib(position: int) -> int:
    if position == 0 or position == 1:
        return position

    return get_fib(position - 1) + get_fib(position - 2)


def main():
    # Test cases
    print(get_fib(2))
    print(get_fib(11))
    print(get_fib(0))


if __name__ == '__main__':
    main()
