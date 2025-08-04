class Solution:
    def get_min_max(self, arr):
        min = max = arr[0] 
       
        
        for i in range(1, len(arr)):
            if arr[i] < min:
                min  = arr[i] 
            elif  arr[i] > max:
                max = arr[i]
        
        return min,max

  
