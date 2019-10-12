## 3.3 Stack of Plates
from collections import deque
import unittest

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

class DStack(Stack):
    def __init__(self, capacity):
        super(DStack, self).__init__(capacity)
        self._array = deque()

    def popleft(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        return self._array.popleft()

class SetOfStacks(object):

    def __init__(self, capacity_per):
        self.stacks = [DStack(capacity_per)]
        self.capacity_per = capacity_per
        self.curr_stack = 0
        self.top = -1

    def is_curr_full(self):
        return self.stacks[self.curr_stack].is_full()

    def is_curr_empty(self):
        return self.stacks[self.curr_stack].is_empty()

    def push(self, val):
        if self.is_curr_full():
            self.curr_stack += 1
            if len(self.stacks) == self.curr_stack:
                self.stacks.append(DStack(self.capacity_per))
        self.stacks[self.curr_stack].push(val)

    def pop(self):
        self.peek()
        return self.stacks[self.curr_stack].pop()

    def peek(self):
        if self.is_curr_empty():
            if self.curr_stack == 0:
                raise Exception("Stack is Empty")
            self.curr_stack -= 1
        return self.stacks[self.curr_stack].peek()

    # def pop_at(self, stack_num):
    #     if self.stacks[stack_num].is_empty() or stack_num > self.curr_stack:
    #         raise Exception('Specified stack is empty')
    #     val = self.stacks[stack_num].pop()
    #     self.left_shift(stack_num)
    #     return val
    #
    # def left_shift(self, stack_num):
    #     for i in range(stack_num, self.curr_stack):
    #         # peek at next stack and


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))

    # @unittest.skip('')
    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        self.assertEqual(lst, list(range(4, 35)))

if __name__ == '__main__':
    unittest.main()
