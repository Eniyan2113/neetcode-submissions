class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):
            nxtdp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nxtdp.add(t + nums[i])
                nxtdp.add(t)
            dp = nxtdp        
        return True if target in dp else False