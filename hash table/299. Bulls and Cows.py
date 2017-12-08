class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A,B=0,0
        secretDict={}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A+=1
            if secret[i] not in secretDict:
                secretDict[secret[i]]=1
            else:
                secretDict[secret[i]]+=1
        for i in range(len(guess)):
            if guess[i] in secretDict:
                if secretDict[guess[i]] > 0:
                    B+=1
                    secretDict[guess[i]]-=1
        return str(A)+"A"+str(B-A)+"B"



s=Solution()
secret1,guess1="1807","7810"
secret2,guess2="1123","0111"
print(s.getHint(secret1,guess1))
print(s.getHint(secret2,guess2))