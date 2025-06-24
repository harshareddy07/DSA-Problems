class Solution:
    def getLastDigit(self, a: str, b: str) -> int:
        # Step 1: Get the last digit of base a
        last_digit = int(a[-1])  # e.g., a = "432" → last_digit = 2
        
        # Edge case: anything to the power 0 is 1
        if b == "0":
            return 1

        # Step 2: Map of repeating last-digit cycles
        cycles = {
            0: [0],
            1: [1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5],
            6: [6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1]
        }

        cycle = cycles[last_digit]
        cycle_len = len(cycle)

        # Step 3: Get b % cycle_len using string
        rem = 0
        for digit in b:
            rem = (rem * 10 + int(digit)) % cycle_len
        # Example: b = "100", cycle_len = 4
        # → rem = 0 (so we'll take the last item in the cycle)

        # Step 4: Use correct index in cycle
        index = rem - 1 if rem != 0 else cycle_len - 1
        return cycle[index]
