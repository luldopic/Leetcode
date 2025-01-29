from solution_check import ProblemSet

def reverseWords(s: str):
    """
    :type s: str
    :rtype: str
    """
    s = s.strip()
    s_list = s.split(" ")
    for word in s_list:
        word = word.strip()
    
    output = ""
    s_list.reverse()
    for word_index in range(0, len(s_list)-1):
        if s_list[word_index] == '':
            continue
        output = output + s_list[word_index].strip() + " "
        
    return output + s_list[-1]
    
    
if __name__ == "__main__":
    testcases = {
        "testcase1": {
            "args": ("the sky is blue",),
            "solution": "blue is sky the"
        },
        "testcase2": {
            "args": ("  hello world  ",),
            "solution": "world hello"
        },
        "testcase3": {
            "args": ("a good   example",),
            "solution": "example good a"
        }
    }
    
    ps = ProblemSet(testcases,reverseWords)
    
    ps.check_solution()