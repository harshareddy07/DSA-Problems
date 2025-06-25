class Solution:
    def floorSqrt(self, n): 
    # code here
        i = 1
        while i * i <= n:
            i += 1
        return i - 1
