class MinStack:

    def __init__(self):
        self.stack1 = []
        self.minStack = []
        
        
    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.stack1.append(val)
            self.minStack.append(val)

        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
                self.stack1.append(val)

            else:
                self.minStack.append(self.minStack[-1])
                self.stack1.append(val)

    def pop(self) -> None:
        self.stack1.pop()
        self.minStack.pop()

    def top(self) -> int:
        if len(self.stack1) > 0:
            return self.stack1[-1]

    def getMin(self) -> int:
        if len(self.stack1) > 0:
            return self.minStack[-1]
    
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
