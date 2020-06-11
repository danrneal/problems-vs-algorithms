"""Find the index of a given number in a sorted but rotated list.

Usage: search_in_a_rotated_sorted_array.py
"""


def main():
    """Main function call to test the rotated_array_search function."""
    list_1, num_1 = [6, 7, 8, 9, 10, 1, 2, 3, 4], 6
    assert rotated_array_search(list_1, num_1) == linear_search(list_1, num_1)

    list_2, num_2 = [6, 7, 8, 9, 10, 1, 2, 3, 4], 1
    assert rotated_array_search(list_2, num_2) == linear_search(list_2, num_2)

    list_3, num_3 = [6, 7, 8, 1, 2, 3, 4], 8
    assert rotated_array_search(list_3, num_3) == linear_search(list_3, num_3)

    list_4, num_4 = [6, 7, 8, 1, 2, 3, 4], 1
    assert rotated_array_search(list_4, num_4) == linear_search(list_4, num_4)

    list_5, num_5 = [6, 7, 8, 1, 2, 3, 4], 10
    assert rotated_array_search(list_5, num_5) == linear_search(list_5, num_5)

    print("All test cases passed!")


def rotated_array_search(input_list, number):
    """Find the index of a given number in a sorted but rotated list.

    Uses a modified binary search.

    Args:
        input_list: A list of ints representing the list to search in
        number: An int representing the value to search for

    Returns:
        index: An int representing the index of the number in the list, -1 if
            the number is not found
    """
    if len(input_list) == 0:
        return -1

    guess = len(input_list) // 2

    if (input_list[0] <= number < input_list[guess]) or (
        number > input_list[0] > input_list[guess]
    ):
        guess = rotated_array_search(input_list[:guess], number)
    elif input_list[guess] != number:
        added = rotated_array_search(input_list[guess + 1 :], number)
        if added == -1:
            return -1
        guess += added + 1

    return guess


def linear_search(input_list, number):
    """Perform a linear search for a number on a list.

    Args:
        input_list: A list of ints representing the list to search in
        number: An int representing the value to search for

    Returns:
        index: An int representing the index of the number in the list, -1 if
            the number is not found
    """
    for index, element in enumerate(input_list):
        if element == number:
            return index

    return -1


if __name__ == "__main__":
    main()
