# coding=utf-8
#
# @lc app=leetcode id=402 lang=python
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (26.97%)
# Likes:    1059
# Dislikes: 66
# Total Accepted:    69.4K
# Total Submissions: 257.5K
# Testcase Example:  '"1432219"\n3'
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
# 
# 
# Note:
# 
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# 
# 
# 
# 
# Example 1:
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# 
# 
# 
# Example 2:
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
# 
# 
# 
# Example 3:
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
# 
# 
#


class Solution(object):
    def _removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # O(3n)
        if len(num) <= k:
            return '0'
        elif k <= 0:
            return num
        count = 0
        index = 0
        new_num = ''
        # 第一轮，从前往后，删掉前面的较大值
        while index < len(num):
            if index + 1 < len(num) and int(num[index]) > int(num[index+1]):
                index += 1
                count += 1
                while new_num and count < k and num[index] == '0':
                    new_num = new_num[:-1]
                    count += 1
                while not new_num and index < len(num) and num[index] == '0':
                    index += 1
                if not new_num and index == len(num):
                    return '0'
                if count == k:
                    new_num += num[index:]
                    return new_num if new_num else '0'
            else:
                new_num += num[index]
                index += 1
        return new_num[:count-k]
        # 其实后面的两个，就直接截断就好了

        # 第二轮，从后往前，删掉后面的较大值

        # 第三轮，从后往前，删掉后面的值

    def __removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 思路是这么个思路
        # 从前往后
        # 删掉小的
        # 然后保留
        # 使用栈保留剩余的数字
        stack = []
        count = 0
        i = 0
        while i < len(num):
            if i+1 < len(num) and num[i] > num[i+1]:
                count += 1
                if count == k:
                    stack.extend(list(num[i+1:]))
                    break
                i += 1
                while stack and stack[-1] > num[i]:
                    stack.pop()
                    count += 1
                    if count == k:
                        stack.extend(list(num[i:]))
                        i = len(num)
                        break
            else:
                stack.append(num[i])
                i += 1
        while stack and stack[0] == '0':
            stack.pop(0)
        if not stack:
            return '0'

        return ''.join(stack[:count-k]) or '0' if count < k else ''.join(stack)

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 单调栈不应该如此丑陋
        stack = []
        for n in num:
            while stack and stack[-1] > n and k:
                k -= 1
                stack.pop()
                continue
            else:
                stack.append(n)
        if not stack:
            return '0'
        while stack and stack[0] == '0':
            stack.pop(0)
        if not stack:
            return '0'
        while stack and k:
            k -= 1
            stack.pop()
        if not stack:
            return '0'
        return ''.join(stack)


# if __name__ == '__main__':
#     s = Solution()
#     print s.removeKdigits('112', 1)
#     print s.removeKdigits('13337951184242971097189412735925105562812864769529571420601766793856899905960695634828338144367793036733743527259998286784390554887381591483147365254442476273280225311236269414851296894307373153115645836921708264522198512776561438078038307560190200756196035316245673282180956667392815450469593948460623891023733836848495454368701913582051402794417850573113581852179757992342053662072093962298297371586326589927903277687591842114732295531039032346646829614293323488581206504472317662409530922119787693724845719021781708977705437400581372234574089668947514726211680300624621636152098785823532797835511272157360646965803060818113902017781014662029565708940807240692853892606933404142134456877003504335785685250203869590656208852797813261014836103165061712762783383677781676780730433133620050364272931789761074343574658538004271964782130623774178875146908079822974813915675972053774027091780913955583727538379044131602965790950799862466969095157950205052556294892863965710901305201030655056827641839147714614912560099606211437216797442052943983187569048557049811328157311842159222503138182467897856388489889561006664030062931609563097220075725473672845223879404587973634012932912396387947048562801923873331406000027029451247063763592403992941509209538696312946547386595712892536675900011006317676737217472034052768879740999219437827980648402619917726447746980572337446924475354447412479355475723804713545466609501677123711665311883555078032151313536958022681106841186365414001156126151315040983118541753455880910680163939843060055651380215951070495847328465316238733771852532395281221908902799585298188053159198649566561068075255849789339630492247519959464748674931140106560127351885051763041657710780028913027285396982619731871993941755570097145824819617467648502550312753597883310812257879778870206257221439943259638642810267701014103599796361181464462686614111557516829237968225022703319352555395582359262279260258075048868255989840583012767526099949295221999208723259463558359849267506031870651966753461043186525026228948333137501466867954250559182962290338500942446557866297594628573685939793556590370448882202803440235979397729162044595051909213684568864331441918250979582922819705149521243322196013214331405118816016371644270002909673903421971723620772211907976052705573682968646577316098770963374023307273931694843629388305041455728082486468532954457676723882285383670063017471448066652193634408717817865187577085846281712238571779333851444178229096998688170320026039138448385719180838915788767106323597933594246115007563925982864866957782605147224303695250063485912240048553587853862645665741470110181001299608578616530808228811313582199922126437885572545438187314959921495557418604345633020075723170423270928651285094305681120843754318794189896206764855170268851896269725594161196466908910479492718802124132492661143480265129233931886992474346386650832591909501030042299286796642463614512471074910107323642774376394561463815339139932266649122586921993422156634587659409750477533213243697567744042077701485085025631616350599384318051113985864663189080503974102024324192869016153180441637569321610043050835320179100369996434309053695549953337507714016417315885768348108176257982553677919485917169637998327012703900581204668466090580804554631222421249777545638138441782894436431213007536400039981357644748199678108979273939704392031368715168203326275180598527380216501731323405944174190702220994883037466313627755511623398084785523903578312138509832494105953156767300077617479120300160510880506233680299413214660798759957914609976601021090553614267711914495267879491002661790522026084214420379356890444449756745567180436300269646782554184171278700730860850456466960958946800570764172507319392851144076137688438540342611956940455300971277852812603527622692112078496365205618230794857086766325321990886784865651969476657489356058822926777909014046002565032405774210277172606498625669515546801283246966427966029732325350911982507610397795266089328299898961978558383128059684890909166148817260321389460806885319060295382504958423308749851867932327323341657975241076252669986752131551927760723890375191999276825416580799128173344982083723371014271641090802159655357647257664509967879111430127968377164385442371832647746815454821712881330639780213141153326711447230425451921683523242698875774468730792213125325502073040540708165676727083385429762715425629470761696786661205568790090190500420964440936719117206233758802326315515752160425730775305676521250214245059894080444080859213805425786796331148739728805318556965319929633098792683151831781650411901864016630100378981415892677561951557931229419247561108437308601901043172743828169333047486596568598824769816806267200810697936807986720713008496684087014362337888140206185858274300353777746284388801370127867319827525598685900791131129744835737213704334463506576261950687480855806223028988493685312942092751272015323469627639644414519380137165089808872807839314810304536632163859668249060695912691558666738565197728632788223619547770293089249348846217576455153597240851537384832371283537664577790617857409063003250307125289051265956136862998578529207473019434155018380032677981049030334119560609950262872499073502825352087824278928252116649032948945767791220431318396897861377482982427788274861661020400092418844794634813258619700297068768450743731633110307618155709216866679928229684478461384030857857232464128233907798301319354667484198625744238256702583253504650274687550813430041994565238424493047933948335662535507527187312534065502617258026936826518004279192471258841525062929942888348949744657882632368213938698641232824082822152147667041659132978686369701052270470354222141249951731191165837901963214337523631827303437960393792922481491820447405081628139161933474748840611650227955754672155255018119313031587751345821721399791217154046480616854166478513104698056954209395305137959475078835163316916981183265995687575607217811870617812429193526983736024339054714475135530213690784359800871615177829400181862505662407488802833906404621696654965966135994609338536672534209860023877657138545179743054680830355763229545321160269706474204390272554783564155367753166925661733426237084455614358076595096317786722042918270675534001535383183199769773351988887573795677656510661174514807181534607883632266553332509179050723950658020199902115655109920362755486557267378927494537308498349915910815183116577685368045389123977482931960807346045191831371844684701324710724744702493423344603576070545936211835200740151187724097153969121901991532748991300789102136338162179794582669550908921768036668388233604782468874449412041722070309685375422045154952156210633920530382639567687172488115237033851332486936645770371430533757113814227901662372414158753862113926674097124177196999062111351353460093538720498722945722732109244649166915273950760536104878856344272140698386851192554863544316188784904325936088627019100654511578137233893273262893901584732549619508191685235370551549499204575753512377958786239175966650204954946243366955059955738010742198345099075810166488021719753895045591259903692091611666645841120040034803882737452826597418984810948351748923722429278546287873070431028033856538788683485080061759301030551731618969484634153878185478664226646158981797520887140674205704059590288360996982038761044913174976659892124512588167213123812193865618200216007796972903552424311376372337610456325745813512896412141483684763939114197088488956448955734287559747645748105269521281437637886010729014713530169999723227638651848596430465750752760513686817577524809202760092513125030480833684082194434595336502527738584939852443388723355169182822361471622394199948786200481684323960148425648143580588312789213143850790404278048136044749347193712594556881054205625233282104365676200913129116758905378158457050434136470240189921778321037463288726147886007022008096852325675017175447323103986023470922520392481086672447307843099764386837466735698918087547670808425379258014339545816788209885121637187612547400993641047765777490808501555142829338795568145057673344351772995855613227888921639080498625109919346967272551662935669841565072810628551441941512397964147742689949671463940932963067805331618080103485947518290522843833135852845112547626437022868530329797205723279542208163716079677554578830813507130072752751388484835295821400704242337880912281080041214057207152516957853141502050999485887136933079127988975647810564543454794843660457394868397264707298908873553304891849864968274479439623112657005785285465478339213823301972059606109858962689127486315504419304069297663039865009989891757995655832157024539998067327630778015169573462084412621818870812736954027840007688782622001025876200340214520110044858863420655177003426425109595245244887681107516180304771837913357051091497389621159860422692221517041745797274138654030671575546168890863217609944764553648904718351933433047594014932000639972786743676635637342172547134620763156242732474064897238349285715901678989378661735295376129979026200830063103349803851549260452104065207206376937891630680438543684845766712523488226814146933423799560818758788853692895336959710196776037533467241100113607979137143212615857621379650334484877297107467197874263649042652503590128877581927397063691130393251901363573542401779857162058281509913815748919063242434704410260458820136565091086617303750370267371398077180818971601065024208246383193186175191294188810114807614174079298225286855837995559035224970869005166351382287076172986021167829423715148449434231843455408577464847015859163471441708088251226013675381920393756252048999211966315091322376483289717609663372654570378504792306325556347936003349053236178934687268783020258374697611996142610350623550413286234710993464598436824558248893752798030030286296080336057875030836484156041063489545712994824690188653271133189965963959668968605301768860765791058453824391574272258251460300704593243008831580326059208102171408441053814462591910748413998157272997866794867847628994533692632257171339423438040287822039716071509619784044053321241001172519946917107197380032900093', 111)
#     print s.removeKdigits('9', 1)
#     print s.removeKdigits("1234567890", 9)
#     print s.removeKdigits('10', 1)
#     print s.removeKdigits("13431342", 3)
#     print s.removeKdigits("13431342", 5)
#     print s.removeKdigits("13431342", 1)
#     print s.removeKdigits("12345", 2)
#     print s.removeKdigits("12345", 3)
#     print s.removeKdigits("1432219", 3)
#     print s.removeKdigits("10200", 1)
#     print s.removeKdigits("10", 2)
