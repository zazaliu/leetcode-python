class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        """
        解题思路：这题是简化目录，每一级目录前面都有一个斜杠，我可以首先对斜杠进行分割，分割之后得到的结果
        无外乎4种情况：正常目录名称，空字符，".",".."。对于“.”和空字符我们忽略它，对于正常的目录名称我们
        直接压入栈，对于"..",我们把栈顶元素出栈。通过这些处理之后，如果栈为空我们就返回根目录，如果栈不为空
        我们就逐个出栈并在每个元素前面加一个斜杠，最先出的位于路径的最后面。
        """
        listPath = path.split('/')[1::]
        res = []
        for i in listPath:
            if i == '.' or i == '':
                pass
            elif i == '..':
                if res:
                    res.pop()
            else:
                res.append(i)
        return '/' + '/'.join(res)
