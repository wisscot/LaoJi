# 721. Accounts Merge

'''
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
'''


Basic idea: Union Find
    1. Save unique email to username dictionary
    2. union all emails under same username
    3. get all emails under same root

Time O(n) (Amortized) where n is the number of total emails


class UnionFind:
    def __init__(self, uniq_emails):
        self.p = {email:email for email in uniq_emails}

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
        email_to_name = {}
        for username, *emails in accounts:
            for email in emails:
                email_to_name[email] = username
        
        # union all emails under one username
        uf = UnionFind(email_username)
        for username, *emails in accounts:
            for i in range(len(emails)-1):
                uf.union(emails[i], emails[i+1])
                
        # get unioned each block emails
        master_to_emails = collections.defaultdict(list)
        for email in email_username:
            master_to_emails[uf.find(email)].append(email)
            
        # result format
        res = []
        for master in master_to_emails:
            res.append([email_to_name[master]] + sorted(master_to_emails[master]))
            
        return res


       