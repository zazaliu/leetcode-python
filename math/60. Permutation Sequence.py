class Solution(object):
    # def getPermutation(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: str
    #     """
    #     # 初始化序列，全排列中最小的一项
    #     start = [x for x in range(1,n+1)]
    #     for i in range(1,k):
    #         start=self.nextPermutation(start)
    #     start=[str(x) for x in start]
    #     return ''.join(start)
    #
    # # 寻找当前序列的下一个全排列序列
    # def nextPermutation(self,start):
    #     for i in range(len(start)-1,0,-1):
    #         if start[i-1] < start[i]:
    #             begin = i-1
    #             for j in range(len(start)-1,begin,-1):
    #                 if start[j] > start[begin]:
    #                     end = j
    #                     start[begin],start[end] = start[end],start[begin]
    #                     start=start[:begin+1]+start[begin+1:][::-1]
    #                     return start


    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """
        解法：
        采用的方法是直接计算第k个Permutation。
        假设n = 6，k = 400
        先计算第一位，
        第一位为6，那么它最少也是第5! * 5 + 1个排列，这是因为第一位为1/2/3/4/5时，都有5!个排列，因此第一位为6时，
        至少是第5! * 5 + 1个排列（这个排列为612345）。
        5! * 5 + 1 = 601 > k，所以第一位不可能是6.
        一个一个地枚举，直到第一位为4时才行，这时，4xxxxx至少为第5! * 3 + 1 = 361个排列。
        然后计算第二位，
        与计算第一位时的区别在于，46xxxx至少为第4! * 4 + 1 = 97个排列，这是因为比6小的只有5/3/2/1了。
        最后可以计算出第二位为2。
        最终得出第400个排列为425361。
        """
        factoral = 1
        k = k - 1
        res = ''
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, n): factoral = factoral * i
        for i in range(n - 1, -1, -1):
            current = k // factoral
            res = res + str(nums[current])
            nums.remove(nums[current])
            if i != 0:
                k = k % factoral
                factoral = factoral // i
        return res


s=Solution()
print(s.getPermutation(6,400))