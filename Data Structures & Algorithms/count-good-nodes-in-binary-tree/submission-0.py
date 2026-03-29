# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
        2
     4    1
  3     1   5
    4    

'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def auxGoodNodes(root, maxVal):
            if not root:
                return 0

            count = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            
            count += auxGoodNodes(root.left, maxVal)
            count += auxGoodNodes(root.right, maxVal)

            return count

        return auxGoodNodes(root, root.val)
        