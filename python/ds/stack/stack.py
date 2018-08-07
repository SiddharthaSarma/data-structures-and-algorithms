class EmptyStackError(Exception):
    """
    """
    pass


class Stack:

    def __init__(self):
        self.list = []
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def push(self, val):
        self.list.append(val)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return EmptyStackError("list is empty")
        self.top -= 1
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return EmptyStackError("Stack is empty")
        return self.list[self.top]

    def size(self):
        return self.top + 1

