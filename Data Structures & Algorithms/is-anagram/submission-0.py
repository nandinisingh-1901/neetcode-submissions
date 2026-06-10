class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countingInS = {}
        countingInT = {}

        for i in range(len(s)):
            countingInS[s[i]] = 1 + countingInS.get(s[i],0)
            countingInT[t[i]] = 1 + countingInT.get(t[i],0)

        for cnt in countingInS:
            if countingInS[cnt] != countingInT.get(cnt,0):
                return False
        
        return True