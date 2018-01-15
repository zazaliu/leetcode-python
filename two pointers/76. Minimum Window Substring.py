class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tDict = {}
        for i in t:
            if i not in tDict:tDict[i] = 1
            else:tDict[i] += 1
        print(tDict)
        tLeft = len(t)
        i = left = right = 0
        for j,value in enumerate(s,1):
            if value in tDict:
                tLeft -= tDict[value] > 0
                tDict[value] -= 1
            if not tLeft:
                while i < j and (s[i] not in tDict or tDict[s[i]] < 0):
                    if s[i] in tDict:
                        tDict[s[i]] += 1
                    i += 1
                if not right or j-i < right-left:
                    left,right = i,j
        return s[left:right]


Solution1 = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(Solution1.minWindow(S,T))