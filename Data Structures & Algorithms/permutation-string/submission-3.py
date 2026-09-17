class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        count1 = [0]*26

        for x in s1 :
            count1[ord(x)-ord("a")] += 1
 
        l = 0

        while l+len(s1)-1<len(s2):
            count2 = [0]*26
            #matches = 0
            for i in range (l, l+len(s1)):
                count2[ord(s2[i])-ord("a")] += 1
            if count2 == count1 :
                return True
            else :
                l+=1
        return False


        
                

        

        
