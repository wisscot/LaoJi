# 1153. String Transforms Into Another String

'''
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.
'''

Basic idea: Graph

1. since all the same char will be changed at once, 
   same souce cannot be point to different target
   e.g. a -> b   a -> c    are not acceptable
   
2. plot the Graph
   for a chain a -> b -> c 
   we can do change b to c, then a to b, then a is free
   for a cycle a -> b -> c -> a
   we can use extra char, e.g. d, change c to d,
   the cycle becomes a -> b -> c and d -> a, which is 
   d -> a -> b -> c
   
3. if there are all cycles and all 26 chars are used, 
   then, there is no way to break,
   one exception is every char point to itself, then no need to break
   
4. if number of chars (have indegree) < 26, then there is always a way to break
   Case 1 - a floating node, obviously yes
   Case 2 - node point toward one in a cycle
            a ->  b -> c -> d 
                       ^ ---  
            in this case, we break it by change d to b, graph becomes
            a -> b -> c -> d
            
So, the conclusion is 
do the sanity check (step 1) first, then
if indegree nodes < 26, then always a way to crack it
if indegree nodes == 26, then no, except str1 == str2

indegree nodes are all unique chars in str2, so len(set(str2))
            

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        
        # Idea 1
        mapping = {}
        for char1, char2 in zip(str1, str2):
            if mapping.setdefault(char1, char2) != char2:
                return False
            
        # Idea 4
        if len(set(str2)) < 26:
            return True
        
        # Idea 3
        return str1 == str2


