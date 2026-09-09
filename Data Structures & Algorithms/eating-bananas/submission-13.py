class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        kmin = r

        while l<=r :
            k = l + (r-l)//2
            time = 0
            for x in piles:
                time += math.ceil(x/k)
            if time<=h :
                kmin=min(kmin, k)
                r = k-1
            else :
                l = k+1

        return kmin




