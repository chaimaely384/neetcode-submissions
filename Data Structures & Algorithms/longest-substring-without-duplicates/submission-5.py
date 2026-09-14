class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        H = {}
        out = 0
        l = 0

        for i in range(len(s)):
            if s[i] in H :
                l = max(H[s[i]]+1, l)
            H[s[i]] = i 
            out = max(out, i-l+1)
        return out   