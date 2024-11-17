
def sort_list(arr):
    for i in range(1, len(arr)):
        j = i - 1
        i  = i
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
        
arr  = [ 4, 9, 3, 2, 6 ,8, 1]


result = sort_list(arr)
print(f"Sorted List is {arr}") if result else print(" Not Found")
