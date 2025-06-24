class Solution:
    def gcd(self, a, b):
        min_d = min(a,b)
        res = min_d
        
        while res > 0 :
            if a % res == 0 and b % res ==0:
                break
                
            res -= 1
            
        return res
