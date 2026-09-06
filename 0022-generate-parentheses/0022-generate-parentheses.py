class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base case: If the current string reaches the maximum length allowed
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Rule 1: We can always add an opening parenthesis if we haven't used all 'n' of them
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Rule 2: We can only add a closing parenthesis if it matches an unmatched opening one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
        
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
