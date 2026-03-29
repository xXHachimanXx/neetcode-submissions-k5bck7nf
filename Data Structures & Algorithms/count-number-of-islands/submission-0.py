class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        columns, rows = len(grid[0]), len(grid)
        visited = set()
        num_islands = 0

        def bfs(r, c):
            q = []
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.pop()
                for rd, cd in directions:
                    r, c = row + rd, col + cd

                    if (r in range(rows)) and (c in range(columns)) and \
                        (r, c) not in visited and \
                        grid[r][c] == '1':
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(columns):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands

        