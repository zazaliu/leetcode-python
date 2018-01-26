class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 6:
            return n
        t2, t3, t5 = 0, 0, 0
        res = [1]
        for i in range(1,n):
            res.append(min(res[t2]*2,res[t3]*3,res[t5]*5))
            if res[i] == res[t2]*2:
                t2 += 1
            if res[i] == res[t3]*3:
                t3 += 1
            if res[i] == res[t5]*5:
                t5 += 1
        return res[n-1]