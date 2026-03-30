class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list for the courses and prerequisites
        preMap = { i: [] for i in range(numCourses)}
        output = []
        visiting = set()
        visited = set()

        # populate the premap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # dfs
        def dfs(crs):
            # the first base case
            # if we find a cycle
            if crs in visiting:
                return False
            
            # if we have visited a course, return true
            if crs in visited:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            output.append(crs)
            visited.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output

        