
def sort_list(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
        
arr  = [ 4, 9, 3, 2, 6 ,8, 1]


sort_list(arr)
print(f"Sorted List is {arr}") 
