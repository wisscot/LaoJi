# MEMO

## Easily made mistakes

1. 2d array get/set on boarder \
   i==0 or j==0 or __i==len(borad)-1 or j==len(board[0])-1__

2. while loop\
   check __i += 1__ in the end of loop\
   check __i += 1__ also in "__continue__" section

3. heapq\
   heapq.heappop(__hq__)  &emsp;  ~~__hp.pop()__~~ \
   heapq.heappush(__hq__, item)\
   
4. equals sign\
   ==  and = 

5. DP\
   T\[__i+1__]  word[i]


## Nameing Convension

1. left, right, mid for two pointers

2. res

3. duplicates for list: nums, items, array

4. node, head, char

3. key_value for dictionary
   char_child for dictionary in trie

