# Dutch National Flag Problem

## Design Choices

This algorithm keeps track of the of indices of where to place 0s and 2s. Once all the 0s are placed on the right side of the array and the all of the 2s are placed on the left side of the array, we can conclude that the 1s are in their correct positions as well.

## Time Complexity

Since this algorithm only traverses the input array once the time complexity is O(n).

## Space Complexity

This algorithm sorts the input list in place using no extra space and simply keeps track of indices in a few variable making its space complexity O(1).
