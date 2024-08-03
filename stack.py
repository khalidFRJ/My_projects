from collections import deque
stack = deque()

class stack:
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)== 0
    
    def size(self):
        return len(self.container)
    
    def show_stack(self):
        return self.container
    

stack1= stack()
stack1.push(100)
stack1.push(200)
stack1.push(300)
stack1.push(400)
print(stack1.show_stack())
print(stack1.peek())
print(stack1.size())
stack1.pop()
print(stack1.show_stack())






