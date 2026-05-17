class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            m=[0]*26
            for j in i:
                m[ord(j)-ord("a")]+=1
            res[tuple(m)].append(i)
        return res.values()        