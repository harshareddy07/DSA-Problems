**Jump Search**
**Definition:**
Jump search is an efficient search algorithm used to find the position of a target element in a sorted collection (like an array or list). 
It combines elements of both linear search and binary search, allowing it to be faster than linear search for sorted collections.
Jump search works by jumping ahead by fixed steps (or "jumps") and then performing a linear search within a small block where the target element is 
likely to be found.

**Explanation:**
In jump search, the collection is divided into blocks of size m (typically √n, where n is the number of elements). 
The algorithm jumps from one block to the next by skipping m elements at a time until it finds a block where the target element might reside.
Once the target block is identified (when the element at the end of the block is greater than or equal to the target), a linear search is performed 
within that block to locate the target.

Jump search is particularly useful for large, sorted arrays where binary search may involve excessive indexing. By using fixed jumps, 
it can eliminate large sections of the search space with each jump.

**Time Complexity:**

Best Case: O(1) — The target element is at the beginning of the collection.
Worst Case: O(√n) — The target element is near the end or does not exist, requiring all jumps and a linear scan of the last block.
Average Case: O(√n) — On average, the search requires about √n comparisons due to the jump and linear scan combination.

**Space Complexity:**

O(1) — Jump search only needs a constant amount of extra space for variables, regardless of the collection's size.
