class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''

        if I have cycle

        how can I find the root in this case?
        5 -> 4 -> 3 -> 0
             v    v    
             2 -> 1
        '''

        graph = {}

        for pr in prerequisites:
            if pr[0] not in graph:
                graph[pr[0]] = []
            graph[pr[0]].append(pr[1])

        def dfs(root, visited):
            if root in visited:
                return True
            
            if root not in graph:
                return False
            
            visited.add(root)

            for neigh in graph[root]:
                if dfs(neigh, visited):
                    return True
            
            visited.remove(root)
            graph[root] = []
            
            return False
            
        visited = set()
        for i in range(numCourses):
            if dfs(i, visited):
                return False
            
        return True