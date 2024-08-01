Because we're rotating the matrix by 90 degrees, the easiest way to do this is to implement the rotation in 
layers. We perform a circular rotation on each layer, moving the top edge to the right edge, the right edge 
to the bottom edge, the bottom edge to the left edge, and the left edge to the top edge.


This algorithm is O (N2), which is the best we can do since any algorithm must touch all N2 elements. 
