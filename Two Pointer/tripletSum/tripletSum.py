class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
            arr.sort()  # Step 1: Sort the array
            n = len(arr)
        
            for i in range(n - 2):
                l, r = i + 1, n - 1  # Two pointers
                while l < r:
                    curr_sum = arr[i] + arr[l] + arr[r]
        
                    if curr_sum == target:
                        return True  # Found a triplet
                    elif curr_sum < target:
                        l += 1  # Increase sum
                    else:
                        r -= 1  # Decrease sum
        
            return False
