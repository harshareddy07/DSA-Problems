**Remove Dups: Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed?**

Solution  1 :

  **In order to remove duplicates from a linked list, we need to be able to track duplicates. A simple hash table 
  will work well here**


Solution  2 :

  **Follow Up: No Buffer Allowed 
  lfwe don't have a buffer, we can iterate with two pointers: current which iterates through the linked list, 
  and runner which checks all subsequent nodes for duplicates.**
  
  This code runs in O ( 1) space, but O ( N2) time
