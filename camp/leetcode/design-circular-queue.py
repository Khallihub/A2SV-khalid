class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for i in range(k)]
        self.length = 0
        self.maxSize = k
        self.front = 0
        self.back = 0

    def enQueue(self, value: int) -> bool:
        if self.length == self.maxSize:
            return False
        self.queue[self.back%self.maxSize] = value
        self.back += 1
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.length < 1: return False
        self.queue[self.front%self.maxSize] = None
        self.front += 1
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.length < 1:
            return -1
        return self.queue[self.front%self.maxSize]   

    def Rear(self) -> int:
        if self.length < 1:
            return -1
        return self.queue[self.back%self.maxSize-1]   
        

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.maxSize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()