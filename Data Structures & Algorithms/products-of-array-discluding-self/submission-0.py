class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        q=[0]*len(nums)
        prefix=1
        for i in range(len(nums)):
            q[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            q[i]*=postfix
            postfix*=nums[i]
        return q        