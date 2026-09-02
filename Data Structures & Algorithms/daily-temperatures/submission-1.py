class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        l = len(temperatures)
        out = [0]*l

        for i in range (l-2, -1, -1) :
            j = i + 1
            while j < l and temperatures[j]<= temperatures[i] :
                if out[j] == 0 :
                    j = l
                    break
                else :
                    j += out[j]
            if j < l :
                out[i] = j -i
        return out
