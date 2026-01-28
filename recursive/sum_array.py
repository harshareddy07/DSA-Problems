def sum_array(nums=[]):
    if len(nums) == 0:  # Handle empty array
        return 0
    if len(nums) == 1 :
        return nums[0]
        
    return nums[0] + sum_array(nums[1:])
    
    
print(sum_array([1,2,3,4,5]))
