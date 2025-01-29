from solution_check import ProblemSet

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
        
if __name__ == "__main__":
    testcases = {
        "testcase1": {
            "args": ([1,7,0,7,-8,None,None],),
            "solution": 2
        },
        "testcase2": {
            "args": ([1,7,0,7,-8,None,None],),
            "solution": 2
        }
    }
    
    ps = ProblemSet(testcases,maxLevelSum)
    
    ps.check_solution()