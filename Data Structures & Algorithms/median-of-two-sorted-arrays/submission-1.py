class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        half = (len(A)+len(B))//2

        if len(A)>len(B):
            A, B = B, A
        
        l, r = 0, len(A)-1

        while True :
            ma = l+(r-l)//2

            mb = half -ma-2

            Aleft = A[ma] if ma>=0 else float("-infinity")
            Aright = A[ma+1] if ma+1<len(A) else float("infinity")
            Bleft = B[mb] if mb>=0 else float("-infinity")
            Bright = B[mb+1] if mb+1<len(B) else float("infinity")

            if Aleft<=Bright and Bleft<=Aright :
                if (len(A)+len(B))%2 :
                    return min(Aright, Bright)
                else :
                    return (min(Aright, Bright)+max(Aleft, Bleft))/2
            elif Aleft > Bright :
                r = ma-1
            else :
                l = ma+1
      
        
        
          





        