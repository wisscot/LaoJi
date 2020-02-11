# 380. Insert Delete GetRandom O(1)

'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
'''

Basic idea:
random_get O(1) -> list
insert O(1) -> hashtable
remove O(1) -> not keeping order -> list


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.num_idx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_idx:
            return False
        
        self.nums.append(val)
        self.num_idx[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_idx:
            return False
        
        idx = self.num_idx[val]
        if idx == len(self.nums) - 1: # be careful with switching last item
            self.nums.pop()
            self.num_idx.pop(val)
        else:
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
            self.nums.pop()
            self.num_idx.pop(val)
            self.num_idx[self.nums[idx]] = idx
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)
