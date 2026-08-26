class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for p1, p2 in prerequisites:
            adj[p1].append(p2)

        visiting = set()
        visited = set()

        def dfs(course):
            if not adj[course] or course in visited:
                return True
            if course in visiting:
                return False
                
            visiting.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

            
            
