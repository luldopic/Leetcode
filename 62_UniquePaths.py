from solution_check import ProblemSet

def UniquePath(m,n):
    pass

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