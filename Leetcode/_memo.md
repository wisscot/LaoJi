# MEMO

## Easily made mistakes

1. 2d array get/set on boarder \
   i==0 or j==0 or __i==len(borad)-1 or j==len(board[0])-1__

2. while loop\
    __i += 1__ in the end of loop\
    __i += 1__ also in "__continue__" section

3. BFS check if in __visited__

3. heapq\
   ~~__hp.pop()__~~ &emsp;   heapq.heappop(__hq__)  \
   heapq.heappush(__hq__, item)
   
4. equals sign\
   ==  and = 

5. DP\
   T\[__i+1__]  &emsp;  word\[__i__]


## Naming Convension

1. left, right, lower, upper, mid, target for two pointers

2. i, j, k, i_, j_, k_  for new i j k

3. num, val, accu, item, count, cnt, char

3. duplicates for list: nums, vals, items, array, arr

4. node, head, root

6. curr, prev, nxt, idx, index, neib, dist

7. u, v, w, e,  for graph

3. key_value for dictionary
   char_child for dictionary in trie

8. hqueue

2. res