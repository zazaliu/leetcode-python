class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        sList=list(s)
        left=0
        right=len(sList)-1
        while left <= right:
            if sList[left] in vowels and sList[right] in vowels:
                sList[left],sList[right]=sList[right],sList[left]
                left=left+1
                right=right-1
            else:
                if sList[left] not in vowels:
                    left=left+1
                if sList[right] not in vowels:
                    right=right-1
        return "".join(sList)
