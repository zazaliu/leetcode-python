class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict,tDict={},{}
        for i in range(len(s)):
            sDict[s[i]]=sDict[s[i]]+1 if s[i] in sDict else 1
        for i in range(len(t)):
            tDict[t[i]]=tDict[t[i]]+1 if t[i] in tDict else 1
        return sDict == tDict



s=Solution()
s1,t1="anagram","nagaram"
s2,t2="rat","car"
print(s.isAnagram(s1,t1))
print(s.isAnagram(s2,t2))