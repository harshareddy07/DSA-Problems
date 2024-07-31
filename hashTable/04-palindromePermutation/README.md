**Palindrome Permutation: Given a string, write a function to check if it is a permutation of 
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A 
permutation is a rearrangement of letters. The palindrome does not need to be limited to just 
dictionary words.**

EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "taco cat'; "atco eta·; etc.)

For example, we know tactcoapapa is a permutation of a palindrome because it has two Ts, four As, two Cs, two Ps, and one 0. That O would be the center of 
all possible palindromes. 

To be more precise, strings with even length (after removing all non-letter characters) must have 
all even counts of characters. Strings of an odd length must have exactly one character with 
an odd count. Of course, an "even" string can't have an odd number of exactly one character, 
otherwise it wouldn't be an even-length string (an odd number+ many even numbers= an odd 
number). Likewise, a string with odd length can't have all characters with even counts (sum of 
evens is even). It's therefore sufficient to say that, to be a permutation ot a palindrome, a string
