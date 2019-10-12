class Stack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._array = []

    def is_full(self):
        return len(self._array) == self.capacity

    def is_empty(self):
        return len(self._array) == 0

    def push(self, val):
        if self.is_full():
            raise Exception("Stack full")
        self._array.append(val)

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        return self._array[-1]

    def pop(self):
        self.peek() # For Empty check
        return self._array.pop()


class MinStack(Stack):
    def __init__(self, capacity):
        super(MinStack, self).__init__(capacity)
        self.minstack = Stack(self.capacity)

    def push(self, val):
        if self.is_empty() or val <= self.minstack.peek():
            self.minstack.push(val)
        super(MinStack, self).push(val)

    def pop(self):
        val = super(MinStack, self).pop()
        if val == self.minstack.peek():
            self.minstack.pop()
        return val

    def getMin(self):
        return self.minstack.peek()



if __name__ == '__main__':
    s = MinStack(5)
    s.push(3)
    s.push(5)
    print(s.getMin())
    s.push(2)
    s.push(1)
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    s.peek()

    """
Number Inserted: 3
Number Inserted: 5
Minimum Element in the stack is: 3
Number Inserted: 2
Number Inserted: 1
Minimum Element in the stack is: 1
Top Most Element Removed: 1
Minimum Element in the stack is: 2
Top Most Element Removed: 2
Top Most Element is: 5
    """