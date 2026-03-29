class Solution:
    # BFS
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return

        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        n, m = len(board), len(board[0])

        def is_valid(x, y):
            return 1 <= x <= n-2 and 1 <= y <= m-2

        def bfs():
            queue = deque()
            visited = set()

            for i in range(n):
                for j in range(m):
                    if (i == 0 or j == 0 or i == n-1 or j == m-1) and \
                        board[i][j] == "O":
                        queue.append((i, j))
                        board[i][j] = "S"

            while queue:
                nx, ny = queue.popleft()
                for dx, dy in dirs:
                    x, y = nx + dx, ny + dy
                    if is_valid(x, y) and board[x][y] == "O":
                        visited.add((x, y))
                        queue.append((x, y))
                        board[x][y] = "S"

        bfs()
        for i in range(n):
            for j in range(m):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                    
        