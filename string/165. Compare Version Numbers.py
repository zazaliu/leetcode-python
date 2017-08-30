class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1=version1.split(".")
        l2=version2.split(".")
        for i in range(min(len(l1),len(l2))):
            if int(l1[i]) > int(l2[i]):
                return 1
            elif int(l1[i])<int(l2[i]):
                return -1
        lenth=min(len(l1),len(l2))
        res=0
        if len(l1)>len(l2):
            res= 1 if int("".join(l1[lenth:]))>0 else -1
        elif len(l2)>len(l1):
            res= 1 if int("".join(l2[lenth:]))>0 else -1
        if len(l1)>len(l2) and res == 1:
            return 1
        elif len(l1)<len(l2) and res == 1:
            return -1
        else:
            return 0