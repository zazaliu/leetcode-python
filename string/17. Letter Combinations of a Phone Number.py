class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numDic=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if len(digits) == 0:
            return []
        res=['']
        for i in digits:
            temp=numDic[int(i)]
            resTemp=[]
            for j in temp:
                for k in res:
                    resTemp.append(k+j)
            res=resTemp
        return res
