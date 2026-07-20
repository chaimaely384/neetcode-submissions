class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hm = {}

        for i, n in enumerate(nums) :
            diff = target - nums[i]
            if diff in Hm :
                return [Hm[diff], i]
            else :
                Hm[n]=i
        return []


            


        
        