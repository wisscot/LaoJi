# Prefix Sum 

when dealing with __subarray number sum__ problems

## Subarray Sum

```python
presum = list(nums)
for i in range(1, len(nums)):
    presum[i] += presum[i-1]
    # presum[i] = the sum of the first i numbers  0, 1, ..., i

sum(j ... i) = presum[i] - (presum[j-1] if j > 0 else 0)
count = collections.Counter({0:1})
```

TAG
[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
0208G Done

[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

[Lint139. Subarray Sum Closest](https://www.lintcode.com/problem/subarray-sum-closest/)

[Lint402. Continuous Subarray Sum](https://www.lintcode.com/problem/continuous-subarray-sum/)

[403. Continuous Subarray Sum II](https://www.lintcode.com/problem/continuous-subarray-sum-ii/)
\
arr -> circle

[Lint404. Subarray Sum II](https://www.lintcode.com/problem/subarray-sum-ii/)
\
subarray sum to be in a range


# Submatrix Sum

1D -> 2D

TAG
[1074. Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
0208G \
fix i, j then it becomes a 1d subarray sum problem O(n)

