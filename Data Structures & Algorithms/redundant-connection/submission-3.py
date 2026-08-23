class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(1, len(edges) + 1)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        cycle = set()
        cycleStart = -1

        visit = set()

        def dfs(node, par):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True
            
            visit.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(nei)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False
        dfs(1, -1)
        for i, j in reversed(edges):
            if i in cycle and j in cycle:
                return [i, j]
        
        return []
