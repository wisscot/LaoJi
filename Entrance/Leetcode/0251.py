# 251. Flatten 2D Vector

'''
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.
'''

class Vector2D(object):

    def __init__(self, vec2d):
        self.stack = vec2d[::-1]

    def next(self):
        if self.hasNext():
            return self.stack.pop()
        else:
            return None
        
    def hasNext(self):
        while self.stack and type(self.stack[-1]) == list:
            self.stack += self.stack.pop()[::-1]
            
        if self.stack:
            return True
            
        return False
        
