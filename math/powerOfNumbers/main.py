class Solution:
    def reverse_exponentiation(self, n):
        # code here
        temp = n
        rev = 0
        while temp > 0:
            rem =  temp % 10
            rev =  rev * 10 + rem
            temp = temp // 10
            
        res = n ** rev
        return res
            
            
