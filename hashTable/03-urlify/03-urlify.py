
def replaceSpaceWith(str, trueLength):
    print("st", str)
    spaceCount = 0
    index = 0

    for c in range(trueLength):
        if(str[c] == ' '):
            spaceCount+=1
    
    index = trueLength + spaceCount*2
    print("index", index, spaceCount)
    s_list = list(str)
    for ind in range(trueLength - 1, -1, -1):
        print("i", ind, index)
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
