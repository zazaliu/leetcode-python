class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        解法：转化数学问题，公式计算
        当行数或者列数为1时，只有一种走法；
        其他情况下：行数为m，列数为n，则走到终点需要横向步数m-1，纵向步数n-1，
        就化简为在m-1的横向步数中插入n-1的纵向步数问题，总步数的全排列为(m+n-2)!(m+n-2阶乘)，
        由于横向步数与纵向步数之间没有差别，则分别除去(n-1)!(n-1阶乘)与(m-1)!(m-1阶乘)
        """
        res=m+n-2
        if m == 1 or n == 1:return 1
        if n == 1:return n
        res=self.factorial(res)
        r1=self.factorial(m-1)
        r2=self.factorial(n-1)
        return res/r1/r2
    def factorial(self,n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)