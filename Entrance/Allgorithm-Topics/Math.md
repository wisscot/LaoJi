# Math

## n choose k problem

How many ways to put n balls into k boxes?

| Case | n balls           | k boxes           | number of ways |
|------|-------------------|-------------------|----------------|
| 1    | Distinguishable   | Distinguishable   | k^n            |
| 2    | Distinguishable   | Indistinguishable |                |
| 3    | Indistinguishable | Distinguishable   |                |
| 4    | Indistinguishable | Indistinguishable |                |

### Case 1: Easy
just put ball into boxes one by one, \
each has k choices, so k^n

### Case 2 - 4:  
Solve a sub-problem with __no empty boxes__ first,  \
then the original problem becomes trivial

### Case 2: 
non-empty: 
say f(n, k) is how many way to fit n labaled balls into k unlabeled boxes,\
f(n, k) = f(n-1, k-1) + k * f(n-1, k)          \

Explanation: focus on first ball that we currently have, two cases:
   1. this ball is in a box alone -> f(n-1, k-1)
   2. this ball is with some other ball/balls, so we distribute other balls first, \
      then choose one box to add -> k * f(n-1, k)

Final result = f(n,k) + f(n,k-1) + ...   

### Case 3:
non-empty:
f(n, k) = C(n-1, k-1)

Basic idea is to insert k-1 separators into n-1 gaps    \

Fianl result = f(n, k) + k * f(n, k-1) + C(k, 2) * f(n, k-2) + ...      \
basically choose 1/2/3/... box to be empty

Another way to think: we have n+k-1 spaces, we choose k-1 as separator, and label the sections 1,2,3... as box number,\
Final result = C(n+k-1, k-1)

### Case 4:
non-empty:
f(n, k) = f(n-1, k-1) + f(n-k, k) 

Explanation: take one ball out that we currently have, two cases:
   1. one ball is in a box alone -> f(n-1, k-1)
   2. every box has >= 2 balls, so we distribute one to each boxes first,   \
      then do f() again, so every box will have at least 2 balls -> f(n-k, k)   \
   (Thought: this is similar to Case 2)

Final result = f(n,k) + f(n,k-1) + ...   
