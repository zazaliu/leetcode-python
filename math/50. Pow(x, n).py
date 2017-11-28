class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        product = 1
        if n < 0:
            return 1/self.recurrent(x,-n,product)
        elif n == 0:
            return 1
        return self.recurrent(x,n,product)

    def recurrent(self,x,n,product):
        if n == 1:
            return x*product
        elif n % 2 == 1:
            product = product*x
            return self.recurrent(x*x,n/2,product)
        else:
            return self.recurrent(x*x,n/2,product)