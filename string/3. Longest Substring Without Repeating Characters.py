class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        依次将字符串字符分别加入字典，设置不重复子字符串起始位置 start， 遍历过程中依次查找当前字符
        是否已经存在于不重复子字符串中，如果不存在，则更新最大长度，否则，更新 start 位置
        """
        start=0
        maxLenth=0
        sDic={}
        for i in range(len(s)):
            if s[i] in sDic and start <= sDic[s[i]]:
                start=sDic[s[i]]+1
            else:
                maxLenth=max(maxLenth,i-start+1)
            sDic[s[i]]=i
        return maxLenth
