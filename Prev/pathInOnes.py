
def inBound(sr, sc, m, n):
    return (0 <= sr < m) and (0 <= sc < n)


def shortestCellPathMemo(grid, sr, sc, tr, tc, m, n, cache):
    if not inBound(sr, sc, m, n) or grid[sr][sc] == 0:
        return float('inf')  # not inBound(sr, sc, m, n) will out of range?
    if cache[sr][sc] is None:
        if sr == tr and sc == tc:
            cache[sr][sc] = 1
        else:
            cache[sr][sc] = min(
                shortestCellPathMemo(grid, sr - 1, sc, tr, tc, m, n, cache),
                shortestCellPathMemo(grid, sr + 1, sc, tr, tc, m, n, cache),
                shortestCellPathMemo(grid, sr, sc - 1, tr, tc, m, n, cache),
                shortestCellPathMemo(grid, sr, sc + 1, tr, tc, m, n, cache))
            if cache[sr][sc] < float('inf'):
                cache[sr][sc] = 1 + res
    return cache[sr][sc]


def shortestCellPath(grid, sr, sc, tr, tc):
    m = len(grid)
    n = len(grid[0])
    cache = [[None for x in range(n)] for y in range(m)]
    #cache[sr][sc] = 0
    return shortestCellPathMemo(grid, sr, sc, tr, tc, m, n, cache)


grid = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print(shortestCellPath(grid, sr, sc, tr, tc))