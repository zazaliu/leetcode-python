class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        如果列表长度大于一，不妨把第一字符串当做基准，用一个指针来表示在此之前的字符是满足题目要求的。
        遍历每一个字符串，用指针对应的字符与基准中相应的字符比较，如不同则前面的子字符串就是所要求的结
        果；如果全都相同，则指针右移。还有一种情况要考虑，后面的字符串可能没有第一个字符串长，如果指针
        超过了最短的字符串也应该终止。
        """
        if len(strs) <=0:
            return ""
        for i in range(len(strs[0])):
            for stri in strs:
                if len(stri) <= i or strs[0][i] != stri[i]:
                    return strs[0][:i]
        return strs[0]
