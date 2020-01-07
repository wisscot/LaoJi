

# 721. Accounts Merge

'''
Basic idea:
Union Find
    1. Save unique email to username dictionary
    2. union all emails under same username
    3. get all emails under same root
Time O(n) (Amortized) where n is the number of total emails
'''

class UnionFind:
    def __init__(self, email_username):
        self.p = {email:email for email in email_username}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
        
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.p[rootx] = rooty

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # save all unique email to username pairs
        email_username = {}
        for username, *emails in accounts:
            for email in emails:
                email_username[email] = username
                
        # union all emails under one username
        uf = UnionFind(email_username)
        for username, *emails in accounts:
            for i in range(len(emails)-1):
                uf.union(emails[i], emails[i+1])
                
        # get unioned each block emails
        root_children = collections.defaultdict(list)
        for email in email_username:
            root_children[uf.find(email)].append(email)
            
        # result format
        res = []
        for root in root_children:
            res.append([email_username[root]]+sorted(root_children[root]))
            
        return res


       