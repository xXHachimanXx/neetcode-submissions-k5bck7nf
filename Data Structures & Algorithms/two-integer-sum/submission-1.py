class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = {}

        # nums = [3,4,5,6], target = 7

        # dif  = {4: 0, 3: 1, 2: 2, 1: 3}

        for i in range(len(nums)):
            dif[target-nums[i]] = i
        
        for i in range(len(nums)):
            num = nums[i]
            if num in dif and i != dif[num]:
                return [i, dif[num]]

        return []
        