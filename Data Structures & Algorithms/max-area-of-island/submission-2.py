class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        
        max_area = 0
        rows, columns = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                row, col = q.popleft()

                for rd, cd in directions:
                    r, c = row + rd, col + cd

                    if (r in range(rows)) and (c in range(columns)) and \
                        (r, c) not in visited and grid[r][c] == 1:
                        q.append((r, c))
                        visited.add((r, c))
                        
                        print((r,c))
                        area += 1
            return area

        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area


        