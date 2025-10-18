class Solution(object):
    def longestConsecutive(self, nums):    
     
        numSet = set(nums)
        print("numSet", numSet)
        
        longestStr = 0
        for n in nums:
            if (n-1) not in numSet:
                currentLength = 0
                while (n+currentLength) in numSet:
                    currentLength += 1
                longestStr = max(currentLength, longestStr)
        return longestStr
            
response = Solution()
nums =  [201,301, 105, 302, 103, 102, 303, 101, 104]
print(response.longestConsecutive(nums))
