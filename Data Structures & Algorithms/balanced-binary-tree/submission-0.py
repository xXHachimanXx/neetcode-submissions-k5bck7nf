# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return [True, 0]
            
            left_res = height(root.left)
            if left_res[0] == False:
                return [False, -1]

            right_res = height(root.right)
            if right_res[0] == False:
                return [False, -1]

            left_height, right_height = left_res[1], right_res[1]
            if abs(left_height - right_height) > 1:
                return [False, -1]
            
            return [True, max(left_height, right_height)+1]

        return height(root)[0]


        