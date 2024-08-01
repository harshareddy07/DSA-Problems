**One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away.**


**EXAMPLE** 

pale, ple -> true 

pales, pale -> true 

pale, bale -> true 

pale, bae -> false

**Explanation**

  • Replacement : Consider two strings, such as bale and pale, that are one replacement away. Yes, that does mean that you could 
              replace a character in bale to make pale. But more precisely, it means that they are different only in one place. 
              
  • Insertion : The strings apple and aple are one insertion away. This means that if you compared the
                strings, they would be identical-except for a shift at some point in the strings.
                
  • Removal : The strings apple and aple are also one removal away, since removal is just the inverse of insertion
