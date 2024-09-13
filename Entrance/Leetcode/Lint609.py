# 609 · 两数和-小于或等于目标值
# 描述
# 给定一个整数数组，找出这个数组中有多少个不同的下标对，满足下标对中的两个下标所对应元素之和小于或等于目标值。返回下标对数。
# 样例
# 例1:

# 输入: nums = [2, 7, 11, 15], target = 24. 
# 输出: 5. 
# 解释:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24
# 例2:

# 输入: nums = [1], target = 1. 
# 输出: 0. 

Idea: onwards two pointers

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        i, j = 0, len(nums)-1
        res = 0
        
        while i < j:
            if nums[i] + nums[j] <= target:
                res += j - i
                i += 1
            else:
                j -= 1
                
        return res