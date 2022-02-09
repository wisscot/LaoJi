

class Solution:
    def backPackIII(self, A, V, m):
        # write your code here
        
        T = [0]*(m+1)
        for a,v in zip(A,V):
            for i in range(m+1):
                if (i==0 or T[i]) and i+a <= m:
                    T[i+a] = max(T[i+a], T[i]+v)
        return max(T)