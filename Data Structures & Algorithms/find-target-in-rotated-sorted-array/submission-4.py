class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Let's take this as an example : [3,4,5,0,1,2]
        
        l, r = 0, len(nums)-1

        while l<=r :
            m = l + (r-l)//2  # in the case of the example m=5
            if target == nums[m]:
                    return m
            if nums[m]>= nums[l] :  # we are in the left sorted portion
                if target > nums[m] or target < nums[l] :
                    l = m+1
                else :
                    r = m-1
            else : # right sorted portion
                
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else :
                    l = m+1
        return -1


