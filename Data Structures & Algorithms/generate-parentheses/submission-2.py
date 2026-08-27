class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(open, closed):
            if open == n == closed:
                res.append("".join(stack))
                return 
            
            if open < n:
                stack.append("(")
                dfs(open + 1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                dfs(open, closed + 1)
                stack.pop()
        
        dfs(0, 0)
        return res