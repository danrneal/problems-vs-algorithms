# Square Root of an Integer

## Design Choices

I used a binary search algorithm to cut the search space for the floored square root in half with each iteration. The algorithm first guesses a number in the middle of the search space and checks if it is correct. If not it cuts the search space in half and recurse with the new search space.

## Time Complexity

Time complexity is O(log(n)) since we are cutting the search space in half with each recursion making the time complexity the same as binary search.

## Space Complexity

Space complexity is also O(log(n)) since with each comparison is putting another call to the function on the call stack.
