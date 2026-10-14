class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountS = {}
        CountT = {}
        if len(s) != len(t):
            return False
        for ch in s:
            CountS[ch] = CountS.get(ch, 0) + 1
        for ch in t:
           CountT[ch] = CountT.get(ch, 0) + 1
        return CountT == CountS
