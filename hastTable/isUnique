#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 

def is_unique_chars(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')  # Compute the index for the character
        if (checker & (1 << val)) > 0: 
            return False
        checker |= (1 << val) # checker | (1 << val)
    return True


# Explanation

Sample Execution for "abac"

Initial Value:
checker = 0 (binary 00000000).

Processing Each Character:

Character 'a':

val = 'a' - 'a' = 0
Check if bit 0 is set: checker & (1 << 0) = 0 & 1 = 0 (not set)
Update checker: checker |= (1 << 0) = 0 | 1 = 1 (binary 00000001)
Character 'b':

val = 'b' - 'a' = 1
Check if bit 1 is set: checker & (1 << 1) = 1 & 2 = 0 (not set)
Update checker: checker |= (1 << 1) = 1 | 2 = 3 (binary 00000011)
Character 'a':

val = 'a' - 'a' = 0
Check if bit 0 is set: checker & (1 << 0) = 3 & 1 = 1 (bit 0 is set)
Since bit 0 is set, it means 'a' has been seen before, so the function returns false.
Character 'c':

This character is not processed because the function already returned false upon 
detecting the duplicate 'a'.
