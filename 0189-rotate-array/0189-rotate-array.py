class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        ""
        n=len(nums)
        arr=[0]*len(nums)
        for i in range(0,len(nums)):
            index=(i+k)%n
            arr[index]=nums[i]
        for i in range(len(arr)):
            nums[i]=arr[i]
        return nums        
        