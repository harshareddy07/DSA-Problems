# Find Last Digit of a^b (Large Exponent)

## 🚀 Problem Statement

You are given two non-negative integers `a` and `b` as **strings**. Your task is to compute the **last digit** of the value of \( a^b \), 
without calculating the entire power directly.

### Constraints:
- `a` and `b` can be **very large** (up to 10⁵ digits)
- Return only the **last digit** of \( a^b \)

---

## 💡 Examples

### Example 1:
Input: a = "3", b = "10"
Output: 9
Explanation: 3^10 = 59049 → Last digit = 9

### Example 2:
Input: a = "6", b = "2"
Output: 6
Explanation: 6^2 = 36 → Last digit = 6
---

## 🧠 Approach

### 🔁 Step 1: Use Last-Digit Cycles

The last digit of powers of any digit 0–9 follows a **repeating cycle**. For example:

| Last Digit | Cycle of Last Digits for a^1, a^2, ... |
|------------|----------------------------------------|
| 0          | [0]                                    |
| 1          | [1]                                    |
| 2          | [2, 4, 8, 6]                            |
| 3          | [3, 9, 7, 1]                            |
| 4          | [4, 6]                                  |
| 5          | [5]                                    |
| 6          | [6]                                    |
| 7          | [7, 9, 3, 1]                            |
| 8          | [8, 4, 2, 6]                            |
| 9          | [9, 1]                                  |

These cycles repeat indefinitely, so we can reduce the problem to finding the **correct index** in the cycle.

---

### 🔁 Step 2: Compute `b % cycle_len` Digit-by-Digit

Since `b` is very large (as a string), we can't convert it to an integer directly. Instead, we compute:

rem = 0
for digit in b:
    rem = (rem * 10 + int(digit)) % cycle_len
This gives us b % cycle_len efficiently.

If rem == 0, we use the last index in the cycle.

Else, we use cycle[rem - 1].

