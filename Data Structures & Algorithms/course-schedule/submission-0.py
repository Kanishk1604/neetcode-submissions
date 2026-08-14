class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map course - prereqs
        #we have numcourses -> we want to check if all courses from 0 to numcourses - 1 are visited
        #we havea visited set 
        # we want t oavoid cycles that if a course has a prereq already visited
            #we return false
        #since we do not know where we start from 
        #[[3,1], [1,2], [4,3]]
        #{3:[1], 1:[2], 4:[3], 2 : []}
        # we have a visiting set and a visited set
        #visited set is the one where we visit each key in map
        # visiting set stores courses who do not have any cycles

        visiting = set()
        visited = set()
        courseMap = defaultdict(list)
        for prereq in prerequisites:
            courseMap[prereq[0]].append(prereq[1])
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

            