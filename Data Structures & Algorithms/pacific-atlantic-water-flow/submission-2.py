class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(i, j, prev, visit):
            if (i <0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prev or (i, j) in visit):
                return 
            visit.add((i, j))
            dfs(i + 1, j, heights[i][j], visit)
            dfs(i - 1, j, heights[i][j], visit)
            dfs(i, j + 1, heights[i][j], visit)
            dfs(i, j - 1, heights[i][j], visit)

        pac = set()
        atl = set()
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols - 1], atl)

        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res