class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        isalnum判断字符串是否由字母与数字组成
        """
        left=0
        right=len(s)-1
        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False

                else:
                    left=left+1
                    right=right-1
            else:
                if not s[left].isalnum():
                    left=left+1

                if not s[right].isalnum():
                    right=right-1

        return True