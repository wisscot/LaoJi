# Prefix Sum 

when dealing with __subarray number sum__ problems

## Subarray Sum

```python
presum = [0]
for num in nums:
    presum.append(presum[-1]+num)

# presum[i] = sum nums[0], nums[1], ... nums[i-1]
# sum i,...,j = presum[j+1] - presum[i]
```

[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

[Lint139. Subarray Sum Closest](https://www.lintcode.com/problem/subarray-sum-closest/description?_from=ladder&&fromId=106)

[Lint402. Continuous Subarray Sum](https://www.lintcode.com/problem/continuous-subarray-sum/description?_from=ladder&&fromId=106)

[403. Continuous Subarray Sum II](https://www.lintcode.com/problem/continuous-subarray-sum-ii/my-submissions)
\
arr -> circle

[Lint404. Subarray Sum II](https://www.lintcode.com/problem/subarray-sum-ii/description?_from=ladder&&fromId=106)
\
subarray sum to be in a range


# Submatrix Sum

1D -> 2D

[Lint405. Submatrix Sum](https://www.lintcode.com/problem/submatrix-sum/description?_from=ladder&&fromId=106)
\
fix i, j then it becomes a 1d subarray sum problem O(n)

