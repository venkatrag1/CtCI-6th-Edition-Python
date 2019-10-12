"""
11:10

go to every position and if matches start - start a recursion to match in each of four directions
with one char less;
base case - if len becomes 0 ; return True; if doesn't match return False
"""

def inBound(x, y, nrow, ncol):
    return 0 <= x < nrow and 0 <= y < ncol

def checkMatchRec(grid, word, ind, x, y, nrow, ncol, visited):
    if ind == -1:
        return True
    if inBound(x, y, nrow, ncol) and word[ind] == grid[x][y] and \
            visited[x][y] == False:
        visited[x][y] = True
        ind -= 1
        res = checkMatchRec(grid, word, ind, x-1, y, nrow, ncol, visited) or \
            checkMatchRec(grid, word, ind, x+1, y, nrow, ncol, visited) or \
            checkMatchRec(grid, word, ind, x, y-1, nrow, ncol, visited) or \
            checkMatchRec(grid, word, ind, x, y+1, nrow, ncol, visited)
        visited[x][y] = False
        return res
    else:
        return False



def checkMatch(grid, word, nrow, ncol):
    for x in range(nrow):
        for y in range(ncol):
            visited = [[False for col in range(ncol)] for row in range(nrow)]
            if checkMatchRec(grid, word, len(word) - 1, x, y, nrow, ncol, visited):
                return True
    return False

# Driver Code
if __name__ == "__main__" :

    grid = ["axmy",
            "bgdf",
            "xeet",
            "raks"]

    # Function to check if word
    # exists or not
    r, c = 4, 4
    # if (checkMatch(grid, "geeks", r, c)) :
    #     print("Yes")
    # else :
    #     print("No")

    grid = ["abcd",
            "eafg",
            "hijk"]
    r, c = 3, 4
    assert checkMatch(grid, "abc", r, c) == True
    assert checkMatch(grid, "aba", r, c) == True
    assert checkMatch(grid, "fcb", r, c) == True
    assert checkMatch(grid, "fgf", r, c) == False
    assert checkMatch(grid, "hik", r, c) == False