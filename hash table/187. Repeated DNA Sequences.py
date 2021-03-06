class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        用字典存储所有的长度为十的子字符串，输出数量大于一的即可
        """
        res=[]
        dna={}
        if len(s) < 11:
            return res
        for i in range(len(s)-9):
            subString=s[i:i+10]
            if subString not in dna:
                dna[subString]=1
            else:
                dna[subString]+=1
        for key,value in dna.items():
            if value > 1: res.append(key)
        return res

s=Solution()
dna="AAAAAAAAAAA"
DNA="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
tl="CCAAGTCTAAAAGAATGGGCAGAGTTGCTCTGCACGTTCCGGATACGATAAGAAGACTCCGCCGGGCACCGCCAGTCCCTCGCAGGGGGACACATTGGAATCGGATAATCGATCACTCCGCGCCACCCCGGGTTACGCACCTCACGTTGAGTGAGGAGATGGTGACATTTCGGCACCTATAGGCACGCTCTACCGGAACAGCATCTGTATCAGATGGCAATTCGATGGTATCTTGCGTGAATCAGGAAGTTTTATGTGGCTTCCGGATGACGCGAGATTTTGCGTGAGGTGAGCGGTTGCGTTACCGGTTAGTAGCCCTTAGTAGTTGAAGACAGGCGAGCAGGTGCAGCTGTCCACACGGTATAGGGCAATCAACTTCCATAAAGCATATGTTGTGTAACACCTGCCACCCCTTGTCACAGGTTTCACCAAGACCACATCGTGCTAAAGTTAAACAACATTCGTAAAAGTGCAGAAATTGAAGTATTTGATCTGAGATTACGTTTCAATCTGGAATCCGAAGCTATAGGAGAATGTTGGACCATACGGTGAGTAGAATCGCCACTCACGTTTCGGTACTAGCACATTAGTACGGATCCCGATCGGGGTGGTGGGGCGTTCTTCATGTATACCATTGCGACGGAGTCTGGCTAAACCTTTAGGCAGGTCGCAAGGCAGAATCATGAGCACAATCAGGGTGGCCTGGATCCGTCATGGAGGAATCGGGTCTTCCCGTTTGAGGGGGCGGACTTCGCGGCGCACGTCAGGACACCAAAGGCTCTAGTACCCTCCTATCGAAACTCTTTAGCGAGTTTTGTCCAGCTAGCTTCATCTAACAGGCTCAAAAGTCATAAGAAGGCTCACTTTAAGTAAAAAGTCAGGCGCAAAGTCTAGTGGCGCATTTGATACGTTCCCAGGGCACACATGCACCCCTCTGCAACATTTCAGGCCGCAATTACACTGTAGCTCACCGGGGTCGAAATAGTTAACTCAAGTTTCCGGTCCCTTCCCCACAAAGATCTGTATATGAACCATCAAGACGTGGCTAATAATTATATCTCCGGCCCCTGCCACAGGAGAGAGGGAGCCGGAATGACCGTAATTAGCTCATAAAACTTACCAGCTTATAGGAAGTCGGCTTCTTTGATGACTACGAAATGGTAGGGCGTTCGTTATGTGCTCTCGCGTTCAACATCCGGCGCGACCAATATGCCAACATTCGGAAGCGTGTGATAAATTGCTGAATCCATAGTCCCATAGTGGTTGATAGTTACTCCGGTTCTGAACTTGTGTAATAAATGCCAACATTCTCGTTACTCAGAACGACAGTCAAAGTGCGTGTCACGTTGGGCCTGGGGCACGTCGCTGGTATTCGGGTACTTTACTAATGAATAAGGATTGTGTTGTAGGCCCCTTAAAAACAGGGAATGGGCCGAATACATTTAGCTTGATTCCAGCGGTAGTACTTGGCGGAGTCATGTACCTTACCCGCGCATATAACTCCAGTCGGACATACGTTAGAATTTTGAAAAGGCTGGCGGGGACCGCGAGATGTCCGCCACCCATGTCGCGGCGTGAGGTGACATGACAGCCAGGCAGTTGGCTCGGTGTCCCAGGTGCACGGCCTCACTTAAACTAGCACCCGACGGATTCTTCATACCTGACGTGTGTATTTTTTGACTCTGAGGTTCTGAATAACATCCGTAGGCACATGTGAGAGCAGGGACGGTTCATCACCTATGGTCTCCAGGTACAGCCTACGTGGGGTAGGACCACAACACTCTGTGTGCCATACGGTCGGTCAAGACCTAATGGCGGGAAAAGTGGCTTTAGTCCCGTTGTACGAGGGAAATCAGTTTGGTTACGTGAAAAGTTAATGCTGCATCCAGTGACTACGATATTACCCGGCGAAACGAGATCGTAGTAGTTCTATGTCGGGCTGTCACCTAAGACACCATAAAAGGCGATTAAATATGGATGTGCGGAAGGGTGACTTCTACCCTCAAGACAACTGACTACCACCTTATACGCGCTTCATCGGGAGCTAGCGAGGCGCATCGCACAGTTACAAAGGGGTGTGGTAGGCACCCTGAACACAGAGAGTCACGCCGTGGGAAGACGACGGCGCCCGAACTGCTATCAGCTTCAAACTTCCAACGCCCATCGCGAGCGTACTGAGTTTTCACAGCGGGCTTCCACAAAGAAGTGGCCAGGCGACACCACATTACTGGGTCTGAGCCTCAGGCCAGGCGAAGTAATTGGTTTTGTGGGAATAGTGCACAAATGACCCATATGTGTTGTCAAGTCCCCTGCGACCGTTCGTCGGCGTACCCTTCGCTAATTTCCTAAGCACAATAATTGCAACCCCAAATGAGTCTCGTATTAGAGTAACGCAGAGTTAGGCTCCCCGAAAACGCTAGTCCGGAGCTTGGGATAAAAATAATGATGTAGGGCGGGACCCCGTACTTTCGCATAACAGGGTTTTTGTCGGTTGGCTTGTAAATGCAACTTGGGTTCCACAATCCCACTGGACAAGACAGGAAGGTGAAGAGGGAGCCGATTAAACCCAACTCAACTAGAACTTAGATCTTTCATTCACATCGTGTCAGTACAAATTTGAAAGAGAAGTAGGTACATGGGAGGAACGGGTTACGCCGAGTCTGATATTCTGTGGGAACTCCGTCTGGTCGCAGAGTTACGCCATCACAGCATTGGCTGAGTATCCAATTTGCCTATCACGCAACTACCATTTGCCGATAGCGGACCGACCCTATTTGAGCTATGGTATGTTCACGAATACAACTACGTCTGACAAGACGAGATCCTAAGCACAACTCCTACGATTCCGGACGTCTGGCCCTTGGAGCACTAATCCCTGGGGAATGTCACCAGAGATGTTTACGGCATGAAGAATGGAGGTCACAATTATTGAGAGACGGCGGTATGCACCATATCCAGGGTGCAGTGAGACGATAGACGTAGGGGAGCGGAGCGTCGAGGTGTCTCTGCCAAAGGGCCCCAATGATCCTGAATGGTGTAATCCGGAGACTCGATGGTATCCGCCGCAACGGTTCACTCCGCGTATGGCAGTTGGCTACGTGGTCGCGAGGACAGCTGTACGTTAAGCTAAACGATCCCTTAGCCTCTCGCAGATCGAAGTGCTAATAGTCCTGTCGCAGCCAGGATTGCGAAACTACGACTCAGGGGTAATCGCGGATAGCCTGATTTCATCCGAAAGACCCACACTATAGTCTGTGGTCGGTCCCAGGCGGTTCACGCCACCGGCGACATCGGCAAGTCTACAGGGGTTGGGCCAATTTCCGATAGGATCTCGGAAATGGTATCTCCGACCAGCGCAAACGCGCCACCCTGCGAGTCCGGAGTTTGCTACTCTTCAAATGAACCGATCGCGTCGTCGTTGAAACCGTGAGAGCAACCAGAATTACATTAAGCTCATCGGGATATTGATCCAATTGGGTAAATGTCAACGCTTCAATTTTTGCCGTGTCGCAACCTCCGGATAAACTTAGTACAGATCTTTTGTCGTAGAACGTTGTGGAAGCAGCAGGGAGACCCTGTACTTTCGTCACCTATCAACGTTTCCACCTCTGGTGATGTAAAAGCACGCAACCTACTCCGATACCAATCTGAGTTATGCTGTAAATTATTGGACGCCAATGGGATAAATGGGTAACGTGACCGATACGAAGCTGGCCCTTTCTCCCTCCAGTACCGATGGAATCTAGTACTTTTATAATGATTGGCACGGACGCACCGGTGTGGTTGACCGATTTGGCGGTAACATTGCGGGTTAGGGGGTTAATATATAACGCCTTCACCGATCGCACTACACGCAGATCGGAGGCTCCACTCAGACGTAGAATTTAAACAGAGATGGCTAGCGAAACTCCAAGCAGACGGCAAGGCTGTTCACCAGGAAGCCCCCTTCAAGATTCGTATTCAGGTATTGAGCAAACATCACTGACATTATTTTTGGATTAGCATAGGAAATATATACCGACTCGCGGTGGAGGTCAATGTCAACAGTGCGTGTTTTTAATGTCTGAACAATTTGCCTCCAAAATCTTGTTCGTTATCTCCCGATCAATTACCGCTAGCATTCGGGCATCTTGCGACCCAAGATTGAGATGAGGTGTGAACACTATCTGCACTGACAGCGGTCATAGCGGCGTAAAAATCGTGCGGAGGGAACCTTCACTCATGAGCAGCGGTGTAAAACCCTATGAGACAATTCGCTCCGATGGATAGTGTTGCGCTGACGTCCCACCGGACCAGCAGATATTCAACTCGAGAACATCTTAAAGTTTCCATCTAGGGCGGACCCTCAGGCTTTGCACGTCGGGGCTTAATGGTAATATGAGGTACGATTTAGTCGAATGGTTAAAGACCGTGACCGTGATATGCGCAACAATTCCCTCTGATACCCACTCATCGGGGTGGATTCTGAACACAGTCTGCATAAGTCTCAACCCATGGACGGGGAACTGTTACGAAATATGCAGGGGTCCGATTAGTCCCAGGGTGAGTCTTCCCTTACCGATCTCCACCGTGTTCCATGAGTCGCCGGTGTTTGATTACTGTCTATAGGCCTTACCGTCGTTACTGAGATTTATGGGCGGGGACGTTCGACTGCACTTTCAATTGGCAGAATTCCGTTAAATAAGGACGCAGTTGTCCGCGCACTTCATACCGTTGAGAAAGCAATACATTTTCTTGACACTCCCGGCATGTCGTCATATAGTACCGTCTAGCATTCTGCTAGCTCAAAAGCTCTCTGGCACCGGCATGTGTGACGTATCGAAAGAACAGCACTACAGCAGGCGAGTAGCTCCGGGCTACTTTGTTGCACAGCTACATGCAGTGGTGGTAACTTCGATTGATCCCGGCTCTAGGACTGAGCTTTAGCGAGTCCCTACCCGGCAAGTTCGCCTGATCCTGTCTTGGATGAACTTGGGCGGGCTCTGGCGGGTTGTTAGATC"
print(s.findRepeatedDnaSequences(DNA))
print(s.findRepeatedDnaSequences(dna))
print(s.findRepeatedDnaSequences(tl))