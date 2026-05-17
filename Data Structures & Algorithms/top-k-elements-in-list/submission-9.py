class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for i in nums:
            s[i]=1+s.get(i,0)
        heap=[]
        for i in s.keys():
            heapq.heappush(heap,(s[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res                