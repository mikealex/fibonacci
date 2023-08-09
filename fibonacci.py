"""
FIBONACCI - demonstrates how to use a generator to calculate Fibonacci numbers
"""

import timeit


MAX_FIB = 10000000
NUM_ITERATIONS = 1000000


def fib_generator() -> int:
    """
    Generates Fibonacci numbers in sequence

    Yields:
        int: the next Fibonacci number in the sequence
    """
    fib1 = fib2 = 1
    yield fib1
    yield fib2
    while True:
        next_fib = fib1 + fib2
        if next_fib > MAX_FIB:
            break
        fib1 = fib2
        fib2 = next_fib
        yield next_fib


def generate_fibs():
    """
    Test function to iterate over all of the fibonacci numbers returned bh the fib_generator
    function
    """
    fib_gen = fib_generator()
    for _ in fib_gen:
        pass


if __name__ == "__main__":
    print(
        "timeit: ",
        timeit.timeit(
            "generate_fibs()", setup="pass", number=NUM_ITERATIONS, globals=globals()
        ),
    )
