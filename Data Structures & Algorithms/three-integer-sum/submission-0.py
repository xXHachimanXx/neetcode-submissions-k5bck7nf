class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        tri = sorted([nums[i], nums[j], nums[k]])
                        res.add(tuple(tri))
                  
        return [list(el) for el in res]
                    
        