class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        concat=[]

        for n in s :
            if 48 <= ord(n) <= 57 or 65 <= ord(n) <= 90 or 97 <= ord(n) <= 122:
                concat.append(n.lower())
            else :
                continue
        l = len(concat)//2
        for i in range (l):
            if concat[i]!=concat[len(concat)-i-1]:
                return False
        return True
