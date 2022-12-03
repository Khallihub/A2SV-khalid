class MyCircularDeque:

    def __init__(self, k: int):
        self.lst = [None]*k
        self.currentSize = 0
        self.maxSize = k        
        self.front = 0
        self.back = 0
    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.lst[self.front] = value
            self.currentSize += 1
            return True
        elif not self.isFull():
            self.front = (self.front - 1)%self.maxSize
            self.lst[self.front] = value
            self.currentSize += 1
            return True
        else: 
            return False 

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.lst[self.back] = value
            self.currentSize += 1
            return True
        elif not self.isFull():
            self.back = (self.back + 1)%self.maxSize
            self.lst[self.back] = value
            self.currentSize += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.lst[self.front] = None
            if self.currentSize != 1:
                self.front = (self.front + 1 ) % self.maxSize
            self.currentSize -= 1
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.lst[self.back] = None
            if self.currentSize != 1:
                self.back = (self.back-1)%self.maxSize
            self.currentSize -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.lst[self.front]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.lst[self.back]
        return -1

    def isEmpty(self) -> bool:
        return self.currentSize == 0

    def isFull(self) -> bool:
        return self.currentSize == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
