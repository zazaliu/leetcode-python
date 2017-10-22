class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.DFS(candidates, target, 0, [], res)
        return res

    def DFS(self, candidates, target, start, addList, res):
        if target == 0:
            return res.append(addList)
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            # 注意下一行传递addList时不能用addList.append(candidates[i])，因为使用append会改变原来addList的值，
            # 而使用DFS是要回溯的，因此不能改变addList的值
            self.DFS(candidates, target - candidates[i], i, addList + [candidates[i]], res)