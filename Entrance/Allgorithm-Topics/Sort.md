# Sorting 

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
Forward two pointers, using last num as pivot
Time: O(nlogn) Space:O(1)
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, left, right):
    
        if left >= right:
            return 
        # optional: choose pivot randomly by adding random.choice(range(left, right+1)) and swap it to the right
        # pivot_index = random.choice(range(left, right + 1))
        # nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        pivot = nums[right]
        # ...ssssssssgegegesssssggggp...
        #    ^       ^    ^         ^
        #    l       i    j         r
        i = left  # Do NOT assign 0 to i
        for j in range(left, right): 
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # not nums[-1]
        # ...sssssspgegegegege...
        #    l     i         r
        self.quicksort(nums, left, i-1)
        self.quicksort(nums, i+1, right)
```

Code 3: typical
Towards two pointers, using mid as pivot
Time: O(nlogn) Space:O(1)
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, left, right): # inclusive
    
        if left >= right:
            return 
        pivot = random.choice(nums[left:right+1])
        i, j = left, right
        # ssssssssgsgegsgegegegg
        # ^       ^    ^       ^
        # l       i    j       r
        while i <= j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        # sesesegegegegege
        # l    ji        r
        # left side are all <= pivot
        # right side are all >= pivot
        self.quicksort(nums, left, j)
        self.quicksort(nums, i, right)
```

Code 4: use three pointers to partition lt, eq, gt
Time: worse case O(nlogn) Space: O(1)
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, left, right):
        if left >= right:
            return 
        pivot = random.choice(nums[left:right+1])
        i, j, k = left, left, right
        while j <= k:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == pivot:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
        # sssssssseeeeeggggg
        # l       i   k    r
        self.quicksort(nums, left, i-1)
        self.quicksort(nums, k+1, right)
```        



## Merge Sort
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)
        return nums
    
    def merge_sort(self, nums):
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1


## Counting Sort (For integers only)

if the value of all numbers are between 0 and b\
we can count the numbers in O(n) and then fill into res\
Time: O(n+b)


## Radix Sort  (For integers only)

```python
# pseudo code
for i = 1 to d  # assume largest number has d digits
    use a stable sort to sort array A on digit i 
    # counting sort is an option with time O((n+10)*d)
```
Time: O(n*d)

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
**A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.**

Stable: Insertion Sort, Merge Sort, Bubble Sort

Unstable: Quick Sort, Heap Sort

## Examples


[912. Sort an Array](https://leetcode.com/problems/sort-an-array/)
\
Sorting Practice

[399. Nuts & Bolts Problem](https://www.lintcode.com/problem/nuts-bolts-problem/)
\
quick sort, but pivot must be from outside

[164. Maximum Gap](https://leetcode.com/problems/maximum-gap/)

TAG
[1057. Campus Bikes](https://leetcode.com/problems/campus-bikes/)
\
Bucket Sort


