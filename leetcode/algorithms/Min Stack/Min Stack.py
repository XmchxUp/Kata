class MinStack:
    def __init__(self):
        self.min_st = []
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not len(self.min_st) or val <= self.getMin():
            self.min_st.append(val)

    def pop(self) -> None:
        val = self.st[-1]
        self.st.pop()
        if val == self.getMin():
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
