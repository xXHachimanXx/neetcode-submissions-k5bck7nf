class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        rows, columns = len(grid), len(grid[0])
        INF = 2147483647 
        visited = set()
        q = deque()

        def visitCell(r, c):
            if (min(r, c) < 0 or r == rows or c == columns or
                (r, c) in visited or grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                visitCell(r + 1, c)
                visitCell(r - 1, c)
                visitCell(r, c + 1)
                visitCell(r, c - 1)
            dist += 1





        