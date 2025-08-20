class Solution:
	def twoSum(self, arr, target):
		visit = {}
        for index, n in enumerate(arr):
            rem = target - n 
            if rem in visit:
                return True
            visit[n] = index
        return False
