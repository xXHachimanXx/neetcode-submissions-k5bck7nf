class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, columns = len(grid), len(grid[0])
        res = rows*columns
        fresh_fruits = 0
        queue = deque()

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2: 
                    queue.append((row, column))
                elif grid[row][column] == 1:
                    fresh_fruits += 1

        count = 0
        positions = [[0,1], [1,0], [-1,0], [0,-1]]

        while fresh_fruits > 0 and queue:
            for i in range(len(queue)): # for each source
                r, c = queue.popleft()
                neighbors = set()
                for rp, cp in positions:
                    if r+rp in range(rows) and c+cp in range(columns) and grid[r+rp][c+cp] == 1:
                        neighbors.add((r+rp, c+cp))
                
                for neig in neighbors:
                    queue.append(neig)
                    r, c = neig
                    grid[r][c] = 2
                    fresh_fruits -= 1
            
            count += 1
            
        return count if fresh_fruits == 0 else -1
