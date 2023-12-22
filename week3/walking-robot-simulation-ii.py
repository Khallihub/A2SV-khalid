class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0,0]
        self.dir = "East"

    def step(self, num: int) -> None:
        cycle = (self.width-1)*2 + (self.height-1)*2
        if num > cycle:
            num = num % cycle
        if num == 0:
            if self.dir == "East" and self.pos[0] == 0:
                self.dir = "South"
            elif self.dir == "North" and self.pos[0] == self.width - 1 and self.pos[1] == 0:
                self.dir = "East"
            elif self.dir == "West" and self.pos[0] == self.width - 1 and self.pos[1] == self.height - 1:
                self.dir == "North"
            elif self.dir == "South" and self.pos[1] == self.height - 1 and self.pos[0] == 0: 
                self.dir == "West"

        while num > 0:
            if self.dir == "East":
                if self.pos[0] < self.width - 1:
                    stepsLeft = self.width-1 - self.pos[0]
                    self.pos[0]  += min(stepsLeft, num)
                    num -= min(stepsLeft, num)                    
                    if num == 0:
                        break
                elif self.pos[0] == self.width-1:
                        self.dir = "North"
            elif self.dir == "West":
                if self.pos[0] > 0:
                    stepsLeft = self.pos[0]
                    self.pos[0] -= min(stepsLeft, num)
                    num -= min(stepsLeft, num)
                    if num == 0:
                        break
                elif self.pos[0] == 0:
                    self.dir = "South"
            elif self.dir == "North":
                if self.pos[1] < self.height - 1:
                    stepsLeft = self.height - 1 - self.pos[1]
                    self.pos[1]  += min(stepsLeft, num)
                    num -= min(stepsLeft, num)                    
                    if num == 0:
                        break
                elif self.pos[1] == self.height-1:
                        self.dir = "West"
            elif self.dir == "South": 
                if self.pos[1] > 0:
                    stepsLeft = self.pos[1]
                    self.pos[1] -= min(stepsLeft, num)
                    num -= min(stepsLeft, num)
                    if num == 0:
                        break
                elif self.pos[1] == 0:
                    self.dir = "East"
        
    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()