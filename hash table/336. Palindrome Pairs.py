class Solution:
    def palindromePairs1(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        """
        暴力求解（超时）
        """
        res=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                temp1,temp2=words[i]+words[j],words[j]+words[i]
                if temp1 == temp1[::-1]: res.append([i,j])
                if temp2 == temp2[::-1]: res.append([j,i])
        return res
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        """
        字典法：
        1.依据words中每个元素的值与索引的生成一个字典wordsDict
        2.遍历该字典的key，然后将该字符串分为左右两个部分，分别考虑左右两部分的回文特性：
            a.当left部分为回文字符串时，查找right部分的逆序right[::-1]是否在wordsDict中，是的话将其索引值与当前字符串索引值加入res中
            b.当right部分为回文字符串时，查找left部分的逆序left[::-1]是否在wordsDict中，是的话同样将其索引值加入res中
        注意：res元素的唯一性
        """
        wordsDict={v:k for k, v in enumerate(words)}
        res=[]
        for k,v in wordsDict.items():
            for i in range(len(k)+1):
                left,right=k[:i],k[i:]
                if left == left[::-1] and right[::-1] in wordsDict:
                    if [wordsDict[right[::-1]],v] not in res and v != wordsDict[right[::-1]]:
                        res.append([wordsDict[right[::-1]],v])
                if right == right[::-1] and left[::-1] in wordsDict:
                    if [v,wordsDict[left[::-1]]] not in res and v != wordsDict[left[::-1]]:
                        res.append([v,wordsDict[left[::-1]]])
        return res



s=Solution()
words1=["bat", "tab", "cat"]
words2=["abcd", "dcba", "lls", "s", "sssll"]
words3=["eieeebdjfagghdbfchia","gfdeaccfjhgcgg","gbegjcjjihgjc","jcfdgcgjc","fieihihejjcai","ihgbbec","ejdhiadahjbbfhge","dbhjhgdhi","cbjbdhh","bhijghhaid","ffgfdcficeafibifbih","fijeecbifijjdfddhafi","chgjcbaee","hdjiaiafgaeib","ejbbfdgbc","acbh","efg","aedjdijjeacbajefj","heddcjijfcfcjcije","i","hjiee","idjbdgcchcigchf","dgadifhgfhbcdbbbecc","afjhihijeffj","defffbdgceceefdfcb","eiaeidghdifdbggaggfc","bhhadhfidhha","cgdhjaadgjbde","aiaghjaghigea","hdceeehgga","bgadhjhieff","dicebicahecbi","fedebdihigbaeggd","idbifdghbb","hieid","abjeaa","figjbbebjcahcf","dcdbidbdhdfbbebi","ghfbfbife","bbb","hhdj","hdiai","jjhgch","fjefbdcacijcieii","beeagfhiiccaefe","efbegbcicahjcia","ehjhjgedbijjehged","ehhhdajbjiicfh","edbeeidajii","faicgcafhece","ebgahggfjeajbihcd","bciggiajgjfidhiidj","dfhffebbgcjdda","iafchhgadbid","fagacbadfcbbaf","hjjgbgiefgci","hdedjcigdhjbhgahcab","ehfjibdc","aageeicai","fii","jbdcebjfci","jhbibdbchchdab","jacaiabefihfiagaj","hfjedjfjdgebjichgcj","cdeieijdfeaafg","ggcjcdhchhj","jdi","fj","gbdfhddbahg","fa","cdgcjaai","icheejeehfiedjaa","f","dieeg","hfaibdbjigciadaifcb","cgda","c","bfiddgeabefciahe","ieihahicdeijfjdeie","ihfad","gfiijjcaffeicfea","hgafeaiegjcbihbd","aiedijaa","fafagiiajafdhdh","jhihcbiege","jaghhccheejjce","aiahf","hjicjcahiahcgbhcif","dhggbdcddgegac","jc","ccbhebhcehj","ajhgifcfdcdgfehigd","ajfejeahbgfjib","idigcgbbijfe","hfghgbcjahjghf","eji","ibejcgcfdebhhd","jeeigaiadhh","jhbggbfejef","ahidddbfacddfhjhjgg","dhc","efa","hjbehadfbdeahd","jfead","fhhfehgjc","fgjefeijciahfa","ahgabaebdcdii","gjahd","jfideaaiieigbchgjb","djfigbbifefiffchdd","dggefibheadgije","ch","fijgchjcae","jchgihcfhbf","jhied","ceifjjjaihijhajhfeab","dhfdbdcebbacdg","gdai","gfjcajfb","ihbefhddjfjeefgcicje","chajbecjfgcgbf","bdhgfafafheeb","jjhhgidgcfcaf","habfbc","djfbj","ighgebefcegacach","hejdgig","faeejcjgciid","feccehbfacaecbhbgbc","j","hceaa","jbgibjjccbjbjediacda","igdfhjefcjg","adh","addfafaiafceddbbbb","ihjjjhhbig","ebbabghcb","aceiehheccahhjgcjc","edgjjch","ddhbecdgdddhfejbbcai","dfjbiiedeedgiigf","he","jbachifbif","cacgabgghdhhhgbdf","d","gcahejiec","ihajcbg","jjiib","hideihacfhbh","dhbihjchhj","eaididibhbgcaabifhi","chfb","dje","b","beaehdcffj","afjijfaggg","hb","dgcgadfafifh","eihdhhch","faehddchdgahifb","baahieaiddefhh","eedgaejjbhcebbgiih","becbaad","giafhieb","cijjh","efigdfgdh","ffgfbgfiabijhc","aafdcfcjecbebfib","faffejbjhedfibfhf","fd","gjhbi","geeifjbfje","jbghifihabhb","gehffffgicfjaed","ddejhffad","acbfbehgcdjcgidfgj","hbacf","ece","hfabihdhgggjjcgja","hibdjbgdbadeiajchd","aghgafejegcchidide","ddcebfbgihcbjegefj","eahhhbabedgi","jbjcifjhieg","fdfgfaieejh","bfhchaghjjchba","ehiae","heifahghjciahhdh","ig","ihc","hccjcjaiiaa","hdhefbgefjadbiiacf","gajgcjhadd","gfce","eaegbfjeihfebjj","fjjdeicbda","efbbeijgceiiee","ahbjebae","ffa","gjdfijghgdfb","hfgagdbbghcejh","afajbechh","cicigfdbfjccdccegf","ffhdiifadbjdjijc","hdggdjajb","ebdia","gfdjhbj","bgdfc","dfceagabfecbcjbhb","aheeifgiibjigh","ifgdaidba","ciadjfjhd","eggadicdec","g","cheiafaehiefcb","dhhhebhicffiecbehb","ahfhjhfideafc","befcacfeddaiegeghff","bgahbgaibdhbdddje","eedghcafgcfhebdehead","igjgadicjdgbhhbheh","gaecj","iceieaiigb","bdjfhihgafjhcb","jge","ic","dciehedicbaee","fhcfjfdcggbhagea","ecidjgffggbcejecigg","jabi","cficjchbefd","dgcdhhebgfhbgbdca","eeabbfaibdedhfdc","giaicjie","hhfejfgfcbd","bfeccfjgeifjhigdgdhg","cjhjjbchh","cehddjbjbdheaaj","iijj","eciigagdaf","fb","eae","gbegd","dcgecabdgjabe","dd","ddiceefed","fehadhcfbafhfjficj","cfgdihcfa","fcgejba","chchdaeaii","ijfjhjaii","accaeheabiceijhadh","bdad","jgcjaed","bccbejd","ha","cbjjf","cgh","fjfcdfbdhdfbhhb","afi","hcdh","hdchiedjahdh","hcdhbjibhgachcjiiihj","ahjdjgfegafihaaijgfi","daceabdecijcch","ejgdaecjjcbhcbifhea","je","gafihfgbibijdhejadbg","fgbdafddifcgjbecij","fbhhebh","ffbijihbg","hjdfdijaaai","eajaidbjejbai","edfgfhehjdeegba","fjdjjcaidcjegi","beeijibhdfbfiig","hfddejcb","eaaiefha","haifdfjgeiidehad","ddagad","cadfejdfdeijb","hhebgbh","cefid","idgiaebjdcdijg","bjiddgdcfbiddbd","jfgdabdaid","dibfefcdcgdacihfe","fhghhfjjagifadagahgd","jecjjcchjfiaj","eggeiehaeggbdcgdebia","dfh","djdhbdgcgcjjgagdjdib","ddeigbigbjajjdcbiah","bgbaeea","daedcccfaejiiijceeac","heiegcgadageidgfida","ibgeh","cghejcedbbfba","ebfbchddcjhdhhh","dgeejicfdadhhfj","eaahddh","fhaddbaeggcgehf","eebiahbbhfjbba","ifh","ahi","ijigjdhc","hhjcceihjidjhbjab","abghce","ei","fjcbh","gec","aecaecaaicfgddfdjage","gdfgdh","abbijffichbcfadgjgc","ddccjfbedaih","biecdabhih","dhaejgaiecaefdbb","eeccjffjgag","ci","gca","aghhjah","hdfedgjgjicg","djebdhcfehbcgd","fidaefbfffd","dajadgbabheejaf","degeciccaeij","hghfdcadfgaaaaebacj","jidicafdjgchcjeaddg","bhjchgbj","jajb","cjahfgachghdajbjai","igahibghbiejjeeche","dcijchgabhajaijga","biecej","gedfdbhfci","ddjcfahiahcdaijbeh","da","gcehj","bjaedeiedcbf","jjjbacbiigej","jafejfdjeijdhfhacia","afjjhbdfcajdeege","cgj","gjjgiaefefhjhabaad","hfj","hgaajeajeihhbdcfb","gjagdfeffffjg","bfbbbgic","ddjahjeihcgcebec","ijacdhjbhfgggi","jjbjifjfib","jii","adfjeeihgfcdcacfff","ejid","hehcbjhijcddbhc","ehcbjadi","cdbcjiiaaedid","a","jhhajf","eccgjigajcadcdijjhhg","hebcbichdiffdje","ef","cjcjjcigagdeiahaigh","bjeahjeddjgcfbhabde","gjaijjcibaia","hcghdghaba","chadficjhd","ebfbbjgjbehdh","gdhfeijiedh","bgecgf","hcfc","ajbhaehij","idj","gjeafabahabacehhadj","didggidbefag","bbeijgcif","fg","dhheeeiaai","gi","ccbbhjeechjgdbdjgeg","cgdeagc","bjaegifjejdiac","ehebihifehagdcfgd","fgdfgiedgchbffebe","acea","ifhccjhjjdcdcdd","eafabdccg","bciafbaddbiajcfaba","dibhadicbedaedcf","icbjcbgdjcbbbihciac","dchhfaaedgjc","jdid","cgfiecbfhgcdih","acgiahceegjij","gcjibifagcbfcaf","cdejbddbcfggh","eegadhiggd","jhfeihihiggheaeh","eaegfhjigghh","dgdhjdhdfccgjed","dgcdafhggedgihd","hahbghccdjfdaicgjh","dgiedc","cgefaigdahja","geeibedddejiid","hhcbgcddeghjjhahad","ajcfegjdfej","bciefcehjdgacfhiabhb","bejddfchf","icgfihjcfdjbjihgfdf","hfcge","ggici","aiheciafhdij","dggdgadjbeahcbbed","edeeijcbijaaf","jd","hjbe","bafdhehigef","cfiiabjighdgcb","bfegji","aahgcfcfgaafaej","ebeab","cibceag","gbfffdgahjcgb","gdheadhf","h","ebhjjeig","hccacaabheehaeedg","jcag","bddgb","acbfbj","fcgjjhgedgghgc","gchhehadhbdjj","dabah","jeigdbiajiffdcc","af","bhdcce","hcgjjhaajdbbibiaaaef","ghfhgcgjbjhjjaha","ejdegcbfadeefcdg","ddefc","ibhhjebfhfjbgjhafdhg","jhgfbadac","gjiehddfhcjf","ahghjbhdhbgg","ifjeeicjdbbdhge","digei","ibdiafghbegcbd","efjf","fbhgidbjbaacb","hhgccfbi","egiigbaebeh","ifcabgiiie","cee","haejehfabheechj","gchheebifi","dfjjggidicbhgace","ifgaaghfjfbbhaacibj","ibcjhfa","hgajachehijbdbgfh","bgcbbahjgfae","fgadbhhhdfheecace","gacjedibfbhdbcfb","bdgggg","cid","hichc","dgjc","decchcfcfjb","fhaidcii","ja","ijdgiiajbe","hi","efgicgddfhdfied","hjafceb","ajdhjgjeie","caiechgjegegbdbee","dffiaefbefagie","affa","bbcaeffbhefdcfghedab","gjbe","gegfhhiihhfccbba","igcgj","efhbjcfdfdghiebgbbaf","fghddheejjcbadg","ceieiafeacj","acbcdjfejdbgcg","heheffbjagegig","bbecfgjdcfcahj","faebeadiejiheejij","ceijidbiagehh","jfehbijha","iejdiid","gedd","deejaicjcdbaj","hbcjhce","ahfjbe","jjdifbjfcjbb","iihebei","jjbdbjihghifijc","fhcjjifccdddh","jgbahb","deiifabadjadah","eajajijdheggbdjbfcdj","ijdgadceffag","edd","fi","eahfjiidebg","acajeahddji","fdhafdggcggiffbc","diigjihdebabiffcef","jdiiibbhii","chcgcfgcjj","iahicjfcjdddgjjjghi","dffcghijfehfhg","abgjbchcfijg","ddafiadhhciejhbehegi","bheic","jaigbfbbffhcjfddeab","dhcjhigjfdbfged","bifhfc","hgegfgfc","addjfi","iababijcfcbdb","ibgfiba","fgdjaejcfjibdg","jdhjfebjgbda","dehfaegigafcg","cdfbdjgfiggibechejgc","e","diccheec","ggd","aj","hjagfeehafec","agfbcdijdaca","cgcifccjbeegb","fji","dbfejghagca","iicehgdigjb","aiadaaagfbf","diidbddgjjhbfj","cidfigaefbbibdcgbig","ibfegcajcegidc","cehaibgccejieeceebgf","fiacaieiegagf","aijjhfdg","fbgjeheb","chciicbeebedbfgabe","iceicaiiccghgjf","bdfgecag","ejeicfihjcfdabge","dbd","ffie","dhee","jjefdfghaibfegbcbjii","dabbbcf","gfcjaibgiadh","cjcaahi","gddhaeehaafidf","aigbgddib","bdddfaedfcfbb","cifbf","efdibhebc","cfijhghb","fjiibjacegiac","jhijbejahbidcgg","dbjfbgfgdageia","eibbdegdciad","gjh","eddihjjfefee","dbgcjdfedjgacfafai"]
print(s.palindromePairs(words1))
print(s.palindromePairs(words2))
# print(s.palindromePairs(words3))