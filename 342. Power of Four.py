class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        将整数转换为二进制数，若整数是4的指数，则满足：
        1.最高位为1，其余位为0（num & (num) ==0）
        2.0的个数为偶数（num & 0x55555555 > 1）
        """
        return num & (num-1) ==0 and num & 0x55555555 > 0



Solution1 = Solution()
num = 64
print(Solution1.isPowerOfFour(num))