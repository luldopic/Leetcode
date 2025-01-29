from solution_check import ProblemSet

def ClimbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    
    if n <= 2:
        return n
    
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

if __name__ == "__main__":
    testcases = {
        "testcase1": {
            "args": (2,),
            "solution": 2
        },
        "testcase2": {
            "args": (3,),
            "solution": 3
        }
    }
    
    ps = ProblemSet(testcases,ClimbStairs)
    
    ps.check_solution()