class Solution:
    def frequencyCount(self, arr):
        #  code here


        freq = {}
        
        for i in range(0,len(arr)):
            freq[arr[i]]  = freq.get(arr[i], 0) + 1
            
        for i in range(1,len(arr)+1):
            arr[i-1] = freq.get(i, 0)
            
        return arr
            
            
