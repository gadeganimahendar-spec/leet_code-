class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range (len(nums)):
            left=len(set (nums[:i+1]))
            right=len(set(nums[i+1:]))
            r.append(left-right)
        return r    


        