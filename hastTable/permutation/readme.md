**Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.** 

Note the assumption on line 6. In your interview, you should always check with your interviewer about the 
size of the character set. We assumed that the character set was ASCII.

List Approach : letters = [0] * 128  # Assumption: ASCII
Dictionary Approach : letters = {}

**Time Complexity:**

  List Approach: 𝑂 ( 𝑛 ) O(n) Accessing and updating elements in a list by index is 𝑂 ( 1 ) O(1) due to direct indexing. Hence, counting characters and checking 
  character counts in both s and t are 𝑂 ( 𝑛 ) O(n) operations. 
  
  Dictionary Approach: 𝑂 ( 𝑛 ) O(n) Accessing and updating elements in a dictionary has an average-case time complexity of 𝑂 ( 1 ) O(1) due to hash table 
  implementation. Therefore, counting characters and checking character counts are 𝑂 ( 𝑛 ) O(n) operations. 

**Space Complexity:**

  List Approach: 𝑂 ( 1 ) O(1) The space required is fixed and independent of the input size, as it only depends on the character set size (128 for ASCII). 
  
  Dictionary Approach: 𝑂 ( 𝑘 ) O(k) The space required depends on the number of unique characters in the strings. In the worst case (if all characters are unique and 
  within a large character set like Unicode), this can grow larger than 128. 

**Advantages and Disadvantages:**  
  List Approach: 
    Advantages: Simple and efficient for fixed-size character sets (like ASCII). Predictable space usage. 
    Disadvantages: Limited to small character sets. Not flexible for larger or variable character sets (e.g., Unicode). 
  Dictionary Approach: 
    Advantages: Flexible and handles any character set size. More readable and adaptable. 
    Disadvantages: Potentially higher space usage if the character set is large. Slightly more overhead due to dynamic hashing and potential collisions.
