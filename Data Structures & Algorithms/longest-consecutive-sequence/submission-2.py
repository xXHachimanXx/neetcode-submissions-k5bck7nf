class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #       [2,20,4,10,3,4,5]
        # map = [1,19,3,9,2,3,4]

        # [10, 20, 30, 31, ]
        # 9, 19, 29, 30

        if not nums or len(nums) == 0:
            return 0

        num_set = set(nums)

        longest = 1
        for n in num_set:
            # find the first number of the sequece
            if n-1 not in num_set:
                length = 0
                while (n + length) in num_set: # get the nexts nuumbers of the sequence
                    length += 1
                longest = max(longest, length)

        return longest
            