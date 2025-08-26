class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        local_sum = 0
        for num in nums:
            local_sum = max(local_sum + num, num)
            max_sum = max(max_sum, local_sum)
        return max_sum
