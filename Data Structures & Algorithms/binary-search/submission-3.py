class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l<=r :
            m = l+(r-l)//2   # m = (r+l)//2 can lead to overflow (Calculating the midpoint of a very large array causes the integer memory limits to be exceeded)
            if nums[m] > target :
                r = m - 1
            elif nums[m] < target :
                l = m + 1
            else :
                return m
        return -1