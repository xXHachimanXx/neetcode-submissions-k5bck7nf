class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return false

        lines   = len(matrix) 
        columns = len(matrix[0])

        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        #             
        # find mid line
        # find mid column
        # test if mid[line][column] == target
        # else test if is < or >
        # pass line and column limits 

        def find_the_line(top, bottom):
            line_mid = (top + bottom)//2

            if top > bottom:
                return -1

            if target > matrix[line_mid][-1]:
                return find_the_line(line_mid+1, bottom)
            
            if target < matrix[line_mid][0]:
                return find_the_line(top, line_mid-1)
            
            return line_mid

            
        def binary_search(left, right):
            mid = (left + right)//2

            if left > right:
                return False
            
            if target == matrix[line][mid]:
                return True
            
            if target > matrix[line][mid]:
                return binary_search(mid+1, right)
            
            return binary_search(left, mid-1)
            
        line = find_the_line(0, lines-1)
        if line < 0:
            return False

        return binary_search(0, columns-1)
            



        