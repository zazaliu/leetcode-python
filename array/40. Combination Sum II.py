class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.DFS(candidates,target,0,[],res)
        return res
    def DFS(self,candidates,target,start,addList,res):
        if target == 0 and addList not in res:
            return res.append(addList)
        for i in range(start,len(candidates)):
            if target < candidates[i]:
                return
            self.DFS(candidates,target-candidates[i],i+1,addList+[candidates[i]],res)