class MyQueue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        for i in range (len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        a = self.stack2[-1]
        self.stack2.pop()
        for i in range (len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return a

    def peek(self) -> int:
        print(self.stack1,self.stack2)
        for i in range (len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        a = self.stack2[-1]
        for i in range (len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return a
    def empty(self) -> bool:
        return len(self.stack1) == 0
