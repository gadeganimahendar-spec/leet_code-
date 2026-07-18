class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left=0
        sum1=sum(nums)
        for i in range(len(nums)):
            if (left==(sum1-left-nums[i])):
                return i
            left+=nums[i]
        return -1  