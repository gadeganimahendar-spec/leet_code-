class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # left=[0]*len(nums)
        # pref=1
        # for i in range(0,len(nums)):
        #     left[i]=pref
        #     pref*=nums[i]
        # right=[0]*len(nums)
        # suf=1
        # for i in range(len(nums)-1,-1,-1):
        #     right[i]=suf
        #     suf*=nums[i]
        # res=[0]*len(nums)
        # for i in range(0,len(nums)):
        #     res[i]=left[i]*right[i]
        # return res
        left=[0]*len(nums)
        pre=1
        for i in range(0,len(nums)):
            left[i]=pre
            pre*=nums[i]
        suf=1
        for i in range(len(nums)-1,-1,-1):
            left[i]=left[i]*suf
            suf*=nums[i]
        return left         


        