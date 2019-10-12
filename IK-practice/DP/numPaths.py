
def numberOfPaths(row, col):
    cache = [[0 for y in range(col)] for x in range(row)]
    for x in range(row-1):
        cache[x][0] = 1
    for y in range(col-1):
        cache[0][y] = 1
    for x in range(1, row):
        for y in range(1, col):
            cache[x][y] = cache[x-1][y] + cache[x][y-1]
    return cache[row-1][col-1]


print(numberOfPaths(3, 3))
