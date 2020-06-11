# Search in a Rotated Sorted Array

## Design Choices

This algorithm uses algorithm uses a recursive approach, breaking the list into shorter and shorter segments until the solution is found. Each call the function guesses the middle element and uses the first element in the array to determine if it is in the upper half or lower half of the array.

## Time Complexity

The time complexity is the same as binary search which is O(log(n)) since the array is cut in half with each recursion.

## Space Complexity

The space complexity of this algorithm is also O(log(n)) since each recursive call takes its own space on the call stack.
