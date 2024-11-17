**Insertion Sort**
**Definition:**
Insertion sort is a simple and intuitive sorting algorithm that builds a sorted portion of the array one element at a time. It works by picking elements from the unsorted portion of the array and inserting them into the correct position in the sorted portion.

**Explanation:**
Insertion sort mimics the way people often sort playing cards in their hands:

The algorithm starts with the first element, assuming it is already sorted.
It then picks the next element and compares it with elements in the sorted portion, shifting larger elements one position to the right to make room for the new element.
The new element is inserted in its correct position, maintaining the sorted order.
This process repeats for all elements until the entire array is sorted.
Insertion sort is particularly efficient for small or nearly sorted datasets because it requires minimal element movement. However, its performance degrades with larger datasets due to its nested loop structure.

**Time Complexity:**

Best Case: O(n) — Occurs when the array is already sorted, as only one comparison per element is needed.
Worst Case: O(n²) — Occurs when the array is sorted in reverse order, requiring maximum comparisons and shifts for each element.
Average Case: O(n²) — On average, each element needs to be compared and shifted halfway through the sorted portion.

**Space Complexity:**

O(1) — Insertion sort is an in-place algorithm, meaning it requires only a constant amount of extra space regardless of the array size.


**For small datasets where the simplicity of the algorithm outweighs its inefficiency for large inputs.
When the dataset is already mostly sorted, as insertion sort can sort such datasets very quickly.**
