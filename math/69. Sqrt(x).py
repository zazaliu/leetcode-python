class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        牛顿法：（https://www.wikiwand.com/zh/牛顿法）
        将题目转化为求x*x-a=0的零点值，利用牛顿法迭代求近似值即可
        """
        step=x
        while step*step > x:
            step=(step+x/step)/2
        return int(step)