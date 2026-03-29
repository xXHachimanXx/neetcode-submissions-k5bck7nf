class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # [1,2,3,4,5,6]
        # min = 4
        #  i    i     j
        # [3,4,5,6,1,2]
        #
        # min = 0
        # [5,0,1,2,3,4]
        #  ij       
        #
        # [4,5,0,1,2,3]
        # min = 0
        #
        #  i j   
        # [4,5,6,7]
        # min = 5

        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r)//2

            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m -1
                
        return res