**Approaches
1. Brute Force**
Check all numbers from min(a, b) down to 1 to find the largest divisor common to both.

def gcd(a, b):
    res = min(a, b)
    while res > 0:
        if a % res == 0 and b % res == 0:
            return res
        res -= 1
**Time Complexity: O(min(a, b)) — inefficient for large inputs

Space Complexity: O(1)

Drawback: Too slow, causes Time Limit Exceeded (TLE) for big numbers.**

**2. Euclidean Algorithm (Recommended)**
Uses the property gcd(a, b) = gcd(b, a % b) recursively until b == 0.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
**Time Complexity: O(log max(a, b)) — very efficient

Space Complexity: O(1)

Note: Works regardless of the order of inputs.**

