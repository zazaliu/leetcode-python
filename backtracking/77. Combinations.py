class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """
        DFS
        """
        nList=[i for i in range(1,n+1)]
        res=[]
        if k <= n//2:
            self.dfs(nList,[],k,res)
            return res
        else:
            self.dfs(nList,[],n-k,res)
            for i in range(len(res)):
                temp=[x for x in range(1,n+1) if x not in res[i]]
                res[i]=temp
            return res
    def dfs(self,nums,temp,k,res):
        if k == 0:
            res.append(temp)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:],temp+[nums[i]],k-1,res)

    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """
        递归
        """
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [[i for i in range(1, n + 1)]]
        else:
            res = self.combine(n - 1, k)
            temp = self.combine(n - 1, k - 1)
            for i in temp:
                i.append(n)
            res.extend(temp)
            return res


s=Solution()
print(s.combine1(4,2))