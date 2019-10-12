def fib(n):

    if n <= 1:
        return n
    last = 0
    lastlast = 1
    for i in range(n):
        curr = last + lastlast
        lastlast, last = last, curr

    return curr

print(fib(9))