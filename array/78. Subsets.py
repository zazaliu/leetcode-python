class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        动态规划（自底向上）  
        - 首先设置初始化子集合res=[[]]
        - 然后分别从nums第一个元素开始计算子集合集res，其中集合每增加一个元素，则增加新元素后的子集合集
        变为加入新元素前子集合集所有元素与之前子集合集所有元素的集合加上当前元素  <br> 例如：[1,2]的子集合集
        为res2=[[],[1]],[2],[1,2]]，则[1,2,3]的子集合集为
        res3=res2+res2[0].append(3)+res2[1].append(3)+res2[2].append(3)+res2[3].append(3)
        - 则计算后的res即为结果
        """
        res=[[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                temp=res[j]
                temp=temp+[nums[i]]
                res=res+[temp]
        return res

s=Solution()
print(s.subsets([1,2,3]))