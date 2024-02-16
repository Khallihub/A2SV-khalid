class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.val = data
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = Node(homepage)
        self.cur = newNode
        self.curIdx = 1
        self.size = 1


    def visit(self, url: str) -> None:
        newNode = Node(url, None, self.cur)
        cnt = -1
        tmp = self.cur
        while tmp:
            tmp = tmp.next
            cnt += 1
        self.cur.next = newNode
        self.cur = newNode
        self.size = self.size - cnt + 1
        self.curIdx = self.size


    def back(self, steps: int) -> str:
        tmp = self.cur
        while steps > 0 and tmp.prev:
            tmp = tmp.prev
            steps -= 1
            self.curIdx -= 1
        self.cur = tmp
        return tmp.val

    def forward(self, steps: int) -> str:
        tmp = self.cur
        while tmp.next and steps > 0:
            tmp = tmp.next
            steps -= 1
            self.curIdx += 1
        self.cur = tmp
        return tmp.val
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)