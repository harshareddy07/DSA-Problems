class Solution:
    def thirdLargest(self,arr):
        
        if len(arr) > 2:
            max_1 = max_2 = max_3 = float('-inf')
            
            for i in range(0, len(arr)):
                if arr[i] >  max_1:
                    max_3 = max_2
                    max_2 = max_1
                    max_1 = arr[i]
                elif arr[i] > max_2:
                    max_3 = max_2
                    max_2 = arr[i]
                elif arr[i] > max_3:
                    max_3 = arr[i]
                    
            return max_3
        else:
            return -1
                
