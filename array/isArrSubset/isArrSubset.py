#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        
        subS = {}
     
        for num in a:
            subS[num] = subS.get(num,0) + 1
        
        for num in b:
            if subS.get(num,0) == 0:
                return False
            subS[num] -= 1
            
        return True
    
