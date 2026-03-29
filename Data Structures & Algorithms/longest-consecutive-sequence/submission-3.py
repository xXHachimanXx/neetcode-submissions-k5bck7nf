class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #       [2,20,4,10,3,4,5]
        # map = [1,19,3,9,2,3,4]

        # [10, 20, 30, 31, ]
        # 9, 19, 29, 30

        if not nums or len(nums) == 0:
            return 0

        num_set = set(nums)
        res = 0
        for num in num_set:
            if (num-1) not in num_set: # if it is the first num of the sequence
                length = 0
                while (num + length) in num_set:
                    length += 1
                res = max(res, length)

        return res

            