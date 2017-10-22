# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        """
        思路：先将区间按照每个start的值来排序，排好序以后判断一个区间的start值是否处在前一个区间中，
        如果在前一个区间中，那么合并；如果不在，就将新区间添加。
        """
        res=[]
        if intervals == []:
            return res
        intervals.sort(key=lambda interval:interval.start)
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1].start <= intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end,res[-1].end)
            else:
                res.append(intervals[i])
        return res