class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        先将字符串分割为单词列表
        再将单词列表反转
        再将列表还原为字符串，（单词之间增加空格），再将字符串反转
        """
        return " ".join(s.split()[::-1])[::-1]
