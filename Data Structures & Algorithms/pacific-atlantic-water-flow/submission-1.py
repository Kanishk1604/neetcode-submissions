class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        atl = set()
        pac = set()

        def dfs(i, j, seen, prev):
            if ( i< 0 or j < 0 or i >= rows or j >= cols or heights[i][j] < prev or (i, j) in seen):
                return 
            
            seen.add((i, j))
            return (dfs(i + 1, j, seen, heights[i][j]) 
            or dfs(i - 1, j, seen, heights[i][j]) 
            or dfs(i, j + 1, seen, heights[i][j]) 
            or dfs(i, j - 1, seen, heights[i][j]))
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
