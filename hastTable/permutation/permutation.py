

def check(s, t):
  if(len(s) != len(t)):
    return False

  letters = [0] * 128 
  for i in s:
    
    letters[ord(i)]++

  for j in t:
    letters[ord(j)]--
    if letters[ord(j)] < 0 :
      return False
  return True
    
