class Solution:
    def trap(self, height: List[int]) -> int:
       
        n = len(height)
        res = 0

        for i in range(n):
            l, r = i-1, i+1
            max_left, max_right = height[i], height[i]

            while l >= 0:
                max_left = max(max_left, height[l])
                l -= 1

            while r < n:
                max_right = max(max_right, height[r])
                r += 1

            res += min(max_left, max_right) - height[i]

        
        return res
            
            