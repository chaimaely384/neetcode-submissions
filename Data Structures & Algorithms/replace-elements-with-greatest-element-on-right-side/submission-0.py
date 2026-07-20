class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ar1 = []
        ar2 = []
        for i in range (len(arr)-1) :
            ar1 = arr[i+1::]
            ar1.sort()
            ar2.append(ar1[len(ar1)-1])
        ar2.append(-1)
        return ar2
