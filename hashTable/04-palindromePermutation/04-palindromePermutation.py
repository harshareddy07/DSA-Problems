def get_char_number(c: str) -> int:
    if 'a' <= c <= 'z':
        return ord(c) - ord('a')
    elif 'A' <= c <= 'Z':
        return ord(c.lower()) - ord('a')
    return -1

def buildObject(phrase):
    print("v", ord('z'))
    table = [0] * 26
    for index,c in enumerate(phrase):
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
    return table


def checkPalindrome(x):
    alreadyOddExist = False
    for index, j in enumerate(x):
        print("x", j)
        if j%2==1:
            if alreadyOddExist:
                return False
            alreadyOddExist = True
    return True
            

def palindromePermutation(phrase) :
    c_table = buildObject(phrase)
    print("c",c_table)
    return checkPalindrome(c_table)


v = palindromePermutation("tacos atc")
print("v", v) 



// solution 2


def get_char_number(c: str) -> int:
    if 'a' <= c <= 'z':
        return ord(c) - ord('a')
    elif 'A' <= c <= 'Z':
        return ord(c.lower()) - ord('a')
    return -1

def buildObject(phrase):
    print("v", ord('z'))
    table = [0] * 26
    countOdd = 0
    for index,c in enumerate(phrase):
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                countOdd+= 1
            else:
                countOdd-= 1
    return countOdd <= 1


def palindromePermutation(phrase) :
    return buildObject(phrase)

