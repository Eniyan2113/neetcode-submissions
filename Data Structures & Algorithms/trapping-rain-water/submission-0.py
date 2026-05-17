class Solution:
    def trap(self, height: List[int]) -> int:
        l=0;r=len(height)-1
        res=0
        lm=height[0];rm=height[-1]
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,height[l])
                res+=lm-height[l]
            else:
                r-=1
                rm=max(rm,height[r])    
                res+=rm-height[r]
        return res        