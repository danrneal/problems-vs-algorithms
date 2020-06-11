"""Find the min and max in an unsorted list.

Usage: unsorted_integer_array.py
"""

import random


def main():
    """Main function call to test the get_min_max function."""
    list_1 = list(range(10))
    random.shuffle(list_1)
    assert get_min_max(list_1) == (0, 9)

    list_2 = list(range(10, 100))
    random.shuffle(list_2)
    assert get_min_max(list_2) == (10, 99)

    list_3 = list(range(-10, 10))
    random.shuffle(list_3)
    assert get_min_max(list_3) == (-10, 9)

    print("All test cases passed!")


def get_min_max(unsorted_list):
    """Find the min and max in an unsorted list.

    Args:
        unsorted_list: A list of unsorted ints to find the min and max of

    Returns:
        minimum, maximum: Two ints representing the min and max in the
            given list
    """
    if len(unsorted_list) == 0:
        return None

    minimum = unsorted_list[0]
    maximum = unsorted_list[0]

    for item in unsorted_list:
        if item < minimum:
            minimum = item
        elif item > maximum:
            maximum = item

    return minimum, maximum


if __name__ == "__main__":
    main()
