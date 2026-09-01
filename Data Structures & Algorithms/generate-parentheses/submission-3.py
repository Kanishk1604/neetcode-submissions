class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #closed < open
        # open == n == closed

        subset = []
        res = []

        def dfs(open, closed):
            if open == n == closed:
                res.append("".join(subset))
                return 
            
            if open < n:
                subset.append("(")
                dfs(open + 1, closed)
                subset.pop()
            
            if closed < open:
                subset.append(")")
                dfs(open, closed + 1)
                subset.pop()

        dfs(0, 0)
        return res


    #     []
    #     [(]
    #    [(] []
    # [((] [(]  []
            
    #         [(((]
    #     [((()]
    #     [((())]
    #     [((()))]