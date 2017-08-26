class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        先创建元素个数为 numRows 的 list， 内容为空，然后依次遍历字符串的每个字符，依次填入 list 内容中
        填入顺序依据索引 index， 先从 0 到 numRows-1， index每次增加一，即顺序，当 index==numRows 时，
        更改为逆序，index每次减一，之后将所有已经填入 list 的字符转化为字符串即为结果

        """
        if numRows == 1 or len(s) <= numRows:
            return s
        numList=['']*numRows
        index,flag=0,1
        for i in s:
            numList[index]=numList[index]+i
            if flag == 1:
                index=index+1
                if index == numRows-1:
                    flag=0
            elif flag == 0:
                index=index-1
                if index == 0:
                    flag=1
        return ''.join(numList)
