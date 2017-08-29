class Solution(object):
    def canConstruct1(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        """
        1.依次从mazagine字符串中删除ransomNote中的字符
        """
        rList=list(ransomNote)
        mList=list(magazine)
        for i in rList:
            if i in mList:
                mList.remove(i)
            else:
                return False
        return True


    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        """
        2.利用 set 和 count
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
