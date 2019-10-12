

class Stack(object):
    def __init__(self, n):
        self.vals = [0] * n
        self.head = -1
        self.n = n

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.head == (self.n - 1)

    def push(self, val):
        if self.is_full():
            raise ValueError("Stack is full")
        self.head += 1
        self.vals[self.head] = val

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        val = self.vals[self.head]
        self.vals[self.head] = 0
        self.head -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.vals[self.head]

def revstr(string):
    stack = Stack(len(string))
    [stack.push(ch) for ch in string]
    revstrlist = []
    while not stack.is_empty():
        revstrlist.append(stack.pop())
    return ''.join(revstrlist)

def paranChecker(string):
    paran_dict = {
        '(': ')'
    }
    closing_paran = set(paran_dict.values())
    stack = Stack(len(string))
    for c in string:
        if c in paran_dict:
            stack.push(c)
        elif c in closing_paran:
            if stack.is_empty() or c != paran_dict[stack.peek()]:
                return False
            stack.pop()
    return stack.is_empty()

print(paranChecker('((()))'))
print(paranChecker('(()'))





