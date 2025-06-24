# Count Digits That Evenly Divide a Number

## Problem Statement
Given a positive integer `n`, count the number of digits in `n` that divide `n` evenly (without leaving a remainder). Ignore digits that are `0`.

## Approach 1: Using String Conversion

Convert the number n to a string.

Iterate over each character (digit) in the string.

Convert the character back to integer and check if it divides n.

Increment the count if condition matches.

**Time Complexity**
Converting integer n to string takes O(n) time, where n is the number of digits.

Looping through the string takes O(n).

Overall time complexity: O(n) + O(n) = O(2n) → O(n) (constants ignored in Big O).

**Space Complexity**
The string representation of n requires O(n) space.

Additional variables use O(1) space.

Total space complexity: O(n).

**Approach 2: Using Mathematical Operations (% and //)**

Use modulo % to extract the last digit.

Check if it divides n evenly.

Remove the last digit using integer division //.

Repeat until all digits are processed.

**Time Complexity**
The loop runs once per digit, so O(n) time.

No string conversion overhead.

Overall time complexity: O(n).

**Space Complexity**
Uses only a few integer variables.

Constant space usage: O(1).

**Note:**
Both approaches scale linearly with the number of digits. However, Approach 2 saves memory and performs roughly twice as fast in 
practice because it avoids creating a string.
