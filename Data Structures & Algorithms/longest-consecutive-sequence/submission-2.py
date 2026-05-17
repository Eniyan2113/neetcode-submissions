class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for i in numSet:
            length=0
            while (i+length) in nums:
                length+=1
            longest=max(longest,length)
        return longest        