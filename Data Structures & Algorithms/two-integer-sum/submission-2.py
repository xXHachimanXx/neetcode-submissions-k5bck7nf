class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        # (6:0, 5:1, 4:2, 3:3)
        # [6, 5, 4, 4] -> 7


        #  {5: 0, 5: 1}
        # [5, 5]
        # 
        # [2,3]

        hash_nums = {}
        for i, num in enumerate(nums):
            hash_nums[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff in hash_nums and hash_nums[diff] != i:
                return [i, hash_nums[diff]]
            
        return []


        