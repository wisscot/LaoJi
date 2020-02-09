# 1349. Maximum Students Taking Exam

Basic idea: Bit Mask and DP

use 0, 1 to represent if a seat is occupied by a student or not,
for a row, the representation 1001001110 can be transfered to a integer

for a proposed candidate x = 1001001110, we can use x & (x >> 1) to check if any student have a right side neighbor student,
x & (x << 1) to check the left side
x & (prevx << 1) to check current x and previous x left side, etc. 

DP: get all current row seating possibilities (masks) and accumulative students per each mask

for every prev row masks,
try every possible masks at current row, (000000, 000001, 0000010, ... )
skip the one have conflict with broken chairs or can cheat (1's left, right, upperleft or upperright is 1)
save the maximum



class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        
        m, n = len(seats), len(seats[0])
        
        prev_count = {0: 0}
        for row in seats:
            curr_count = {}
            
            ban_mask = int(''.join(row).replace('#','1').replace('.','0'), 2)
            
            for prevmask, prevcnt in prev_count.items():
                for currmask in range(1<<n):
                    if currmask & ban_mask:
                        continue
                    if (currmask & currmask << 1) or (currmask & currmask >> 1):
                        continue
                    if (currmask & prevmask << 1) or (currmask & prevmask >> 1):
                        continue
                    currcnt = prevcnt + bin(currmask).count('1')
                    curr_count[currmask] = max(curr_count.get(currmask,0), currcnt)
            
            prev_count = curr_count
            
        return max(prev_count.values()) if prev_count else 0
         
