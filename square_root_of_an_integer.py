"""Calculate the floored square root of a number.

Usage: square_root_of_an_integer.py
"""


def main():
    """Main function call to test the sqrt function."""
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    assert sqrt(16) == 4
    assert sqrt(1) == 1
    assert sqrt(27) == 5

    print("All test cases passed!")


def sqrt(number):
    """Calculate the floored square root of a number.

    Args:
        number: An int representing the number to get the floored square
            root of
    Returns:
        floored_sqrt: An int representing the floored square root of the given
            number
    """
    floored_sqrt = 0
    while floored_sqrt ** 2 <= number:
        floored_sqrt += 1

    floored_sqrt -= 1

    return floored_sqrt


if __name__ == "__main__":
    main()
