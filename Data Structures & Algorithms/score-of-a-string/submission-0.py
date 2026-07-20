class Solution:
    def scoreOfString(self, s: str) -> int:
        c = 0
        for i in range (0,len(s)-1):
            if (ord(s[i+1])<ord(s[i])) :
                c+=ord(s[i])-ord(s[i+1])
            else :
                c+=ord(s[i+1])- ord(s[i])
        return c
            
        