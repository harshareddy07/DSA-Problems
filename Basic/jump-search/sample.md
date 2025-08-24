Initial Call: quick_sort([11, 9, 29, 7, 2, 15, 28], 0, 6)  
First Partition Call: partition(elements, 0, 6)  

<pre>
Initial setup:  
Array: [11, 9, 29, 7, 2, 15, 28]
pivot_index = 0, pivot = 11
start = 0, end = 6
</pre>

Step-by-step partition process:
Iteration 1:

Move start pointer right: find first element > pivot (11)
<pre>
start=0: elements[0]=11 ≤ 11, start++
start=1: elements[1]=9 ≤ 11, start++
start=2: elements[2]=29 > 11, stop at start=2
</pre>

Move end pointer left: find first element ≤ pivot (11)
<pre>
end=6: elements[6]=28 > 11, end--
end=5: elements[5]=15 > 11, end--
end=4: elements[4]=2 ≤ 11, stop at end=4
</pre>

start(2) < end(4), so swap elements[2] and elements[4]
Array becomes: [11, 9, 2, 7, 29, 15, 28]

Iteration 2:

Continue from start=2, end=4
Move start right:

start=2: elements[2]=2 ≤ 11, start++
start=3: elements[3]=7 ≤ 11, start++
start=4: elements[4]=29 > 11, stop at start=4

Move end left:

end=4: elements[4]=29 > 11, end--
end=3: elements[3]=7 ≤ 11, stop at end=3


start(4) > end(3), so exit while loop

Final swap:

Swap pivot (elements[0]) with elements[end] where end=3
Swap elements[0]=11 with elements[3]=7
Array becomes: [7, 9, 2, 11, 29, 15, 28]
Return end=3 (pivot's final position)

Recursive Calls:
Left subarray: quick_sort(elements, 0, 2)

Array section: [7, 9, 2]
After partitioning and recursive calls: [2, 7, 9]

Right subarray: quick_sort(elements, 4, 6)

Array section: [29, 15, 28]
After partitioning and recursive calls: [15, 28, 29]
