class MinStack:

    def __init__(self):
        self.stack=[]
        self.min =sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min=min(self.min,val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min=sys.maxsize
        for i in self.stack:
            if (i < self.min):
                self.min= i


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()