# MEMO


## Easily made mistakes

1. 2d array get/set on boarder \
   i==0 or j==0 or __i==len(borad)-1 or j==len(board[0])-1__

2. while loop\
    __i += 1__ in the end of loop\
    __i += 1__ also in "__continue__" section

3. BFS check if in __visited__

3. heapq\
   ~~__hp.pop()__~~  ->  heapq.heappop(__hq__)  \
   heapq.heappush(__hq__, item)
   
4. equals sign\
   ==  or  = 

5. DP   \
   T = [[0] * (__n+1__) for _ in range(__m+1__)]    \
   T\[__i+1__]   word\[__i__]   \

6. DFS  \
   def search(..., i, j ... )  DO NOT USE i, j (temporary variables)

7. check for variables duplicate misuse, especially i, j, k ... 

8. zip() is an iterator, cannot be used twice 

9. two pointer in recursive, i or j start from last left NOT 0


## Naming Convension

1. left, right, lower, upper, mid, target

2. i, j, k, i_, j_, k_  for new i j k

3. num, val, maxval, minval, accu, incr, item, count, cnt, char

3. nums, vals, items, array, arr, cands

4. node, head, root

6. curr, prev, nxt, idx, index, neib, dist

7. u, v, w, e,  for graph

3. key_value, char_child

8. hqueue

2. res