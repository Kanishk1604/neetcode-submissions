class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1 :
            return False
        
        visit = set()

        adjMap = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adjMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n 