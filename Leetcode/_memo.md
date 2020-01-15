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
   
   