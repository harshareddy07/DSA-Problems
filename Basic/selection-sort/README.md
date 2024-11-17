**Selection Sort**
**Definition:**
Selection sort is a simple comparison-based sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion of the array and places it in its correct position in the sorted portion.

**Explanation:**
Selection sort works by dividing the array into two parts: a sorted portion and an unsorted portion. The algorithm proceeds as follows:

Start with the first element as the sorted portion and the rest as unsorted.
Find the smallest element in the unsorted portion.
Swap the smallest element with the first element of the unsorted portion, effectively moving it into the sorted portion.
Repeat the process for the remaining unsorted elements until the entire array is sorted.
While selection sort is intuitive and easy to implement, it is inefficient for large datasets due to its nested loop structure, which leads to a high number of comparisons.

**Time Complexity:**
Best Case: O(n²) — Selection sort always performs the same number of comparisons, regardless of the initial order.
Worst Case: O(n²) — The algorithm always performs O(n²) comparisons, even for the reverse-sorted array.
​ .
**Space Complexity:**

O(1) — Selection sort is an in-place algorithm, requiring only a constant amount of extra space.

**For small datasets where simplicity is more important than efficiency.
When memory usage is critical, as it uses minimal extra space.
Rarely used in practice for large datasets, as other algorithms like quicksort or mergesort are significantly faster.**





