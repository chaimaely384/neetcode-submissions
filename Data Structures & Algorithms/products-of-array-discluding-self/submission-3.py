class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        Output=[1]*len(nums)

        #leftproduct
        leftproduct=1
        for i in range(len(nums)):
            Output[i]*= leftproduct
            leftproduct = Output[i]*nums[i]

        #rightproduct
        rightproduct=1

        for i in range(len(nums)-1,-1,-1):
            Output[i]*= rightproduct
            rightproduct*= nums[i]
        
        return Output






