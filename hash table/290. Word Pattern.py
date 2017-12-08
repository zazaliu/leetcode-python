class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split(" ")
        patternDict,sDict={},{}
        for i in range(len(pattern)):
            if pattern[i] not in patternDict:
                patternDict[pattern[i]]=[i]
            else:
                patternDict[pattern[i]].append(i)
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]]=[i]
            else:
                sDict[s[i]].append(i)
        patternList,sList=[],[]
        for value in patternDict.values():
            patternList.append(value)
        for value in sDict.values():
            sList.append(value)
        patternList.sort()
        sList.sort()
        return patternList == sList



s=Solution()
pattern1 = "abba"
str1 = "dog cat cat dog"
pattern2 = "abba"
str2 = "dog cat cat fish"
pattern3 = "aaaa"
str3 = "dog cat cat dog"
pattern4 = "abc"
str4 = "b c a"
print(s.wordPattern(pattern1,str1))
print(s.wordPattern(pattern2,str2))
print(s.wordPattern(pattern3,str3))
print(s.wordPattern(pattern4,str4))


