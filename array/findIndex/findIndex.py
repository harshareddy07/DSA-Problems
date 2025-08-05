class Solution:
    def search(self, arr, x):
        # code here
        
        for i in range(0, len(arr)):
            if arr[i] == x:
                return i
                
        return -1
        
    def search2(self, arr, x):
        return next((i for i, val in enumerate(arr) if val == x), -1)
