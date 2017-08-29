class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        依次遍历每个单词，先排序，然后查找字典中的 key 值，选择相同的一组加入，遍历完成后依次输出即为结果
        """
        sDict = {}
        res = []
        for i, value in enumerate(strs):
            index = ''.join(sorted(value))
            if index not in sDict:
                sDict[index] = [value]
            else:
                sDict[index].append(value)
        for value in sDict.values():
            res += [value]
        return res