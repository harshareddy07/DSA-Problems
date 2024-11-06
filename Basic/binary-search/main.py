target_pos = -1

def find_target(arr, n):
    l = 0 
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == n:
            globals() ['target_pos'] = mid
            return True
        else:
          if arr[mid] < n:
            l = mid+1
          else:
            r = mid-1
        
    return False
    
arr  = [ 2 , 6, 8, 12, 44, 55 , 77]
target = 8

result = find_target(arr, target)
print(f"Target Found at {target_pos}") if result else print("Target Not Found")
