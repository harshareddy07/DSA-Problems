#User function Template for python3

class Solution:
    # Approach 1
    def evenlyDivides(self, n):
        res = 0
        for i in str(n):
            if int(i)!=0 and n % int(i) == 0:
                res += 1  
        
        return res:
    # Approach 2
    def evenlyDivides(self, n):
        res = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            if digit != 0 and n % digit == 0:
                res += 1
            temp //= 10
        return res
