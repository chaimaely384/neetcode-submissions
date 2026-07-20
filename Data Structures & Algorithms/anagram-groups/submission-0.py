class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #out=[]
        #d = defaultdict(list)

        #for n in strs :
            #d[''.join(sorted(n))].append(n)
        
        #for s in d :
            #out.append(d[s])

        #return out




        d = defaultdict(list)

        for s in strs :
            d["".join(sorted(s))].append(s)
        return list(d.values())
        