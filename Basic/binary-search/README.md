**Binary Search**

**Definition:**
Binary search is an efficient algorithm used to find the position of a target element within a sorted collection (like an array or list). 
It operates by repeatedly dividing the search interval in half, making it much faster than linear search for large, sorted datasets.

**Explanation:**
In binary search, the algorithm starts by comparing the target element with the middle element of the sorted collection:

If the middle element matches the target, the search is complete.
If the target is less than the middle element, the search continues in the left half of the collection.
If the target is greater than the middle element, the search continues in the right half.
This halving process repeats until the target element is found or the search interval is empty, meaning the target is not in the collection. Binary search is much faster than linear search, especially for large collections, due to its divide-and-conquer approach.

**Time Complexity:**

Best Case: O(1) — The target element is at the middle of the collection on the first comparison.
Worst Case: O(log n) — The algorithm reduces the search interval by half on each step, leading to a logarithmic time complexity.
Average Case: O(log n) — On average, binary search takes O(log n) time to locate an element.

**Space Complexity:**

Iterative Implementation: O(1) — Only a constant amount of extra space is needed.
Recursive Implementation: O(log n) — Due to the recursive call stack, each level of recursion uses extra space.
