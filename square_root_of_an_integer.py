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


def sqrt(number, smallest=0, largest=None):
    """Calculate the floored square root of a number.

    Args:
        number: An int representing the number to get the floored square
            root of
        smallest: An int representing the smallest number in the search space,
            defaults to 0
        largest: An int representing the largest number in the search space,
            defaults to the value passed in as number

    Returns:
        floored_sqrt: An int representing the floored square root of the given
            number
    """
    if largest is None:
        largest = number

    guess = (smallest + largest) // 2

    if guess ** 2 <= number < (guess + 1) ** 2:
        floored_sqrt = guess
    elif guess ** 2 < number:
        floored_sqrt = sqrt(number, guess + 1, largest)
    elif guess ** 2 > number:
        floored_sqrt = sqrt(number, smallest, guess)

    return floored_sqrt


if __name__ == "__main__":
    main()
