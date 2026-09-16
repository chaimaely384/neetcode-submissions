class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        H = {}
        l = 0
        out = 0

        for r in range(len(s)):
            H[s[r]] = 1+H.get(s[r], 0)

            if (r-l+1)-max(H.values()) > k :
                H[s[l]] -= 1
                l +=1
            else :
                out = max(out, r-l+1)
        return out

        




        