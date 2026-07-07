class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       l=len(nums)
       l2=len(set(nums))
       if l==l2:
        return False
       else:
        return True
            
                


        