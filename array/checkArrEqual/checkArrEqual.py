
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        
        if len(a) != len(b):
            return False
    
        return sorted(a) == sorted(b)
    
    def checkEqualDict(self, a, b) -> bool:
        # Using dict
        seta = {}
        result = True
        # Count frequencies in a
        for val in a:
            seta[val] = seta.get(val, 0) + 1
                
         # Decrement for elements in b
        for num in b:
            if num not in seta or seta[num] == 0:
                return False
            seta[num] -= 1
    
        # Check all counts are zero
        for count in seta.values():
            if count != 0:
                return False
    
        return True
