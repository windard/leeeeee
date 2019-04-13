# coding=utf-8
# @lc app=leetcode id=459 lang=python
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (39.43%)
# Total Accepted:    76.3K
# Total Submissions: 192.6K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: False
# 
# 
# Example 3:
# 
# 
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # unbelieveable
        if not s:
            return False
        
        a = (s+s)[1:-1]
        # return a.find(s) != -1
        return s in a
        # return bool(a.count(s))

    def ____repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 根据除数进行划分
        # 奇数排除
        len_s = len(s)
        gap = 2
        while gap <= len_s:
            if len_s % gap != 0:
                gap += 1
                continue
            step = len_s / gap

            # 换种思路
            # if gap * s[:step] == s:
            #     return True

            start = 0
            while start <= len_s - 2*step:
                if s[start:start+step] != s[start+step:start+2*step]:
                    break
                start += step
            else:
                return True
            gap += 1                
        return False

    def ___repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 有且仅有一个匹配，就是全匹配
        # Wrong Answer
        # 可以有小相似
        # abaababaab
        # Time Limit
        se = s
        index = 0
        len_s = len(s)
        while index < len_s-1:
            se = se[-1]+se[:-1]
            l_index = -2
            s_index = 0
            flag = False
            might = False
            count = 0
            while s_index < len_s:
                if s[s_index] == se[s_index]:
                    if s_index - l_index == 1:
                        flag = True
                        count += 1
                        if s_index == 1:
                            might = True
                    l_index = s_index
                else:
                    if flag:
                        if count > len_s / 2:
                            return False
                        else:
                            break
                s_index += 1
            else:
                if flag and might:
                    return True
            index += 1

        return False

    def __repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time Limit
        # O(n^2)
        se = s
        index = 0
        len_s = len(s)
        while index < len_s-1:
            se = se[-1]+se[:-1]
            s_index = 0
            while s_index < len_s:
                if s[s_index] != se[s_index]:
                    break
                s_index += 1
            else:
                return True
            index += 1
        return False

    def _repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 理解题意错误
        # 需要完全由重复构成
        se = s
        index = 0
        len_s = len(s)
        while index < len_s-1:
            se = se[-1]+se[:-1]
            l_index = -2
            s_index = 0
            while s_index < len_s:
                if s[s_index] == se[s_index]:
                    if s_index - l_index == 1:
                        return True
                    l_index = s_index
                s_index += 1
            index += 1
        return False


# if __name__ == "__main__":
#     s = Solution()
#     print s.repeatedSubstringPattern("babbabbabbabbab")
#     print s.repeatedSubstringPattern("bb")

    # print s.repeatedSubstringPattern("brmgmqtyxhfjrurkpcrelwzhroiuicilvxrjpkjmrovkjouaqnebjfjautxexhpsehdvrmhlbfvmtsomfsppzarvuozrwrmcypyrchefmctiuhwbblqcmkyiazbwqpbqhbkjioqxslhosdqvogxcsxmtxqppfsgmtqxegpdzakpunfpdmpiemwxlmpbsjhgfzelhtoiwyyqndisrzcylzxxloafyjmfisqrngajgactdknvjqvwrsvehvkheyooqegdkipsirnnbakmsfijyeohbyqgyewoketumimwzbkcbuouczfcftjgtzorflhprdlglzcnaorblgxnhdrmyausblliwvxpyivljayjoqmbykqhphvnjphmatuyqrooblzklatcsgfsswzhfuwpledozyopreftqeddgzfyhlqzjriongfzmjpnjdeakjtcqzfwylxhypihhsxuyfvnomaxqfxcqtegsjfswezuthdczbzzgumwhpvzuubmnhtfqazpeyjxhpcgsbiavuyejtdfngsdnnkgpkvtigsqxuypvgrtdpxoidwylqbzdnhsxengmfykcwbxftqiioyttutekwfpjmjhqwnfenpglqdqjwaumbnfvgjicrxldjswfhblwsriixauvdohedozjzjnqjawsvszevlbnejxdlryofhsivutxfgnojjgedgiatjpxunbgebwmjrwgnsdsathjepnivwkqhaocprktuihdzgmoyrhykqkphxzfvlvfljjacvwxdfcflotlicksuwjcvihrucyhohiscgphlumzkikskwlhswjofshbwfkmosfsawboqondyxvkuirofcemulntsxfismaujeibsvesvccpkufpykdvxsoqqvakidgthpwbmdthfvyrrejqomnlfbdxyejghpbqearrdkaihzbzdkrtxegehmbfqmozbpripibusbezagafqtypzhtgtwmlickmtbullvfdykezshekcfacmvifuwqcycosfkdqfkvgwbfoklznqbpewzjqwbvwdlqkwvcdgxjcborlcsautpzrriinmflpqccmxeqfezifqbssvtooknfbypqkucbngdzfirlmtvtjyldtgrjrhosfglrcnspvyraginubkpmiardjlmasduzjfqnukdpiwsqehmisbwceqgnbunvxjwipowlybdhxvxdcknwlkzrchefbrazdyjsmhfkkirjdrnidceoofgqmmvogxpjvabhiiusrncuerehtlykqgadswtavijrimasvwlmkpiqgpabaalqgovakobfymyjzbbuxmihdqalfanhaayiovkamnikagtzhvvhjdqnvqydsnkuqkcegpfucpeevaffxcoghevdvwgplskbdoglfnficlozlugiyurgbmjykrnwjzxoofztugdysuydogomdfsetdegwrcgrzwhhwabcgauaaaqiqelvzrqcvwzpyhgadpjbpkgxkaxmcpvsugptaixxewmffuhjjqmbcsypvybxnwshfjcfracwyrdelkpvcbweuutpuvoitgrysufjwkfubiymupjwrfdncweytsgpbaptwxcshkmkunypeinvpqktposkjybkarfwojoxtdhqsfhwpuufneaevsqetsqtjvsxggucldsdizcavwfichoxafbtxtogogfxnzzacrgmqimletwgbkgdpjwmdkutrzqgapicgorywfmcbileurhkadyfptzispqthzxppqomwcqzkbdgukqxprcgkbpethxaixpynfmlhcktgpaazszqlcxvfoaaxzagwsemzszjukeczgfbzetkisiqgkqgjtminswmkvvghajjgomhsfudyetgojmzeyhrsfecbbjkdutmifvclrflvarjmglqesizaobbrmlxghjometzwamtbefnkqfqkppkdtnxfbuoidewjxwhakbboiqayxtinktqdgplhjbrofoyfmhfwkgnsypqvizitubycqlkcmdqstqxfaeekmtfkixhtysostmvlahnmmgggwfnwjtjvmqhvnpqohegcqdpqmffzllfjruicotyajfxywnmfrvjkyzclghmtvtconmqbfqeowbpsrbaiwjuvixiqgwjbporcaiggakwwllrcprnlahilgsbnonqfbkibuqjuaitnvkskdfwfogsvzwkpjcvkmfngvzdvhwkcgcpljnsatlvuhhkqlfcakpihqlexhocptracgvczgzwnigfunjwzaegrqmqxaspvlrarmetsephovokkxgjalprbbhadcpbnhbhvfaolpxamokwntfnewehzojeqzffigmfmovxdtzrhmpufwiluoutedawehcooqucfpbkibcrptouqyhkobgteipjptxdkthrjjbtmflbzbxrzednfjiltaujtumfnwwwhasthfwigtzfzfueodpidmtyghevdcukemfmrbwxwwevbybrdrbgfuflclihpcswqxkhbggxemvflwzqpcxuzehdrqkgsecleosfvbeznbhayirnkqilupolhbtafynjmfqhixjwaqyyyroihywdpkqxlkztkmeytxgcwpawhyxfqlpzjldyytvjfwepijociweengauexbwkqwtcbuaurlaospybfajbgpqmpktplpzentiopilgvlwncvqkvbneqeqgqjvezwiopqfgaqnxdjlfgdreffivjydziadjxnzodevfukdxvqfctwgadoymmbowcthbhhpmlksiuvhslougnahqqffeitbmoinvrfifranoxwgklaqaczssgxwrszdhktcbymgpmvdjsltflmhpnzhuzgnrfqapjfrjrzbevgppsludzdtmccibivvqovfzayjuamyvspmkciqbllqnnaryyoqmjxnmwwgykgtdxfnanfdaqvngyggwuwigtvsruapegkjfpxheeneviubicjexfofymxqizfohqymhxuobjuytqzctkgqpvvohugrvnfcfdopakdctzanqcpjmxbeuyubuaupparvdhkeupipqkegovrdtuhnubrodlfslyppibvcsftjpyrgtljofqcatvqwiyquwglghiiapejeccmxnvmtnqvglnevlvrkbeqkmbkbfvijyuglssgfkdoxrstenkqqpjbdknhrjpahlisddzjncxlvrgchqszhdalnqsgzjigwraauzlhekubbafktykadmntchzbsijpzkrvlceroztrzycuyovcakvfswgkgszhcscpuhhigcchceedszhujczdaiohapocirreaapicrrfxviruplgtljvtzcvrtxbmqhmrwuvplamjkdfbrlwexsxyusrprubjcncajyqxaeglklobzlhydewzyqprkqcmgfnrdfoflwsvkhylsfjxlhwlxneighwomlfrqwwcupzeyypqfaprinehbjrjqoxezcvsarwvivbgvtybtnuddalgjcpbsofusamtuiocfrldklgebajeaukmzbnrptlhvzcpjsupkhsusyatakxcgjofkezbxmlsmnkvgemqlgmdgnzizwnfidnuhowgajzmwlkepyuchjhnygyxflepotjyhheisfwpqithhqjoztdxbbwioczdwjddshnlnmcduxlbnwrorvntyjdnmdskovpicdvrrxvlvinkegzybmtcywrmbjwpglakqvchvzvshicnqdluqgwqdnceyywglwqetunotigasjqjoddgkzwpoyvoyrumpkqjfdxamgdeptpdysmitixhjtvhmrtcclnjpmjdsmjjhzngrzqnjqwslucxlxbpjoyabkdvyofinuqhvgueyqxjkbjwyklhbmhewmzwbeeqyuxtdrabkxlwausyggghuplscnofrvvsptlsmlwykhvkbpjjxrrrgejkrapjvldmgofucbtokobnfmwddnuluewlglwbyzneoubsxughkjwpvtsyinkctiobvmcumracmbujxcthmrxjkrivguxbenczaevoywqkzmvxqqeeidouvypdupfyejxgqtuorkyqyvnpmutwxhqufgazxfzbqzigseulrubpqreelyakhqhpyhqvoqzepjljnhwecxuuqaabaaoisvztcpqqhpuyyhjmpfsrfonvpnzppnzhiycmqtcxiyyhghvxnnqscdntqmkhbkojkrxckbcuaadihyfuovosaclsqvzshpdugdwseapeasoittejqtbqxokpljjtzpphslcwordolryenfndaqwzegoqsaltpaajnefbxiqjcqnpvduvtquyzlotlbmabojotqsqbibdapuwsornholizbbkcpmdfvuynmrowstwjnudcmrlactbgwlinxosukthykwuersqfntjbmudrpexnphaovsihlrfxpbehuumjpxkctptitqvkxvavpicbbiarleyfamoqjaucpnmkfhueeubtegwgqxxbdxhejxwsaqwpfiamrwqvruqxandqmcrrzyviytcylapsipezmxwfrpctcijqkahmbfwbazzmzogkgnlskkzdzdwdlhtyhamkhilihkwjbcvhpibbscgrfcutjpttsfdznrjxbfiekdlblodgqjxwoupzjiudpadcrozuujzgmkhazkgrwfnmzelloioditgzihtersmfftfggnxctnqurdfilwltrtuzdofuirbnnjvtwtxrgnmzqthepvzhouiriqnqjpgwabpwwoqebcguxnankzwztgsdwgwixcexfwvemliqpomnemcolypfgikfognnktkqrhueteukvgzbsbpfbhmipxpfdcsovegnlctginrdvqenuwsvdffueuzhytxwxflijerstivoacbuavsfczzgwaqutpqsvdcehtyaduogyraypudrweauesozhhtekvlurjuuflabrmgmqtyxhfjrurkpcrelwzhroiuicilvxrjpkjmrovkjouaqnebjfjautxexhpsehdvrmhlbfvmtsomfsppzarvuozrwrmcypyrchefmctiuhwbblqcmkyiazbwqpbqhbkjioqxslhosdqvogxcsxmtxqppfsgmtqxegpdzakpunfpdmpiemwxlmpbsjhgfzelhtoiwyyqndisrzcylzxxloafyjmfisqrngajgactdknvjqvwrsvehvkheyooqegdkipsirnnbakmsfijyeohbyqgyewoketumimwzbkcbuouczfcftjgtzorflhprdlglzcnaorblgxnhdrmyausblliwvxpyivljayjoqmbykqhphvnjphmatuyqrooblzklatcsgfsswzhfuwpledozyopreftqeddgzfyhlqzjriongfzmjpnjdeakjtcqzfwylxhypihhsxuyfvnomaxqfxcqtegsjfswezuthdczbzzgumwhpvzuubmnhtfqazpeyjxhpcgsbiavuyejtdfngsdnnkgpkvtigsqxuypvgrtdpxoidwylqbzdnhsxengmfykcwbxftqiioyttutekwfpjmjhqwnfenpglqdqjwaumbnfvgjicrxldjswfhblwsriixauvdohedozjzjnqjawsvszevlbnejxdlryofhsivutxfgnojjgedgiatjpxunbgebwmjrwgnsdsathjepnivwkqhaocprktuihdzgmoyrhykqkphxzfvlvfljjacvwxdfcflotlicksuwjcvihrucyhohiscgphlumzkikskwlhswjofshbwfkmosfsawboqondyxvkuirofcemulntsxfismaujeibsvesvccpkufpykdvxsoqqvakidgthpwbmdthfvyrrejqomnlfbdxyejghpbqearrdkaihzbzdkrtxegehmbfqmozbpripibusbezagafqtypzhtgtwmlickmtbullvfdykezshekcfacmvifuwqcycosfkdqfkvgwbfoklznqbpewzjqwbvwdlqkwvcdgxjcborlcsautpzrriinmflpqccmxeqfezifqbssvtooknfbypqkucbngdzfirlmtvtjyldtgrjrhosfglrcnspvyraginubkpmiardjlmasduzjfqnukdpiwsqehmisbwceqgnbunvxjwipowlybdhxvxdcknwlkzrchefbrazdyjsmhfkkirjdrnidceoofgqmmvogxpjvabhiiusrncuerehtlykqgadswtavijrimasvwlmkpiqgpabaalqgovakobfymyjzbbuxmihdqalfanhaayiovkamnikagtzhvvhjdqnvqydsnkuqkcegpfucpeevaffxcoghevdvwgplskbdoglfnficlozlugiyurgbmjykrnwjzxoofztugdysuydogomdfsetdegwrcgrzwhhwabcgauaaaqiqelvzrqcvwzpyhgadpjbpkgxkaxmcpvsugptaixxewmffuhjjqmbcsypvybxnwshfjcfracwyrdelkpvcbweuutpuvoitgrysufjwkfubiymupjwrfdncweytsgpbaptwxcshkmkunypeinvpqktposkjybkarfwojoxtdhqsfhwpuufneaevsqetsqtjvsxggucldsdizcavwfichoxafbtxtogogfxnzzacrgmqimletwgbkgdpjwmdkutrzqgapicgorywfmcbileurhkadyfptzispqthzxppqomwcqzkbdgukqxprcgkbpethxaixpynfmlhcktgpaazszqlcxvfoaaxzagwsemzszjukeczgfbzetkisiqgkqgjtminswmkvvghajjgomhsfudyetgojmzeyhrsfecbbjkdutmifvclrflvarjmglqesizaobbrmlxghjometzwamtbefnkqfqkppkdtnxfbuoidewjxwhakbboiqayxtinktqdgplhjbrofoyfmhfwkgnsypqvizitubycqlkcmdqstqxfaeekmtfkixhtysostmvlahnmmgggwfnwjtjvmqhvnpqohegcqdpqmffzllfjruicotyajfxywnmfrvjkyzclghmtvtconmqbfqeowbpsrbaiwjuvixiqgwjbporcaiggakwwllrcprnlahilgsbnonqfbkibuqjuaitnvkskdfwfogsvzwkpjcvkmfngvzdvhwkcgcpljnsatlvuhhkqlfcakpihqlexhocptracgvczgzwnigfunjwzaegrqmqxaspvlrarmetsephovokkxgjalprbbhadcpbnhbhvfaolpxamokwntfnewehzojeqzffigmfmovxdtzrhmpufwiluoutedawehcooqucfpbkibcrptouqyhkobgteipjptxdkthrjjbtmflbzbxrzednfjiltaujtumfnwwwhasthfwigtzfzfueodpidmtyghevdcukemfmrbwxwwevbybrdrbgfuflclihpcswqxkhbggxemvflwzqpcxuzehdrqkgsecleosfvbeznbhayirnkqilupolhbtafynjmfqhixjwaqyyyroihywdpkqxlkztkmeytxgcwpawhyxfqlpzjldyytvjfwepijociweengauexbwkqwtcbuaurlaospybfajbgpqmpktplpzentiopilgvlwncvqkvbneqeqgqjvezwiopqfgaqnxdjlfgdreffivjydziadjxnzodevfukdxvqfctwgadoymmbowcthbhhpmlksiuvhslougnahqqffeitbmoinvrfifranoxwgklaqaczssgxwrszdhktcbymgpmvdjsltflmhpnzhuzgnrfqapjfrjrzbevgppsludzdtmccibivvqovfzayjuamyvspmkciqbllqnnaryyoqmjxnmwwgykgtdxfnanfdaqvngyggwuwigtvsruapegkjfpxheeneviubicjexfofymxqizfohqymhxuobjuytqzctkgqpvvohugrvnfcfdopakdctzanqcpjmxbeuyubuaupparvdhkeupipqkegovrdtuhnubrodlfslyppibvcsftjpyrgtljofqcatvqwiyquwglghiiapejeccmxnvmtnqvglnevlvrkbeqkmbkbfvijyuglssgfkdoxrstenkqqpjbdknhrjpahlisddzjncxlvrgchqszhdalnqsgzjigwraauzlhekubbafktykadmntchzbsijpzkrvlceroztrzycuyovcakvfswgkgszhcscpuhhigcchceedszhujczdaiohapocirreaapicrrfxviruplgtljvtzcvrtxbmqhmrwuvplamjkdfbrlwexsxyusrprubjcncajyqxaeglklobzlhydewzyqprkqcmgfnrdfoflwsvkhylsfjxlhwlxneighwomlfrqwwcupzeyypqfaprinehbjrjqoxezcvsarwvivbgvtybtnuddalgjcpbsofusamtuiocfrldklgebajeaukmzbnrptlhvzcpjsupkhsusyatakxcgjofkezbxmlsmnkvgemqlgmdgnzizwnfidnuhowgajzmwlkepyuchjhnygyxflepotjyhheisfwpqithhqjoztdxbbwioczdwjddshnlnmcduxlbnwrorvntyjdnmdskovpicdvrrxvlvinkegzybmtcywrmbjwpglakqvchvzvshicnqdluqgwqdnceyywglwqetunotigasjqjoddgkzwpoyvoyrumpkqjfdxamgdeptpdysmitixhjtvhmrtcclnjpmjdsmjjhzngrzqnjqwslucxlxbpjoyabkdvyofinuqhvgueyqxjkbjwyklhbmhewmzwbeeqyuxtdrabkxlwausyggghuplscnofrvvsptlsmlwykhvkbpjjxrrrgejkrapjvldmgofucbtokobnfmwddnuluewlglwbyzneoubsxughkjwpvtsyinkctiobvmcumracmbujxcthmrxjkrivguxbenczaevoywqkzmvxqqeeidouvypdupfyejxgqtuorkyqyvnpmutwxhqufgazxfzbqzigseulrubpqreelyakhqhpyhqvoqzepjljnhwecxuuqaabaaoisvztcpqqhpuyyhjmpfsrfonvpnzppnzhiycmqtcxiyyhghvxnnqscdntqmkhbkojkrxckbcuaadihyfuovosaclsqvzshpdugdwseapeasoittejqtbqxokpljjtzpphslcwordolryenfndaqwzegoqsaltpaajnefbxiqjcqnpvduvtquyzlotlbmabojotqsqbibdapuwsornholizbbkcpmdfvuynmrowstwjnudcmrlactbgwlinxosukthykwuersqfntjbmudrpexnphaovsihlrfxpbehuumjpxkctptitqvkxvavpicbbiarleyfamoqjaucpnmkfhueeubtegwgqxxbdxhejxwsaqwpfiamrwqvruqxandqmcrrzyviytcylapsipezmxwfrpctcijqkahmbfwbazzmzogkgnlskkzdzdwdlhtyhamkhilihkwjbcvhpibbscgrfcutjpttsfdznrjxbfiekdlblodgqjxwoupzjiudpadcrozuujzgmkhazkgrwfnmzelloioditgzihtersmfftfggnxctnqurdfilwltrtuzdofuirbnnjvtwtxrgnmzqthepvzhouiriqnqjpgwabpwwoqebcguxnankzwztgsdwgwixcexfwvemliqpomnemcolypfgikfognnktkqrhueteukvgzbsbpfbhmipxpfdcsovegnlctginrdvqenuwsvdffueuzhytxwxflijerstivoacbuavsfczzgwaqutpqsvdcehtyaduogyraypudrweauesozhhtekvlurjuufla")
    # print s.repeatedSubstringPattern("abaababaab")
    # print s.repeatedSubstringPattern("abaabaa")
    # print s.repeatedSubstringPattern("ababba")
    # print s.repeatedSubstringPattern("abab")
    # print s.repeatedSubstringPattern("aba")
    # print s.repeatedSubstringPattern("abcabcabcabc")
    # print s.repeatedSubstringPattern("abcdefghijhj")

    # print s.repeatedSubstringPattern("a"*9239+"b")
