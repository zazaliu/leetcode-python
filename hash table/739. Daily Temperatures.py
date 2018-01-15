class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        """
        hash table法
        """
        temperatureDict = {}
        res = [0 for i in temperatures]
        for i in range(len(temperatures)-1,-1,-1):
            for tem in range(temperatures[i]+1,101):
                if tem in temperatureDict:
                    res[i] = min(res[i],temperatureDict[tem]-i) if res[i] != 0 else temperatureDict[tem]-i
            temperatureDict[temperatures[i]] = i
        return res