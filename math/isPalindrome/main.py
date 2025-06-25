#User function Template for python3

class Solution:
    def isPalindrome(self, n):
		# Code here
		isPalindrome = True
		num = str(n)
		l = 0
        r = len(num)-1
		while l < r :

            if num[l] != num[r]:
                isPalindrome = False
                break
		    l +=1
		    r -= 1
            
        return isPalindrome
