from solution_check import ProblemSet

def UniquePath(m,n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    grid = [[0 for _ in range(n)] for _ in range(m)]
    
    grid[0][0] = 1
    for m_index in range(m):
        for n_index in range(n):
            if m_index == 0 and n_index == 0:
                continue
            if m_index == 0:
                up = 0
            else:
                up = grid[m_index-1][n_index]
            if n_index == 0:
                left = 0
            else:
                left = grid[m_index][n_index-1]
            grid[m_index][n_index] = up + left
    
    return grid[m-1][n-1]

if __name__ == "__main__":
    testcases = {
        "testcase1": {
            "args": (3,7),
            "solution": 28
        },
        "testcase2": {
            "args": (3,2),
            "solution": 3
        }
    }
    
    ps = ProblemSet(testcases,UniquePath)
    
    ps.check_solution()