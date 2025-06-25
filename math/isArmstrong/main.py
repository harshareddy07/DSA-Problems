#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        res = 0
        for i in str(n):
            res = res + int(i) ** 3
        
        return True if res == n else False
