class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict,tDict={},{}
        sRes,tRes=[],[]
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]]=[i]
            else:
                sDict[s[i]].append(i)
        for i in range(len(t)):
            if t[i] not in tDict:
                tDict[t[i]]=[i]
            else:
                tDict[t[i]].append(i)
        for k,v in sDict.items():
            sRes.append(v)
        for k,v in tDict.items():
            tRes.append(v)
        sRes.sort()
        tRes.sort()
        return sRes == tRes


s=Solution()
s1,t1='paper','title'
s2,t2='ab','aa'
s3,t3='ab','ca'
print(s.isIsomorphic(s1,t1))
print(s.isIsomorphic(s2,t2))
print(s.isIsomorphic(s3,t3))