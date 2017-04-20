'''
Author: Sai Uday Bhaskar Mudivarty
Problem: https://codefights.com/interview/2szSXxzqWuAJKProX/
'''
def sudoku2(grid):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in range(9):
        if not isValidList([grid[i][j] for j in range(9)]) or \
           not isValidList([grid[j][i] for j in range(9)]):
            return False
    for i in range(3):
        for j in range(3):
            if not isValidList([grid[m][n] for n in range(3 * j, 3 * j + 3) \
                                                 for m in range(3 * i, 3 * i + 3)]):
                return False
    return True

def isValidList(xs):
    xs = list(filter(lambda x: x != '.', xs))
    return len(set(xs)) == len(xs)