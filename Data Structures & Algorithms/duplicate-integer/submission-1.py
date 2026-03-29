class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1 2 3 3]
        # (1, 2, 3) -> O(n)

        nums_set = set()

        for el in nums:
            if el in nums_set:
                return True
            
            nums_set.add(el)

        return False


        