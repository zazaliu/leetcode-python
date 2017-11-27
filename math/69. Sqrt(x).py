class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        牛顿法"""
        step=x
        while step*step > x:
            step=(step+x/step)/2
        return int(step)