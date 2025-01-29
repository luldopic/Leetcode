from solution_check import ProblemSet

def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1 = list(word1)
        word2 = list(word2)
        word_order = [word1,word2]
        
        flip_bit = 0
        output=[]
        while len(word_order[0])>0 and len(word_order[1])>0:
            output.append(word_order[flip_bit].pop(0))
            flip_bit = 1 if flip_bit == 0 else 0
        
        if len(word_order[0])>0:
            output.extend(word_order[0])
        
        if len(word_order[1])>0:
            output.extend(word_order[1])
    
        return str("".join(output))

if __name__ == "__main__":
    testcases = {
        "testcase1": {
            "args": ("abc","pqr"),
            "solution": "apbqcr"
        },
        "testcase2": {
            "args": ("ab","pqrs"),
            "solution": "apbqrs"
        },
        "testcase3": {
            "args": ("abcd","pq"),
            "solution": "apbqcd"
        }
    }
    
    ps = ProblemSet(testcases,mergeAlternately)
    
    ps.check_solution()