class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjMap = {i: [] for i in range(1, len(edges) + 1)}

        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        visit = set()
        cycle = set()
        cycleStart = -1
        def dfs(node, parent):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True
            visit.add(node)

            for nei in adjMap[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                          cycleStart = -1
                    return True

            return False
        
        dfs(1, 0)

        for i in range(len(edges) - 1, 0, -1):
            if edges[i][0]  in cycle and edges[i][1] in cycle: 
                return edges[i]

        return []