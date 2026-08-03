class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)

        i, j = 0, n-1

        resultat = 0

        while i<j :
            area = (j-i)*min(heights[i], heights[j])
            resultat = max(resultat, area)
            if heights[i]<=heights[j] :
                i+=1
            else :
                j-=1
        return resultat
        
        