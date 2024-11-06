**Ternary Search**
**Definition:**
Ternary search is a divide-and-conquer search algorithm used to find a target element within a sorted collection (like an array or list). 
Unlike binary search, which divides the collection into two parts, ternary search splits it into three equal parts. 
This approach is efficient for large, sorted datasets, particularly when reducing the search space in larger chunks could offer benefits.

**Explanation:**
In ternary search, two mid-points (mid1 and mid2) are calculated to divide the collection into three segments. 
The algorithm then compares the target element with the values at these mid-points:

If the target matches either mid-point, the search is successful.
If the target is smaller than the value at mid1, the search continues in the left segment.
If the target is greater than the value at mid2, the search continues in the right segment.
If the target lies between mid1 and mid2, the search is limited to the middle segment.
This process repeats, reducing the search space by one-third with each iteration, until the target is found or the search space is empty.

**Time Complexity:**

Best Case: O(1) — The target is found at one of the mid-points on the first comparison.
Worst Case: O(log₃(n)) — In each iteration, the search space is reduced by a factor of three, resulting in logarithmic time complexity with base 3.
Average Case: O(log₃(n)) — On average, ternary search takes O(log₃(n)) time to locate an element.

**Space Complexity:**

Iterative Implementation: O(1) — Only a constant amount of extra space is needed.
Recursive Implementation: O(log₃(n)) — Due to the recursive call stack, with each level using additional space.

**When to Use Ternary Search:**
Ternary search is effective for large, sorted arrays, but binary search is often preferred because it is generally simpler and has similar time 
complexity (O(log₂(n))), making ternary search less common in practice.
