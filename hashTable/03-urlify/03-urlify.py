
def replaceSpaceWith(str, trueLength):
   
    spaceCount = 0
    index = 0

    for c in range(trueLength):
        if(str[c] == ' '):
            spaceCount+=1
    // find total length required
    index = trueLength + spaceCount*2
 
    s_list = list(str)
    for ind in range(trueLength - 1, -1, -1):
         // copy the character to a new string if there is space if there is space then fill 3 places with %20
        if str[ind] != " ":
            s_list[index-1] = str[ind]
            index-=1
        else:
            s_list[index-1] = "0"
            s_list[index-2] = "2"
            s_list[index-3] = "%"
            index = index - 3
    
    return ''.join(s_list)

v = replaceSpaceWith('Mr John Smith    ', 13)
print("v", v)
