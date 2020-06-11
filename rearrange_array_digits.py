"""Take ints from a list and arrange them into two ints with a maximum sum.

Usage: rearrange_array_digits.py
"""


def main():
    """Main function call to test the rearrange_digits function."""
    assert sum(rearrange_digits([1, 2, 3, 4, 5])) == sum([542, 31])
    assert sum(rearrange_digits([4, 6, 2, 5, 9, 8])) == sum([964, 852])
    assert sum(rearrange_digits([1, 0, 0, 0, 0, 0])) == sum([100, 0])

    print("All test cases passed!")


def rearrange_digits(input_list):
    """Take ints from a list and arrange them into two ints with a maximum sum.

    Args:
        input_list: A list of ints representing the ints to arrange in the
            final output

    Returns:
        final: An array of two ints with the maximum sum from arranging the
            ints from the input
    """
    final = ["", ""]
    input_list = mergesort(input_list)
    idx = 0

    while len(input_list) > 0:
        final[idx] += str(input_list.pop())
        idx = (idx + 1) % 2

    final = [int(final[0]), int(final[1])]

    return final


def mergesort(items):
    """Sort an input list array.

    Args:
        items: A list of ints to be sorted from least to greatest

    Returns:
        merged: A list of sorted ints
    """
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


if __name__ == "__main__":
    main()
