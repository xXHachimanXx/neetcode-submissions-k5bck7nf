class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub_set = []

        def aux(i, curr):
            if curr == 0:
                res.append(sub_set.copy())
                return
            if i >= len(nums) or curr < 0:
                return
            
            sub_set.append(nums[i])
            aux(i, curr - nums[i])
            sub_set.pop()
            aux(i+1, curr)

        aux(0, target)
        return res