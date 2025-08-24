# Quick Sort with Hoare Partition - Complete Trace

## Step-by-Step Trace: [11, 9, 29, 7, 2, 15, 28]

### Initial Call: quick_sort(elements, 0, 6)

### First Partition: partition(elements, 0, 6)

**Setup:**

- Array: `[11, 9, 29, 7, 2, 15, 28]`
- pivot_index = 0, pivot = 11
- start = 0, end = 6

**Iteration 1:**

1. **Move start pointer right** (find element > 11):

   - start=0: elements[0]=11 ≤ 11 ✓, start++
   - start=1: elements[1]=9 ≤ 11 ✓, start++
   - start=2: elements[2]=29 > 11 ❌, **stop at start=2**

2. **Move end pointer left** (find element ≤ 11):

   - end=6: elements[6]=28 > 11 ❌, end--
   - end=5: elements[5]=15 > 11 ❌, end--
   - end=4: elements[4]=2 ≤ 11 ✓, **stop at end=4**

3. **Check and swap:**

   - start(2) < end(4) → swap elements[2] and elements[4]
   - Array: `[11, 9, 2, 7, 29, 15, 28]`

**Iteration 2:**

1. **Move start pointer right:**

   - start=2: elements[2]=2 ≤ 11 ✓, start++
   - start=3: elements[3]=7 ≤ 11 ✓, start++
   - start=4: elements[4]=29 > 11 ❌, **stop at start=4**

2. **Move end pointer left:**

   - end=4: elements[4]=29 > 11 ❌, end--
   - end=3: elements[3]=7 ≤ 11 ✓, **stop at end=3**

3. **Check condition:**

   - start(4) > end(3) → **exit while loop**

**Final pivot placement:**

- Swap pivot (elements[0]) with elements[end=3]
- Swap elements[0]=11 with elements[3]=7
- Array: `[7, 9, 2, 11, 29, 15, 28]`
- **Return end=3** (pivot's final position)

### Recursive Calls

**Left subarray: quick_sort(elements, 0, 2)**

- Works on: `[7, 9, 2]`
- After sorting: `[2, 7, 9]`

**Right subarray: quick_sort(elements, 4, 6)**

- Works on: `[29, 15, 28]`
- After sorting: `[15, 28, 29]`

### Final Result

- **Sorted array:** `[2, 7, 9, 11, 15, 28, 29]`

## Key Features of Hoare Partition

### Advantages:

- **Fewer swaps:** Makes about 3 times fewer swaps than Lomuto partition
- **Better performance:** Generally faster due to fewer operations
- **Two-way scanning:** More efficient element movement

### Important Notes:

1. **Pivot position:** Pivot doesn't necessarily end up in the exact middle
2. **Boundary handling:** Returns the boundary between smaller and larger elements
3. **Stability:** Not stable (relative order of equal elements may change)
4. **In-place:** Uses O(1) extra space (excluding recursion stack)

## Time Complexity

- **Best Case:** O(n log n) - when pivot divides array evenly
- **Average Case:** O(n log n)
- **Worst Case:** O(n²) - when pivot is always smallest/largest

## Space Complexity

- **O(log n)** - recursion stack space in average case
- **O(n)** - in worst case when tree is skewed

## When to Use

- General-purpose sorting when average-case performance matters
- When in-place sorting is required
- When dealing with primitive data types (not stable sorting needed)

---

*Note: This implementation uses the first element as pivot. For better performance, consider random pivot selection or median-of-three method.*
