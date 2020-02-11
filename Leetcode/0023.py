# 23. Merge k Sorted Lists

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

Solution 0: Brute Force
Time O(nlogn) where n is the total number of nodes

Solution 1: Use merge two sorted lists which takes O(n)
merge every two for each layer
Time O(nlogk)

Solution 1+: Use merge two sorted lists which takes O(n)
Divide and Conquer (top down)
Time O(nlogk)

Solution 2: Heapq
Time: O(nlogk)



# Solution 1
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        newlists = []
        for i in range(0, len(lists), 2): # use range instead of len()//2
            newlists.append(self.mergetwo(lists[i:i+2]))
        return self.mergeKLists(newlists)
        
    def mergetwo(self, lists):
        if len(lists) == 1:
            return lists[0]
        
        head1, head2 = lists[0:2]
        dummy = ListNode(0)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        if head1:
            node.next = head1
        elif head2:
            node.next = head2
            
        return dummy.next
            


# Solution 1+
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists)//2 
        left = self.mergeKLists(lists[:mid]) # if mid = (l+r)//2 then, [:mid+1]
        right = self.mergeKLists(lists[mid:])
        
        return self.mergetwo(left, right)
        
    def mergetwo(self, head1, head2):        
        dummy = ListNode(0)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        if head1:
            node.next = head1
        elif head2:
            node.next = head2
            
        return dummy.next
            

# Solution 2
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        hqueue = [(node.val, idx, node) for idx, node in enumerate(lists) if node]
        heapq.heapify(hqueue)  # have to heapify first
        
        dummy = ListNode(0)
        curr = dummy
        
        idx = len(lists) # not len(hqueue) because there might be empty node
        while hqueue:
            _, _, nextnode = heapq.heappop(hqueue)
            curr.next = nextnode
            curr = curr.next
            if curr.next:
                heapq.heappush(hqueue, (curr.next.val, idx, curr.next)) # remember add hqueue
                idx += 1
                
        return dummy.next
            