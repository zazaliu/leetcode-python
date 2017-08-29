class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        1）：去掉字符串右边的空格，转换为 list；
        2）：以此判断 list 每个元素，仅当该元素不是空格且下一个元素是空格时，计数 count 加一；
        3）：则分隔块个数为 count+1 （注意当字符串全部为空格时时即使计数器为零，结果也不能加一）
        """
        sList=list(s.rstrip())
        count=0
        for i in range(len(sList)-1):
            if sList[i] != " " and sList[i+1] == " ":
                count = count+1
        return count+1 if len(sList) > 0 else count
