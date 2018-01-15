class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1,n+1)]
        elif k == n:
            return [[i for i in range(1,n+1)]]
        else:
            res=self.combine(n-1,k)
            temp=self.combine(n-1,k-1)
            for i in temp:
                i.append(n)
            res.extend(temp)
            return res