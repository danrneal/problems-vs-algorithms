# Square Root of an Integer

## Design Choices

I used the exponent operator to keep track of how large the number squared was and once it exceeded the target was able to decrement the number by one to get the floored square root.

## Time Complexity

Time complexity is O(sqrt(n)) since the while loop only has to execute until the square root of n is reached incrementing by one each loop.

## Space Complexity

Space complexity is O(1) since all that is stored is a single value in a variable.
