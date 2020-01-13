163. Missing Ranges

Basic idea:
find the start and end the range,
add lower-1 and upper+1
then go left to right

Time O(n)


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        import bisect
        i = bisect.bisect_left(nums, lower)
        j = bisect.bisect_right(nums, upper)
        
        array = [lower-1] + nums[i:j] + [upper+1]
        
        res = []
        for i in range(1, len(array)):
            if array[i] - array[i-1] > 1:
               self.save_result(array, i, res)
               
        return res
        
    def save_result(self, array, i, res):
        if array[i] - array[i-1] == 2:
            res.append(str(array[i]-1))
        else:
            res.append(str(array[i-1]+1) + '->' + str(array[i]-1))