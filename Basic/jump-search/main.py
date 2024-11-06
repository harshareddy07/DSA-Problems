target_pos = -1

def find_target(arr, n):
    m = round(len(arr) ** (1 / 2))  # Size of each jump
    print("m", m )
    l = 0
    r = min(m, len(arr) - 1)  # Start with the first jump size

    # Jump until we find a block where `n` could exist
    while arr[min(r, len(arr) - 1)] < n:
        l = r  # Move to the next block
        r += m
        if l >= len(arr):  # If we've gone out of bounds
            return False

    # Linear search within the identified block
    for i in range(l, min(r + 1, len(arr))):
        if arr[i] == n:
            globals()['target_pos'] = i
            return True

    return False

arr = [1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11, 12, 13, 14, 15]
target = 13

result = find_target(arr, target)
print(f"Target Found at index {target_pos}") if result else print("Target Not Found")
