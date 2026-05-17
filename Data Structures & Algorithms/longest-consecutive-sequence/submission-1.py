class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=0
        for i in nums:
            q=i;n=1
            while q in nums:
                if q+1 in nums:
                    q+=1
                    n+=1
                else:
                    break    
            m=max(m,n)   
        return m         