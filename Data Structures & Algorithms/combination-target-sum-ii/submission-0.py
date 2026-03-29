class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub_set = []
        candidates.sort()

        def aux(i, curr):
            if curr == target:
                res.append(sub_set.copy())
                return
            if i == len(candidates) or curr > target:
                return
            
            # choice number
            sub_set.append(candidates[i])
            aux(i+1, curr + candidates[i])

            # not choice number
            # skip equals numbers to not choice it
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            sub_set.pop()
            aux(i+1, curr)

        aux(0, 0)
        return res