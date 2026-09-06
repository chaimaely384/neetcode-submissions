class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        maxArea = 0
        stack = []

        for i in range (n+1) :

            while stack and (i == n or heights[i]<=heights[stack[-1]]) :
                h = heights[stack.pop()]
                if stack :
                    width = i - stack[-1] - 1
                else :
                    width = i
                maxArea = max(maxArea, h * width)
            stack.append(i)
        return maxArea                                 