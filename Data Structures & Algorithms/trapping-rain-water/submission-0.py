class Solution:
    def trap(self, height: List[int]) -> int:

        result = 0

        i, j = 0, len(height)-1

        maxl, maxr = height[i], height[j]

        while i<j :
            if maxl < maxr :
                i+= 1
                maxl= max(maxl, height[i])
                result+= maxl - height[i]

            else :
                j-= 1
                maxr = max(maxr, height[j])
                result+= maxr - height[j]
        return result
            


