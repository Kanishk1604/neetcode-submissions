class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #pacific - > i < 0 or j < 0
        #atlantic -> i >= m or j > = n
        #both true add cords

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(i, j, visit, prev):
            if (i >= 0 and i < rows and j >= 0 and j < cols and  (i, j) not in visit and heights[i][j] >= prev ):
                val = heights[i][j]
                visit.add((i,j))
                dfs(i + 1, j, visit, val) 
                dfs(i, j + 1, visit, val)
                dfs(i - 1, j, visit, val)
                dfs(i, j - 1, visit, val)
        
        res = []

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

        