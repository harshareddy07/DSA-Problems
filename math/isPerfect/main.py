import math
class Solution:
    def isPerfect(self, n):
         
        if n <= 1:
            return False
        
        res = 1  # 1 is a proper divisor for all n > 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                res += i
                if i != n // i:  # avoid double-counting square roots
                    res += n // i
        
        return res == n
