# 465. Optimal Account Balancing

'''
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.
'''

Basic idea:
Draw directed graph with IN/OUT
the stable graph is that any node have either in or out (not both)

Preprocess and get each person's net IN / OUT (balances)
so the goal is to match all INs to OUTs
kinda like n backpack problem  -> NP-compelete

So we use brute force: 
person that has balance e.g. [3, 4, -5, 10, -9, -3]
for each person, he/she can transfer the balance to any other one,
but if transfer to another same sign person, 
then the person will have both IN and OUT in the graph,
so we only try to transfer to opposite sign

Algorithm: DFS

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        node_bal = collections.defaultdict(int)
        for node1, node2, val in transactions:
            node_bal[node1] += val
            node_bal[node2] -= val
            
        bals = [bal for bal in node_bal.values() if bal]
        
        return self.min_trans(bals, 0)
        
    def min_trans(self, bals, start):
        if start == len(bals):
            return 0
        
        if bals[start] == 0:
            return self.min_trans(bals, start+1)
        
        res = float('inf')
        for i in range(start+1, len(bals)):
            if bals[i] == 0 or bals[i]*bals[start]>0:
                continue
            # transfer ALL balance of node start to node i
            bals[i] += bals[start]
            res = min(res, 1 + self.min_trans(bals, start+1))
            bals[i] -= bals[start]
            
        return res
        