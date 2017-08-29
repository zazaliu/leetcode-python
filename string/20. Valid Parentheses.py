class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        listStack=[]
        for i in s:
            if i not in pairs:
                listStack.append(i)
            else:
                if listStack:
                    if listStack[-1] == pairs[i]:
                        listStack.pop()
                    else:
                        return False
                else:
                    return False
        if listStack:
            return False
        else:
            return True
