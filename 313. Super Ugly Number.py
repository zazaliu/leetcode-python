class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        tP = [0 for i in primes]
        for i in range(1, n):
            temp = []
            for j in range(len(tP)):
                temp.append(primes[j] * res[tP[j]])
            res.append(min(temp))
            for k in range(len(tP)):
                if res[-1] == res[tP[k]] * primes[k]:
                    tP[k] += 1
        return res


solution = Solution()
print(solution.nthSuperUglyNumber(7,[2,3,5]))