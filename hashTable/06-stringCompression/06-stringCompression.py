//solution 1

def compressString(string):
    consecutiveString = []
    consecutiveCount = 0
    for i in range(len(string)):
        consecutiveCount+= 1
        if( i+1 >= len(string) or ord(string[i]) !=  ord(string[i+1])  ):
            consecutiveString.append(string[i])
            consecutiveString.append(consecutiveCount)
            consecutiveCount = 0
    
    consecutiveString = ''.join(map(str, consecutiveString))
    
    return consecutiveString if len(consecutiveString) < len(string)  else string
        

v = compressString("aabcccccdd")
 

print("v", v)

// solution 1

// find whether given string is shorter than compressed one later append the value


def checkLength(string):
    compressedLength = 0
    consecutiveCount = 0
    for i in range(len(string)):
        consecutiveCount+= 1
        
        if( i+1 >= len(string) or ord(string[i]) !=  ord(string[i+1])  ):
            compressedLength+= 1 + len(str(consecutiveCount))
            print("compressedLength", compressedLength)
            consecutiveCount = 0
    
    return compressedLength 
        
def compressString(string):
    finallength = checkLength(string)
    if finallength >= len(string):
        return string

    consecutiveString = []
    consecutiveCount = 0
    for i in range(len(string)):
        consecutiveCount+= 1
        if( i+1 >= len(string) or ord(string[i]) !=  ord(string[i+1])  ):
            consecutiveString.append(string[i])
            consecutiveString.append(consecutiveCount)
            consecutiveCount = 0
    
    consecutiveString = ''.join(map(str, consecutiveString))
    
    return consecutiveString 
        

v = compressString("aabcccccdd")
 
print("v", v)
