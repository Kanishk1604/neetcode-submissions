class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dfs on each vertix
        # add them in visit
        #if they are are visit, seeing them again return false
        #after every iteration on each vertix, if dfs on that node returns true
        # increse res 

        adjMap = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return 
            
            visit.add(node)

            for nei in adjMap[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
                
            return
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1
            
        return res