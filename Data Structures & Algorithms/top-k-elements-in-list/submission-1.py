class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = defaultdict(int)

        for i in nums :
            d[i]+=1
        sortd=sorted(d.values(), reverse=True)

        out=[]

        for j in range(k):
            for key, value in d.items():
                if value == sortd[j] and key not in out:
                    out.append(key)
        return out 


        