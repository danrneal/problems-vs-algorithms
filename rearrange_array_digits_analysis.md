# Rearrange Array Digits

## Design Choices

This algorithm first sorts the input list so that we can then place the largest digits in the left-most position in each final integers and the smallest digit in the right-most position in each final integers.

## Time Complexity

This algorithm takes O(n\*log(n)) time since sorting will be the dominant operation in the algorithm (implemented as mergesort). The while loop happens in O(n) time looping through each element in the input list once. This is dominated by the complexity of mergesort which takes O(n\*log(n)) time.

## Space Complexity

The space complexity is O(n) since mergesort does not sort in place and is the dominant factor in the space complexity.
