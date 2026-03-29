class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = -1

        for i in range(n):

            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i-idx))
                start = idx
            
            stack.append((start, heights[i]))
        
        for i, h in stack:
            max_area = max(max_area, h * (n - i))
        
        return max_area

