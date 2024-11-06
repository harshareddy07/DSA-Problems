target_pos = -1

def find_target(arr, n):
    i = 0
    while i < len(arr):
        if arr[i] == n:
            globals() ['target_pos'] = i
            return True
        i+= 1
    return False
    
arr  = [ 4, 9, 3, 2, 6 ,8, 1]
target = 6

result = find_target(arr, target)
print(f"Target Found at {target_pos}") if result else print("Target Not Found")
