
def sort_list(arr):
    for i in range(len(arr)):
        minPos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minPos] :
                minPos = j
                
        temp = arr[i]
        arr[i] = arr[minPos]
        arr[minPos] = temp
    return arr
        
arr  = [ 4, 9, 3, 2, 6 ,8, 1]


sort_list(arr)
print(f"Sorted List is {arr}") 
