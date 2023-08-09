"""
Unit tests for fibonacci generator
"""


from fibonacci import fib_generator


def test_fibonacci_generator():
    """
    Unit test for fibonacci_generator
    """
    fib_gen = fib_generator()
    assert next(fib_gen) == 1
    assert next(fib_gen) == 1
    assert next(fib_gen) == 2
    assert next(fib_gen) == 3
    assert next(fib_gen) == 5
    assert next(fib_gen) == 8
    assert next(fib_gen) == 13
    assert next(fib_gen) == 21
