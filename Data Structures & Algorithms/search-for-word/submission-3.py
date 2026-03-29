class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board) , len(board[0])
        roots = []
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    roots.append((i, j))
        
        def dfs(subword, node):
            if subword == word:
                return True

            if len(subword) > len(word):
                return False

            # find neighbors
            directions = [[0,1], [1,0], [0,-1], [-1, 0]]
            neighbors = []
            node_row, node_col = node
            for rd, cd in directions:
                neighbors.append((rd+node_row, cd+node_col))

            # iterate in neighbors
            res = False
            for nei in neighbors:
                nei_r, nei_c = nei

                if nei not in visited and nei_r in range(rows) and nei_c in range(columns) and not res:
                    nei_letter = board[nei_r][nei_c]
                    visited.add(nei)
                    res = dfs(subword + nei_letter, nei)
                    visited.remove(nei)

            return res
        
        exists = False
        visited = set()
        for root in roots:
            if not exists:
                visited.add(root)
                exists = dfs(word[0], root)
                visited.remove(root)
        
        return exists

            
