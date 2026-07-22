class Solution:

    def encode(self, strs: List[str]) -> str:

        res=""
        for n in strs :
            res+= str(len(n))+"#"+n
        return res

    def decode(self, s: str) -> List[str]:

        decodedlist=[]

        i=0
        while i<len(s) :
            j=i
            while s[j] !='#':
                j+=1
            length= int(s[i:j])
            j+=1
            decodedlist.append(s[j:j+length])
            i=j+length
        return decodedlist




