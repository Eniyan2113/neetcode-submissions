class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for n in nums:
            nextdp = defaultdict(int)
            for i,j in dp.items():
                nextdp[i + n] += j
                nextdp[i - n] += j
            dp = nextdp
        return dp[target]        