class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_set = []

        def aux(i):
            if i >= len(nums):
                res.append(sub_set.copy())
                return
            
            sub_set.append(nums[i])
            aux(i+1)
            sub_set.pop()
            aux(i+1)
        
        aux(0)
        return res
