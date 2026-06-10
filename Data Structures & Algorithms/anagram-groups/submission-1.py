class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for word in strs:
            s = "".join(sorted(word))
            m[s].append(word)
        res = []
        for v in m.values():
            res.append(v)
        return res
    