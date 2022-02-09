# 1088. Confusing Number II

'''
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.
'''

Basic idea:

Calculate how many numbers consists of 0, 1, 6, 8, 9

Calculate how many numbers above are not confusing number, which is rotation = original

return the difference



mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
class Solution:
    def confusingNumberII(self, N: int) -> int:
        
        self.N = N
        
        total_num = self.total_num(str(N))
        
        strob_num = self.strob_num()
        
        return total_num - strob_num
    
    
    def total_num(self, num: str):
        
        if not num:
            return 1
        
        res = sum(int(x) < int(num[0]) for x in mapping) * 5 **(len(num)-1)
        
        if num[0] in mapping:
            res += self.total_num(num[1:])
            
        return res
    
    def strob_num(self):
        
        res = [0]
        
        for i in range(1, len(str(self.N)) + 1):
            self.search(['-1']*i, 0, i-1, res)
            
        return res[0]
    
    def search(self, nums, left, right, res):
        
        if left > right:
            if int(''.join(nums)) < self.N:
                res[0] += 1
            return
        
        for k, v in mapping.items():
            nums[left], nums[right] = k, v
            
            if len(nums) > 1 and nums[0] == '0':
                continue
                
            if left == right and k != v:
                continue
            
            self.search(nums, left+1, right-1, res)
        
        