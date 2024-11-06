
**Linear Search**

**Definition:**
Linear search is a straightforward algorithm used to find a specific element within a collection (like an array or list). The search starts at the beginning of the collection and checks each element one by one until the desired element is found.

**Explanation:**
In a linear search, each element of the list is compared with the target value. If a match is found, the position of the element is returned; otherwise, if the search reaches the end of the collection without finding the target, it concludes that the element does not exist in the collection. This algorithm is efficient for small or unsorted collections but can be slow for larger datasets.

**Time Complexity:**

Best Case: O(1) — The element is found at the beginning of the collection.
Worst Case: O(n) — The element is at the end of the collection or not present at all, requiring a comparison with every element.
Average Case: O(n) — On average, half of the elements need to be checked before finding the target.

**Space Complexity:**

O(1) — Linear search requires only a constant amount of extra space for a few variables, regardless of the size of the collection.
