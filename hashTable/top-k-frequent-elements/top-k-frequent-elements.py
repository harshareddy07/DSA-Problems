class Solution(object):
    def topKFrequent(self, nums, k):    
     
        res = []
        countByNum = {}
        freqCount = [ [] for i in range(len(nums))]
        print("freqCount", freqCount)
        
        for j in nums:
            countByNum[j] = 1 + countByNum.get(j, 0)
        print("countByNum", countByNum)
        
        for key, value in countByNum.items():
            freqCount[value].append(key)
            
        print("freqCount", freqCount)
        
        for item in range(len(freqCount) -1 , 0, -1):
            for n in freqCount[item]:
                res.append(n)
                if k == len(res):
                    return res
                    
response = Solution()
nums =  [2,2,3,4,5,5,6,6,6]
k = 3
print(response.topKFrequent(nums, k))
