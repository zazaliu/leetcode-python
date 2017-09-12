class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxRes,begin,end=0,0,len(height)-1
        while begin < end:
            maxRes=max(maxRes, min(height[begin],height[end])*(end-begin))
            if height[begin] < height[end]:
                begin+=1
            else:
                end-=1
        return maxRes