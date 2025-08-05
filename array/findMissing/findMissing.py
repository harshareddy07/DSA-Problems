class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1  # Since one number is missing
        total = n * (n + 1) // 2  # Sum of 1 to n
        return total - sum(arr)
