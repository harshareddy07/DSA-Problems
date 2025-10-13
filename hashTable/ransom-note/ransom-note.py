class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countMag = {}

        for c in magazine:
            countMag[c] = countMag.get(c, 0) + 1
        
        for t in ransomNote:
            if t not in countMag:
                return False
            elif countMag[t] == 1:
                del countMag[t]
            else:
                countMag[t] -= 1

        return True

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
       
        for key, val in ransom.items():
            if key not in mag or mag[key] < val:
                return False
        return True
