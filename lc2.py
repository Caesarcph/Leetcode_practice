class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq(s):
            ans=[0]*26
            for c in s:
                ans[ord(c)-ord('a')]+=1
            return ans

        return freq(s)==freq(t)