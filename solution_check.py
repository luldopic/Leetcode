class ProblemSet:
    def __init__(self, testcase_dict, solution_func):
        """
        :type testcase_dict: dict
        :type solution_func: function
        """
        self.testcase_dict = testcase_dict
        self.solution_func = solution_func

    def parse_args(self, args):
        """
        Parse the args to adapt to the function's expected input format.

        :param args: The input arguments from the testcase.
        :return: A tuple of arguments to unpack (*args).
        """
        # Single argument as a single value
        if not isinstance(args, (list, tuple)):
            return (args,)
        # Single argument as a list
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            return (args[0],)
        # Multiple arguments as single values
        else:
            return tuple(args)

    def check_case(self, testcase_id):
        """
        Check the solution for a given testcase ID.

        :param testcase_id: str
        :return: dict (contains status and details)
        """
        if testcase_id not in self.testcase_dict:
            return {
                "status": "error",
                "message": f"Testcase ID '{testcase_id}' does not exist."
            }

        testcase = self.testcase_dict[testcase_id]
        args = testcase.get("args")
        expected_solution = testcase.get("solution")

        # Parse the arguments to the correct format
        parsed_args = self.parse_args(args)

        try:
            # Execute the solution function with the parsed arguments
            actual_solution = self.solution_func(*parsed_args)
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error executing the solution: {e}",
                "args": args
            }

        # Compare actual vs expected
        if actual_solution == expected_solution:
            return {
                "status": "success",
                "message": "Solution is correct.",
                "expected": expected_solution,
                "actual": actual_solution
            }
        else:
            return {
                "status": "failure",
                "message": "Solution is incorrect.",
                "expected": expected_solution,
                "actual": actual_solution
            }

    def check_solution(self):
        """
        Check the solutions for all test cases and print the results.
        """
        summary = {"success": 0, "failure": 0, "error": 0}
        results = {}

        for testcase_id in self.testcase_dict:
            result = self.check_case(testcase_id)
            results[testcase_id] = result
            summary[result["status"]] += 1

        # Print summary
        total = sum(summary.values())
        print(f"Summary: {summary['success']} passed, {summary['failure']} failed, {summary['error']} errors out of {total} test cases.")

        # Print details of each test case
        for testcase_id, result in results.items():
            print(f"Testcase '{testcase_id}': {result}")
