"""Sort an array of 0s, 1s, and 2s in place.

Usage: dutch_national_flag_problem.py
"""


def main():
    """Main function call to test the rearrange_digits function."""
    list_1 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    assert sort_012(list_1) == sorted(list_1)

    list_2 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0]
    assert sort_012(list_2) == sorted(list_2)

    list_3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    assert sort_012(list_3) == sorted(list_3)

    print("All test cases passed!")


def sort_012(input_list):
    """Sort an array of 0s, 1s, and 2s in place.

    Args:
        input_list: A list of ints consisting of 0s, 1s, and 2s to be sorted

    Returns:
        input_list: The list of ints passed in, sorted.
    """
    idx = 0
    left = 0
    right = len(input_list) - 1

    while idx <= right:
        if input_list[idx] == 0:
            input_list[idx], input_list[left] = (
                input_list[left],
                input_list[idx],
            )
            left += 1
            idx += 1
        elif input_list[idx] == 2:
            input_list[idx], input_list[right] = (
                input_list[right],
                input_list[idx],
            )
            right -= 1
        else:
            idx += 1

    return input_list


if __name__ == "__main__":
    main()
