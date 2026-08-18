class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        par = []
        def dfs(open, close):
            nonlocal par
            if open == n and close == n:
                res.append("".join(par))
                return 
            if open < n:
                par.append("(")
                dfs(open + 1, close)
                par.pop()
            if close < open:
                par.append(")")
                dfs(open, close + 1)
                par.pop()
    
        dfs(0, 0)
        return res
            