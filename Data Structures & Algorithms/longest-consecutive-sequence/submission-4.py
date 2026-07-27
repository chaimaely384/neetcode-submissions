class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         
        numsSet =  set(nums)

        longest = 0

        for n in numsSet :
            # Si c est le début d'une séquence ( pas de n-1 qui existe dans le set)
            if (n-1) not in numsSet :
                # On initialise le compte à 0 à chaque fois qu on trouve une nouvelle sequence
                length = 0 
                while (n+length) in numsSet :
                    length+=1
                longest = max(longest,length)
        return longest


        


        
            

                

