
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        heights = [
            [4,2,7,3,4],
            [7,4,6,4,7],
            [6,3,5,3,6]
        ]

        heights = []
        res = []

        heights = [[1, 2]]
        res = [[0,0], [0,1]]

        heights = [[1],[2],[3]]
        res = [[0,0], [0,1]]

        pacific ->  column = -1, row = -1
        atlantic -> column = n,  row = n

        for each position, scan all paths and test if can touch pacific and atlantic ocean
        """

        if not heights or not heights[0]:
            return []

        res = []
        rows, columns = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def bfs(node, visited, prev_height):
            r, c = node
            if(
                node in visited or 
                r < 0 or c < 0 or r >= rows or c >= columns or
                heights[r][c] < prev_height
                ):
                return
            
            visited.add(node)
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            for dr, dc in directions:
                neigh = (r+dr, c+dc)
                bfs(neigh, visited, heights[r][c])
            
        # starting from pacific
        for row in range(rows):
            bfs((row, 0), pacific, heights[row][0])
        for col in range(columns):
            bfs((0, col), pacific, heights[0][col])

        # starting from atlantic
        for row in range(rows):
            bfs((row, columns-1), atlantic, heights[row][columns-1])
        for col in range(columns):
            bfs((rows-1, col), atlantic, heights[rows-1][col])
        
        for i in range(rows):
            for j in range(columns):
                if (i, j) in pacific and (i,j) in atlantic:
                    res.append([i, j])

        return res



        