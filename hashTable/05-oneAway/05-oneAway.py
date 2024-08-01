def oneEditAway(first, second):
    
    if abs(len(first) - len(second) ) > 1:
        return False
    
    # find shorter and longer lengths
    s2 = first if len(first) < len(second) else second
    s1 = second if len(first) < len(second) else first
    print("s1 -  s2", s1, s2)
    index1 = 0
    index2 = 0
    foundDifference = False
    while index1 < len(s1) and index2 < len(s2):
        if ord(s1[index1]) != ord(s2[index2]):
            if foundDifference:
                return False
            foundDifference = True
            # On replace, move shorter pointer
            if len(s1) == len(s2):
                index2+= 1
        else:
            # move pointer for shorter string
            index2+= 1
        # Always move pointer for longer string (by default)
        index1+= 1
        
    return True
    
# oneEditinsert
v = oneEditAway("pal", "pale")
# oneEditRemoval
v2= oneEditAway("pale", "pal")
# oneEditReplace
v3 = oneEditAway("pale", "pble")
print("v", v2, v2, v3)
            
  
        
        
    
    
