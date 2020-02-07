# 1146. Snapshot Array

'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
'''

Basic idea: 

Save only the changes, then binary search

class SnapshotArray:

    def __init__(self, length: int):
        self.snapid = 0
        self.A = [[[-1, 0]] for _ in range(length)] # snapid, val

    def set(self, index: int, val: int) -> None:
        self.A[index].append([self.snapid, val])

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.A[index]
        # [(-1, 0), (snapid, val), ...]
        j = bisect.bisect(history, [snap_id+1]) - 1 # binary search to find a number less or equal
        return history[j][1]