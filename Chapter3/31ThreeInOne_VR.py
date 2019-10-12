class MultiStack(object):
    # Driver Code
    def __init__(self, capacity, k):
        self._array = [0] * capacity
        self.top = [-1] * k
        self.size = [0] * k
        self.capacity = capacity

    def is_full(self, stack_num):
        raise NotImplementedError

    def is_empty(self, sn):
        return self.size[sn] == 0

    def push(self, val, sn):
        raise NotImplementedError

    def pop(self, sn):
        raise NotImplementedError

    def peek(self, sn):
        raise NotImplementedError

class FixedSize3Stack(MultiStack):
    def __init__(self, capacity, k=3):
        if k != 3:
            raise ValueError("K must be three")
        super(FixedSize3Stack, self).__init__(capacity, k)
        self.per_stack_capacity = int(self.capacity/ 3)
        self.top = [i * self.per_stack_capacity for i in range(k)]

    def is_full(self, sn):
        return self.size[sn] == int(self.capacity / 3)

    def push(self, val, sn):
        if self.is_full(sn):
            raise Exception("Stack is full")
        # Increment size
        self.size[sn] += 1
        # Increment top
        self.top[sn] += 1
        # Copy to array at top
        self._array[self.top[sn]] = val

    def pop(self, sn):
        val = self.peek(sn)
        self.size[sn] -= 1
        self.top[sn] -= 1
        return val

    def peek(self, sn):
        if self.is_empty(sn):
            raise Exception("Stack is Empty")
        return self._array[self.top[sn]]


class KStacks(MultiStack):
    def __init__(self, capacity, k=3):
        super(KStacks, self).__init__(capacity, k)
        self.next = [i+1 for i in range(self.capacity)] # THis array stores one linked list per stack and one linked list for free
        self.next[self.capacity - 1] = -1
        self.free_top = 0

    def is_full(self, sn):
        return self.free_top == -1

    def push(self, val, sn):
        if self.is_full(sn):
            raise Exception("Stack is full")
        # Increment size
        self.size[sn] += 1
        # Get current free
        insert_at = self.free_top
        # Set free index to next free
        self.free_top = self.next[self.free_top]
        # Get current free index and set that node to point to current top
        self.next[insert_at] = self.top[sn]
        # Update top to current free
        self.top[sn] = insert_at
        # Copy array value to top
        self._array[self.top[sn]] = val

    def pop(self, sn):
        val = self.peek(sn)
        self.size[sn] -= 1
        # Get releasing node from top
        current_top = self.top[sn]
        # Copy relasing value
        val = self._array[current_top]
        # Update top to top_next
        self.top[sn] = self.next[self.top[sn]]
        # Update next of releasing node to current free top
        self.next[current_top] = self.free_top
        # Update free to free next
        self.free_top = current_top
        return val

    def peek(self, sn):
        if self.is_empty(sn):
            raise Exception("Stack is Empty")
        return self._array[self.top[sn]]


# Driver Code
if __name__ == "__main__":
    #https: // www.geeksforgeeks.org / efficiently - implement - k - stacks - single - array /
    # Create 3 stacks using an
    # array of size 10.
    #kstacks = FixedSize3Stack(10, 3)
    kstacks = KStacks(10, 3)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " +
          str(kstacks.pop(2)))
    print("Popped element from stack 1 is " +
          str(kstacks.pop(1)))
    print("Popped element from stack 0 is " +
          str(kstacks.pop(0)))


"""
Popped element from stack 2 is 45
Popped element from stack 1 is 39
Popped element from stack 0 is 7
"""