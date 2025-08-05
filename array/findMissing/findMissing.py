class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1  # Since one number is missing
        total = n * (n + 1) // 2  # Sum of 1 to n
        return total - sum(arr)
    def find_missing_custom_range(arr):
        start = min(arr)
        end = max(arr)
        
        xor_full = 0
        xor_arr = 0
    
        for i in range(start, end + 1):
            xor_full ^= i
    
        for num in arr:
            xor_arr ^= num
    
        return xor_full ^ xor_arr
