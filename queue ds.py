from collections import deque

#a queue class (data structures)
class queue():
    def __init__(self):
        self.queue = deque()
        
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        if len(self.queue)> 0:
            return self.queue.popleft()
        else:
            return None
    def peek(self):
        if len(self.queue) > 0:
            print(self.queue[0])
           # print(self.queue)
        else:
            return None
    
b = queue()        
b.push(5)
b.push(0)
b.push(2)
b.push(8)
b.peek()
b.pop()
b.peek()

