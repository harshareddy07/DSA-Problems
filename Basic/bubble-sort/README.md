**Bubble Sort**
**Definition:**
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is completely sorted..

**Explanation:**
Bubble sort derives its name from the way larger elements "bubble up" to the top of the list with each pass:
The algorithm starts at the beginning of the list and compares adjacent elements.
If the current element is greater than the next one, they are swapped.
This process continues for each pair of adjacent elements, pushing the largest unsorted element to its correct position at the end of the list after each pass.
The algorithm repeats, ignoring the sorted portion at the end, until no swaps are needed, indicating that the list is sorted.
Although bubble sort is easy to understand and implement, it is inefficient for large datasets because it repeatedly traverses the list without optimizing the number of comparisons and swaps.

**Time Complexity:**
Best Case: O(n) — Occurs when the list is already sorted, requiring only one pass with no swaps.
Worst Case: O(n²) — Occurs when the list is sorted in reverse order, requiring maximum swaps and comparisons for each element.
Average Case: O(n²) — On average, each element needs to be compared with every other element.

**Space Complexity:**
O(1) — Bubble sort is an in-place algorithm, meaning it requires only a constant amount of extra space regardless of the list size.

**Bubble sort is primarily used for educational purposes to demonstrate basic sorting concepts.
It is rarely used in practice due to its inefficiency compared to other sorting algorithms like quicksort, mergesort, or insertion sort.**
