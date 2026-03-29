class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        quarter_count = defaultdict(set)

        for i in range(len(board)):
            count = set()
            for j in range(len(board[i])):
                num = board[i][j]

                if num == '.':
                    continue
                    
                quarter_index = (i // 3) * 3 + (j // 3)

                if num in rows[i] or num in columns[j] or num in quarter_count[quarter_index]:
                    return False
                
                rows[i].add(num)
                columns[j].add(num)
                quarter_count[quarter_index].add(num)

        return True
        
        
        
