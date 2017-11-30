class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        首先明确n个不等的数它们能构成的二叉搜索树的种类都是相等的。而且1到n都可以作为二叉搜索树的根节点，
        当k是根节点时，它的左边有k-1个不等的数，它的右边有n-k个不等的数。以k为根节点的二叉搜索树的种类
        就是左右可能的种类的乘积。用递推式表示就是
         h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2) ，
         其中h(0)=h(1)=1，因为0个或者1个数能组成的形状都只有一个。从1到n依次算出h(x)的值即可。
         此外这其实就是一个卡特兰数。
        """
        res=[1,1,2]
        if n < 3:
            return res[n]
        for i in range(3,n+1):
            temp=0
            for j in range(1,i+1):
                temp+=res[j-1]*res[i-j]
            res.append(temp)
        return res[n]