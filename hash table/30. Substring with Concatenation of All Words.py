class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        """
        数据量大的时候，使用dict查找速度更快，用空间换取时间
        """
        res=[]
        wordsDict={}
        for i in words:
            if i not in wordsDict:
                wordsDict[i]=1
            else:
                wordsDict[i]+=1
        length=len(words[0])
        subStringLength=length*len(words)
        for i in range(len(s)-subStringLength+1):
            subString=s[i:i+subStringLength]
            newWords={}
            j=0
            while j < subStringLength//length:
                temp=subString[length*j:length*(j+1)]
                if temp not in words:
                    break
                if temp not in newWords:
                    newWords[temp]=1
                else:
                    newWords[temp]+=1
                if newWords[temp] > wordsDict[temp]:
                    break
                j+=1
            if j == len(words):
                res.append(i)
        return res

s=Solution()
sList="barfoothefoobarman"
words=["foo","bar"]
print(s.findSubstring(sList,words))

s1="wordgoodgoodgoodbestword"
words1=["word","good","best","good"]
print(s.findSubstring(s1,words1))