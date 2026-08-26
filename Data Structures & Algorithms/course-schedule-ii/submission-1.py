class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = {i: [] for i in range(numCourses)}

        for p1, p2 in prerequisites:
            adj[p1].append(p2)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res