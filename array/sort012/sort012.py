class Solution:
    def sort012(self, arr):
        # code here
        low = 0 # points to the position where the next 0 should go
        mid = 0 # the current element under inspection
        high = len(arr) - 1  # points to where the next 2 should go
        
        
        while mid <= high: 
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high] , arr[mid]
                high -= 1
        
        return arr
