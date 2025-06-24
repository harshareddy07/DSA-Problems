class Solution:
    def gcd(self, a, b):
        ## Approach 1
        res = min(a,b)       
        while res > 0 :
            if a % res == 0 and b % res ==0:
                break
            res -= 1  
        return res
        
        ## Approach 2
        while b != 0:
            a, b = b, a % b
        return a
