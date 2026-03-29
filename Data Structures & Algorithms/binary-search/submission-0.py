class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = -1

        def binary_search(i, j):
            
            if i > j:
                return -1

            mid = i + (j-i)//2

            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                return binary_search(mid+1, j)
            
            return binary_search(i, mid-1)
            
        
        return binary_search(0, n-1)

