target_pos = -1

def find_target(arr, n):
 
    l = 0
    r = len(arr) - 1  
    while l <= r:
         # Calculate the two mid-points
        mid1 = l +  (r - l) // 3
        mid2 = r -  (r - l) // 3
        print("mid1", mid1, mid2)
         # Check if the target is at either mid-point
        if arr[mid1] == n or arr[mid2] == n:
            globals()['target_pos'] = mid1 if arr[mid1] == n else mid2
            return True
     
        else:
           
            if n < arr[mid1]:
                r = mid1  - 1
            elif n > arr[mid2]:
                l = mid2 + 1
            # n > arr[mid1] and n < arr[mid2]:
            else:
                l = mid1 + 1
                r = mid2 - 1

    return False

arr = [1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11, 12, 13, 14, 15]
target = 13

result = find_target(arr, target)
print(f"Target Found at index {target_pos}") if result else print("Target Not Found")
