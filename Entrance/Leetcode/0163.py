163. Missing Ranges

Basic idea:
find the start and end the range,
add lower-1 and upper+1
then go left to right

Time O(n)


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        arr = [num for num in nums if lower <= num <= upper]
        arr = [lower-1] + arr + [upper+1]
        
        res = []
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1] + 1:
                continue
                
            if arr[i] == arr[i-1] + 2:
                res.append(str(arr[i]-1))
            else:
                res.append(str(arr[i-1]+1) + '->' + str(arr[i]-1))
                
        return res