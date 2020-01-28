# Sorting 

[912. Sort an Array](https://leetcode.com/problems/sort-an-array/)

## Quick Sort

Basic idea: Divide and Conquer

Step 1. choose a randome (or last one) as pivot\
Step 2. put smaller to pivot left, greater to pivot right\
Step 3. then recursive do it for left and right

Code1: easy to explain, use more space, but __Stable__
```python
def quicksort(self, nums):
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)
    lt = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    gt = [v for v in nums if v > pivot]

    return self.quicksort(lt) + eq + self.quicksort(gt)
```

Code2: typical
Time: O(nlogn) Space:O(1)
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, left, right):
    
        if left >= right:
            return 
        pivot = nums[right]
        # ssssssssbbbbbsbssbbbbp
        # l       j    i       r
        j = left  # Do NOT assign 0 to j
        for i in range(left, right): 
            if nums[i] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[right], nums[j] = nums[j], nums[right] # not nums[-1]
        # sssssspbbbbbbbbb
        # l     j        r
        self.quicksort(nums, left, j-1)
        self.quicksort(nums, j+1, right)
```

## Merge Sort

## Counting Sort

if the value of all numbers are between 0 and b\
we can count the numbers in O(n) and then fill into res\
Time: O(n+b)

## Radix Sort 

Sort integers only

```python
# pseudo code
for i = 1 to d
    use a stable sort to sort array A on digit i 
    # counting sort is an option
```

```python
# Radix Sort with base 10

def radixsort(self, nums):
    d = len(str(max(nums)))
    for i in range(d):
        nums = self.coutingsort(nums, i)
    return nums

def coutingsort(self, nums, i):
    # i = 0, 1, ... ,d
    # bar = 1, 10, 100, ...
    boxes = [[] for _ in range(10)]
    bar = 10**i 
    
    for num in nums:
        idx = num//bar%10  # get reverse ith digit
        boxes[idx].append(num)  

    res = []
    for box in boxes:
        res += boxes
        
    return res

```

## Bucket Sort 

Bucket sort assumes that the input is drawn from a uniform distribution and has an average-case running time of O(n)

<br>

__Examples:__\
[164. Maximum Gap](https://leetcode.com/problems/maximum-gap/)

## Time Complexity Analysis

|              | Worse    | Average  | Special      |
|--------------|----------|----------|--------------|
| QuickSort    |          | O(nlogn) |              |
| MergeSort    | O(nlogn) |          |              |
| HeapSort     | O(nlogn) |          |              |
| CountingSort |          |          | O(n+b)->O(n) |
| RadixSort    |          |          | O(d(n+b))->O(n) |
| BucketSort   |          |          | O(n) aver.   |

Comparison Sort: QuickSort, MergeSort and HeapSort

## Stability
> A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.

Stable: Insertion Sort, Merge Sort, Bubble Sort

Unstable: Quick Sort, Heap Sort

## Examples

[399. Nuts & Bolts Problem](https://www.lintcode.com/problem/nuts-bolts-problem/)
\
quick sort, but pivot must be from outside



