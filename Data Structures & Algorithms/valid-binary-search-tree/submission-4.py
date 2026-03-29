# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        h, l = 100000, -100000
        def isValidBSTAux(root, low, high):
            if not root:
                return True

            if not (low < root.val < high):
                return False
            
            return isValidBSTAux(root.left, low, root.val) and isValidBSTAux(root.right, root.val, high)
            

        return isValidBSTAux(root, l, h)

        