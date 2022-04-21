
class MinStack(object):
    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, n: int):
        self.data.append(n)
        if not self.min_stack or n <= self.min_stack[-1]:
            self.min_stack.append(n)

    def pop(self):
        if not self.data:
            return -1
        n = self.data.pop(-1)
        if n == self.min_stack[-1]:
            self.min_stack.pop(-1)
        return n

    def top(self) -> int:
        return self.data[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]
