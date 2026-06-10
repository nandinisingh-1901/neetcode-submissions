class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # mapS[s[i]] += 1 
        ##this error is happening because you’re trying to increment a key that doesn’t exist yet in the dictionary.
        ##KeyError: 'r' getting this error
        # mapT[t[i]] += 1 
        mapS = {}
        mapT = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i],0) + 1
            mapT[t[i]] = mapT.get(t[i],0) + 1
        
        for c in mapS:
            if mapS[c] != mapT.get(c,0):
                return False
        return True 