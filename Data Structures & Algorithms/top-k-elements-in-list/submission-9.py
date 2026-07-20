class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #bizzare celle là apparaint plus efficace en soumettant la solution alors que la complexité est O(n + m log m + k·m) avec 
            #n = length of nums

            #m = number of unique elements (size of dictionary)

            #k = number of top frequent elements requested

        #d = defaultdict(int)

        #for i in nums :
        #    d[i]+=1
        #sortd=sorted(d.values(), reverse=True)

        #out=[]

        #for j in range(k):
        #    for key, value in d.items():
        #        if value == sortd[j] and key not in out:
        #            out.append(key)
        #return out


    #solution optimale avec complexité spaciale et temporelle de O(n)    

        bucket = [[] for i in range(len(nums)+1)] 
        # on initialise une liste de listes au nombre des éléments de nums
        # on crée un dictionnaire qui mappe chaque nombre dans nums à son nombre d'occurrence
        # on stocke dans chaque indice de bucket les éléments de nums dont l'occurrence égale à l'indice
        # on parcours les éléments du buket avec une boucle inversée pour obtenir les k elements dont la fréquence d 'apparence est la maximale
        frequency = {}

        out=[]

        for i in nums :
            frequency[i] = 1 + frequency.get(i,0)
        
        for key, value in frequency.items() :
            bucket[value].append(key)
        
        for i in range(len(bucket)-1, 0, -1) :
            for n in bucket[i]:
                out.append(n)
                if len(out)==k:
                    return out        



        