class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting, visited = set(), set()
        courseMap = defaultdict(list)

        for pre in prerequisites:
            courseMap[pre[0]].append(pre[1])
        res = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for pre in courseMap[course]:
                if not dfs(pre):
                    return False
            
            res.append(course)
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res