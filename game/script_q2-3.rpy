label q2_3:
    window hide
    scene bg_cut3 at cg0 with Dissolve(3)
    pause
    scene bg_liroom0 with fade
    window show
    show qianimg black close at char_left with dissolve
    qian_speaking "啊……啊嚏！"
    hide qianimg
    show qianimg black o at char_left
    qian_speaking "呃，对不起……你这么看我干什么？"
    show liimg black o at char_right with easeinright
    li_speaking "你啊，没感觉不舒服吗？头不疼不晕？"
    hide qianimg
    show qianimg black shock at char_left
    qian_speaking "什么意思？怎么了……啊？？！！"
    qian "我震惊地看着镜子前倒映出来的景象——我的脸——连我自己都几乎认不出来了。\n这些瘢痕和肿胀是怎么回事啊……好恶心……"
    li_speaking "没事，你这是被污染了，前几天估计还没习惯，过段时间习惯了就好。"
    qian_speaking "……\n为什么你这么平常地说这个？这不是很危险吗？我会不会生病啊？我是不是要死了？我——"
    li_speaking "停停停，你差不多了啊。\n这就是很平常，只是你没经历过这里的环境而已。我看你也不痛，别去在意就行了。"
    qian_speaking "……被你说完，突然觉得有点痛了。"
    li_speaking "忍着，过几天就好了。"
    hide qianimg
    show qianimg black at char_left
    qian_speaking "那我说痛不痛有什么区别……"
    hide liimg
    show liimg black at char_right
    li_speaking "嗯，区别在于，如果你快痛死了，我会给你搞点药什么的。"
    hide qianimg
    show qianimg black close at char_left
    qian_speaking "那我现在就痛死了！"
    hide liimg
    show liimg black ask at char_right
    li_speaking "真的？你看起来很有精力啊。"
    hide qianimg
    show qianimg black close at char_left
    qian_speaking "才不是——啊……"
    hide qianimg
    show qianimg black o at char_left
    hide liimg
    show liimg black at char_mid with dissolve
    qian "我正要继续说的时候，黎沙突然转过身，手指尖贴上了我的脸。"
    qian "凉凉的……"
    hide liimg
    show liimg black o at char_mid with dissolve
    li_speaking "行了吧？别叫了。"
    hide qianimg
    show qianimg black at char_left
    qian_speaking "呃，好……谢谢你。"
    li_speaking "你是想待在这收拾还是跟我出去？"
    qian_speaking "……嗯？"
    li_speaking "干活啊，你不会想着什么都不做吧。"
    qian_speaking "只是确认一下……我知道啦……"
    qian "我——"
    menu:
        "【出门】":
            jump q2_3_01
        "【不出门】":
            jump q2_3_02


label q2_3_01:
    hide qianimg
    show qianimg black o at char_left
    qian_speaking "我也去看看吧……"
    hide liimg
    show liimg at char_mid with dissolve
    li_speaking "好，至少你也要多了解一些东西才能在这活下来。"
    hide qianimg
    show qianimg black still at char_left
    qian_speaking "嗯……"
    qian "她理所当然的语气让我感到酸涩，因为我无法反驳——我将会留在这个地方，再也无法回去了。\n我明明，只是想过普通平常的生活，和家人一起……仅此而已。"
    scene bg_workplace with fade
    show qianimg coat close at char_mid with dissolve
    qian_speaking "咳，咳咳咳……咳啊——谢谢……"
    qian "我伏在墙边，仿佛要把肺都咳出来，仍然聊胜于无。四肢已经累得发软，这几下剧烈的咳嗽差点让我直接跪在地上，好在黎沙勉强扶住了我。"
    show liimg at char_right with dissolve
    li_speaking "你也太弱了吧，也没做什么。"
    qian_speaking "咳……我又没接触过这些！"
    hide liimg
    show liimg laugh at char_right 
    li_speaking "也是，感觉怎么样？是你们特别想过的那种城外生活吗？"
    
    scene bg_workplace with Fade(0.1,0.1,0.1)
    qian_speaking "我……咳，咳咳……\n……"
    show blur with vpunch
    qian "难以控制，我咳出的眼泪顺着脸颊落到地上，把视野染得模糊一片，只剩虚晃的黎沙和她那毫无温度的笑脸，也在此刻随着尘土一层一层地落下来。"
    qian "即使在洞口，也能听到坑洞里传来的机器工作的声音。\n这里没日没夜地产出晶矿石，是这个时代最重要的能量资源。但……"
    hide blur
    show qianimg coat sad at char_left with dissolve
    qian_speaking "荆棘之城的能源，都是城外供应的吗？"
    show liimg at char_mid with dissolve
    li_speaking "嗯，是啊。"
    hide qianimg
    show qianimg coat still at char_left
    qian_speaking "……可是，那为什么……既然资源在外面，为什么要直接给城里……"
    hide liimg
    show liimg close at char_mid
    li_speaking "也没办法啊。你看这里的环境……人都被逼得半死不活的，科技也没有多少发展，真要抢起来，怎么打得过。"
    qian_speaking "……是吗。"
    hide liimg
    show liimg smile at char_mid
    li_speaking "像现在这样，你们那的人给点好处，外面都要争着去抢机会呢。"
    hide liimg
    show liimg o at char_right with dissolve
    li_speaking "就算资源在这，还是被城里的人给守着。得要他们允许了其他人才能进去，费老大力气生产完的晶体石还得低价交给他们——啊，你能重复一遍刚刚的话吗？"
    unknown "噢，你还不知道吗？‘那边’又要来招人了，快去看看呗，听说这一次要的人特别多，说不定你跟我这种的也可以呢。"
    hide liimg
    show liimg still at char_right
    li_speaking "……\n我知道了，谢谢。"
    hide qianimg
    show qianimg coat sad at char_left
    qian_speaking "那个……怎么了？"
    qian "黎沙突兀地终止和我的话题，打断旁边人的话。而后，她皱了皱眉，表情变得有些奇怪。"
    li_speaking "我去看看。"
    hide qianimg
    show qianimg coat still at char_left
    hide liimg with easeoutright
    qian "她言简意赅，没有多说就转身离开。我……"
    menu:
        "【跟上去】":
            jump q2_3_1
        "【留在原地】":
            jump q2_3_2

label q2_3_2: # ending here
    qian "想到她刚才的表情，我突然有点不敢跟过去。说到底，她一直也不待见我，现在也许没有继续跟着的必要吧……"
    hide qianimg
    show qianimg black still at char_left with dissolve
    qian "更何况，我的身体还痛得受不了……现在，连身上的斗篷我都嫌重，我干脆找了个角落蹲下来，解开扣子，不断调整自己的呼吸。"
    qian "呼……哈啊……也许是我真的累过头了，在这种地方，我竟然有种昏睡的预感……"
    hide qianimg
    show qianimg black closecalm at char_left
    qian "就休息一下吧……"

    scene bg_workplace with fade
    show dark with dissolve
    unknown "……喂！……你……听得到吗！！……这里……！"
    qian_speaking "呃……"
    qian "发生什么了……头好晕……睁不开眼睛……"
    unknown "……还可以……试试……醒醒！！……"
    show blur with hpunch
    qian "好吵啊……烦死了……好累……"
    unknown "不行……喂……有人……"
    qian "算了……不理会就好……"
    qian "经过我的努力，声音似乎越来越小了。"
    qian "太好了……就这样吧……"
    scene bg_black with fade
    qian "我放下心来，安心享受无边的黑暗……"
    qian "……"


    # 【Ending：噩梦】
    window hide
    show screen ending_title(number=16) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[16] = 1

    return


label q2_3_02: # ending here
    scene bg_liroom0 with Fade(0.1,0.1,0.1)
    show qianimg black o at char_left with dissolve
    qian_speaking "我就，先待在这里吧……"
    show liimg o at char_right with dissolve
    li_speaking "好吧。\n别乱跑，把东西都收一收。"
    hide qianimg
    show qianimg black at char_left 
    qian_speaking "嗯。"

    scene bg_liroom0 with fade
    show qianimg black at char_mid with fade
    qian "我有些百无聊赖地坐在地上，习惯性地伸向手腕的地方，但那里已经没有终端的存在。\n对哦，之前被黎沙拿走了……"
    hide qianimg
    show qianimg black closecalm at char_mid
    qian "不过，就算现在拿回来也没什么用……毕竟我已经，不在荆棘之城了。"
    hide qianimg
    show qianimg black at char_mid
    qian "我有些茫然地看向远处，笼罩在漂浮颗粒中的一切都让我感到无比陌生。"
    qian "但从此之后，我就要在这里生活了是吗……\n回不去了……是吗？"

    scene bg_black with fade
    unknown "时茜？怎么了？时茜？快过来……\n时茜，小心——！"
    
    scene bg_liroom0 with fade
    show dark 
    qian_speaking "啊……！！"
    qian_speaking "……\n……原来是梦啊。"
    qian "气势汹涌的尘沙太过真实，我几乎以为自己下一秒就要被淹没……原来我还是没能摆脱当时的恐惧。\n那时候，近在咫尺的风暴就盘旋在头顶，离接触只有一墙之隔……"
    show liimg black still at char_right with easeinright
    li_speaking "吵什么？"
    show qianimg o at char_left with dissolve
    qian_speaking "啊……！\n我把你吵醒了吗……对不起……"
    li_speaking "不然呢？"
    qian_speaking "对不起……"
    hide liimg
    show liimg black closeask at char_right
    li_speaking "……啧。烦死了。"
    qian_speaking "……"
    hide liimg
    show liimg black close at char_right
    li_speaking "唉……"
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "……你很不开心吗？"
    hide liimg
    show liimg black at char_right
    li_speaking "无缘无故被吵醒，很难会开心起来吧。"
    qian_speaking "对不起……我的意思是，别的事情……\n你今天好像是因为有些事情在烦恼吧？"
    li_speaking "……\n跟你没关系。\n别想那么多，赶紧睡吧。"
    qian_speaking "嗯……也，也是啊。"
    qian "我说不上是什么心情。\n黎沙对我仁至义尽，但我知道我从未得到过她的信任，也从未有机会了解过她的真实想法。"
    qian "想来也是理所应当吧……"
    hide liimg
    show liimg black o at char_right
    li_speaking "……\n我知道，你对这个地方很不习惯，又破又乱，比不上你们那。"
    li_speaking "但你也只能慢慢习惯啰？我可没有精力每天开导你。"
    hide qianimg
    show qianimg still at char_left
    qian_speaking "嗯，我知道……"
    li_speaking "总之，你就加油活下去吧。"
    qian "我不由得撇过头——我知道，薄薄的墙外侧，是那片一望无际，充满未知与风险的沙暴之地。"
    scene bg_sand0 with fade
    show dark with dissolve
    qian "从今以后……我的生活将会在这个地方……在这里活下去。"
    
    # 【Ending：空荡】
    window hide
    show screen ending_title(number=15) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[15] = 1
    return 




label q2_3_1:
    hide qianimg
    show qianimg coat shock at char_left
    qian_speaking "……等等！我也……去！"
    hide qianimg with easeoutright
    qian "我思考一瞬，还是拖着沉重的身体——衣服太重，我一度想要脱掉披风——只能努力跟上黎沙的脚步"
    qian "就算她很讨厌我也好，她已经帮了我这么多，我更应该主动去适应这里。毕竟……现在我也只能这样了。"
    
    scene bg_sand2 with fade
    qian "人声鼎沸，掀起大量尘土，即使捂着嘴也差点让我再次咳嗽起来。我艰难地在睁开的小缝隙中捕捉周围的景象，好在有斗篷遮掩，没人注意到我动作扭曲。"
    qian_speaking "喂，怎么……这么……多人……啊……"
    li_speaking "小点声……看着就好……"
    qian "那是什么意思？\n我努力仰起头，什么都看不见，但耳畔仿佛捕捉到熟悉的声音，在人群的嘈杂中格外显眼。"
    qian "是荆棘之城飞行器的声音……！"

    scene bg_tall1 with fade
    qian "我这才注意到，在远处的某个方向，竟然能看到那仿佛直入云霄的高高影子。它与周围格格不入，在尘沙间屹立。"
    show crowd with dissolve
    show dark with dissolve
    unknown "这次我家小孩有机会吗？又好看又乖，还很年轻的！"
    unknown "听说这次放开了要人，只要差不多的都能进，是真的吗？"
    unknown "慢慢来啊，都听见没？慢慢来！"
    hide crowd
    show qianimg coat close at char_mid with hpunch
    qian_speaking "……咳咳……这都什么啊……呃啊……！"
    qian "周围说的话我都听不懂，愈发焦急，只想看清到底发生了什么。然而人群突然骚动起来，差点把我撞倒。好在黎沙眼疾手快，捞了我一把。"
    show liimg still at char_right with dissolve
    qian "她的脸上带着明显的厌恶表情，令我胆战心惊。"
    scene bg_sand2 with fade
    show crowd with dissolve
    unknown "真的，是真的！直接去那边排队就行！"
    unknown "太好了，太好了……感谢你们，啊啊……！感谢，感谢啊！"
    unknown "后面的别挤了！慢慢来！！！"
    qian "四周都传来起伏的声响，我惊异地发现许多人正朝着同一个方向一边吼一边笑，更有人直接向着那处跪了下来。只是太多人挡着，我看不清那边到底是什么。"
    qian "……好难受，不知为何，一股反胃感直冲我的脑门，让我差点忍不住想要大声呼喊。"
    li_speaking "小心点。"
    qian "黎沙的声音压得很低，从身后传来，她帮我掖住了差点被我拉得下滑的斗篷，也给我的身体来了点降温。"
    qian_speaking "嗯……这是……"
    li_speaking "去另一边说。"
    window hide
    show cg_li30 at cg0 with dissolve
    pause(1.5)
    window show
    qian_speaking "……你是说……荆棘之城向外招募居民？还要挑选？只有符合资格的才能进？怎么可能，太奇怪了，我从来都没听说过啊……！"
    li_speaking "是啊，这就是问题。"
    qian_speaking "去了城里的人没有一个再回来过，只有信件，后来也越来越少，最后都没了消息。更何况她们收了多少人？我数都数不清，而你连听都没听说过……"
    qian_speaking "真的太奇怪了……但是你说那么多人，你们就没人怀疑过吗？没人去问过吗？反而还争着去抢资格？"
    qian "我大声质疑——想到刚才的景象，我就有点控制不住自己的声音。好在黎沙一下挽过我的肩膀，装作我们在打闹的样子。"
    li_speaking "你啊……还好是过来说话，这话让别人听见，谁都知道你绝对不是外面的人。"
    scene bg_sand2 with vpunch
    qian_speaking "啊，怎么会……呃，唔……"
    li_speaking "她们……你怎么了？"
    qian_speaking "好，晕……痛……"
    show blur with vpunch
    qian "不知道是不是刚才情绪激烈，我的脑袋突然一阵眩晕。紧接着，淡淡的刺痛传来，疲惫的身体更加沉重。要站不稳了……"
    show liimg ask at char_mid with hpunch
    li_speaking "喂……你还好吗？喂！"
    show blur with vpunch
    qian_speaking "呃……呜……"
    show bg_transparent with shake
    qian "眼前是剧烈摇晃的黎沙，身影逐渐越来越远……"

    scene bg_liroom0 with fade
    show bg_transparent with dissolve
    qian "哈……哈啊……！！\n……啊……"
    qian "等等，好奇怪……怎么有点模糊……嗯……？"
    li_speaking "还疼吗？"
    qian_speaking "什么？还好……啊，黎沙……！我之前怎么了？你又帮了我吗……谢谢你……"
    li_speaking "……"
    li_speaking "给你。"
    qian_speaking "啊？这……这是……！！"
    qian "我震惊地看着面前有些颤抖的镜子，好一会才重新聚焦。上面映着我的脸，没错……但为什么是这样……"
    window hide
    show cg_qian20 at cg0 with dissolve
    pause(2)
    window show
    li_speaking "你……是我不好。你本来就还没习惯这里，又那么娇弱，我不该带你去污染最严重的地方。"
    qian_speaking "我没有娇弱……不，所以我这是，污染……？"
    qian "面颊还有些烧灼般的疼痛，我后知后觉感到恐惧——与死亡擦肩而过的恐惧。"
    li_speaking "……你能捡回一条命，确实不算娇弱。\n现在污染越来越严重，荆棘之城就是最大的污染源。平时的防护只能做到基础，什么时候影响到器官，也只是时间和概率问题。"
    qian_speaking "……"
    li_speaking "抱歉。"
    qian_speaking "不你怎么需要道歉！\n……是我……想得太简单了，也没有注意这些。"
    li_speaking "……"
    qian "气氛一时有些凝滞和尴尬，我得想个话题出来打破这个状态……对了……"
    scene bg_liroom0 with fade
    show qianimg black still mask at char_left with easeinleft
    qian_speaking "那个……我晕倒之前我们说的，你还记得吗？"
    show liimg black at char_right with easeinright
    li_speaking "你的大声质疑？"
    hide qianimg
    show qianimg black mask at char_left
    qian_speaking "……重点是说的内容。\n这种事情……到底是怎么坚持下来的……"
    hide liimg
    show liimg black ask at char_right 
    li_speaking "哦……是啊。\n有信件已经很好了，就算没有，大家也会相信她们是在城里过得好，毕竟……城里再怎么样，留在外面更加活不下去啊。哼……"
    hide liimg
    show liimg black laugh at char_right 
    li_speaking "当然了，就算不相信的，一群快残废的人跟带高级武器的上等人，难道还能冲上去质问不成。"
    hide qianimg
    show qianimg black still mask at char_left
    qian_speaking "……"
    hide liimg
    show liimg black o at char_right 
    li_speaking "不过啊……她们要相信也完全可以理解。外面太难活了，沙暴越来越多，城里人过来的次数也越来越多，上一次也就是在不久前。"
    hide liimg
    show liimg black close at char_right 
    li_speaking "可我是知道的，明知道有问题还不能阻拦。我真是，真是让人受不了……"
    hide qianimg
    show qianimg black sad mask at char_left
    qian "黎沙的声音越来越低，几乎要听不见。那一瞬间，我骤然感到心痛。"
    qian "第一次在她身上看到好似“脆弱”的影子，可明明不该是这样的……\n其实，她也才和我差不多年纪啊……"
    qian "我突然有种强烈的冲动，想要……说些什么的冲动。"
    menu:
        "【对不起】":
            jump q2_3_1_1
        "【去阻拦】":
            jump q2_3_1_2


label q2_3_1_1: # ending here
    hide qianimg
    show qianimg black still mask at char_left
    qian_speaking "对不起……"
    hide liimg
    show liimg black still at char_right 
    li_speaking "……\n我说过的吧，你有什么好对不起的，别总是说这话。"
    qian_speaking "对……呃，嗯……"
    hide liimg
    show liimg black at char_right 
    li_speaking "你自己好好休息，别想太多。"
    hide qianimg
    show qianimg black sad mask at char_left
    qian_speaking "好，嗯……那个……"
    li_speaking "想不出话就别说了。"
    qian_speaking "嗯……"
    hide liimg with dissolve
    qian "鬓发遮住了黎沙的眼睛，我看不清她的表情，迷茫得不知道做什么。\n说起来，这个场景和刚遇到她的时候几乎一样……"
    qian "只是，那时候我并不知道自己的人生会发生如此改变……"
    qian "从未想过自己会沦落如此境地，这双眼睛是否也是一种报应呢。"
    qian "未来，我将会在这里活下去吗……"

    # 【Ending：沉默】
    window hide
    show screen ending_title(number=17) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[17] = 1
    return


label q2_3_1_2:
    scene bg_liroom0 with Fade(0.2,0.2,0.2,color="#fff")
    show qianimg black shout mask at char_left with dissolve
    qian_speaking "……那，\n去阻拦吧。"
    show liimg black ask at char_right with dissolve
    li_speaking "什么？"
    hide qianimg
    show qianimg black sad mask at char_left
    qian_speaking "我是说……就是，那些事情，去阻拦它们啊。"
    hide liimg
    show liimg black laugh at char_right 
    li_speaking "……噗，哈哈。"
    li_speaking "要不是知道你就这么天真，我真的会以为你是故意气我的。"
    hide qianimg
    show qianimg black still mask at char_left
    qian_speaking "……"
    hide liimg
    show liimg black smile at char_right 
    li_speaking "之前你自己说的话都忘了吗，你们的管理有多麻烦，阻拦这件事又怎么可能。"
    qian_speaking "……"
    qian "果然她也是有想过的，之前盘问我各种D层的问题大概也是为了这个……"
    qian_speaking "那些城里的……她们不是在招人吗，当时听旁边的人说什么这次要的人很多，应该很着急吧……"
    qian "我没有急着反驳黎沙——毕竟她不信任我也是理所应当——而是自顾自地往下说。"
    qian_speaking "只要混进去就好了。"
    hide liimg
    show liimg black at char_right 
    li_speaking "……嗯？什么意思。"
    qian_speaking "重复以前的人的做法，被她们带进城。提前做好准备的话，也许就能知道她们到底经历了什么，说不定可以获得线索，那之后……"
    li_speaking "那之后呢？"
    hide qianimg
    show qianimg black mask at char_left
    qian_speaking "呃……我还没想好。"
    li_speaking "……我说过吧，城里拥有的资源不是我们能比的，这种情况下自己闯进去和活腻了有什么区别。"
    qian_speaking "是啊，我想得太简单了。但这也是最容易的办法……"
    hide liimg
    show liimg black o at char_right 
    li_speaking "不过我觉得可以试试。"
    hide qianimg
    show qianimg black o mask at char_left
    qian_speaking "至少它理论上是可行——啊？\n你……你觉得可以？"
    li_speaking "是啊。"
    hide liimg
    show liimg black smile at char_right 
    li_speaking "赌一下，大不了就是死而已，但如果赌赢了……到那时候，我真想看到那些人的表情。"
    hide qianimg
    show qianimg black still mask at char_left
    qian "她如此轻巧地把自己放在命悬一线的天平上，语气像猜测今天的饭好不好吃。\n我……"
    menu:
        "【跟她一起】":
            qian "我惊讶于她的回答，因而没有太多犹豫，正好逼迫自己下定决心。"
        "【不跟她一起】":
            hide qianimg
            show qianimg black close mask at char_left
            qian "不……都到这个时候了，我怎么可能再次逃避。"
            qian "我硬生生在心里掐断即将出口的软弱话语，转换成背道而驰的意味。"

    hide qianimg
    show qianimg black shout mask at char_left
    qian_speaking "嗯，我也是……这么想的。"
    hide liimg
    show liimg black o at char_right 
    qian "无视黎沙微微皱起的眉毛，我忍住不适感，努力把话说完。"
    hide qianimg
    show qianimg black still mask at char_left
    qian_speaking "既然是我说的建议，我当然也要去。\n况且，我也有……自己想知道的事情。"
    hide liimg
    show liimg black still at char_right 
    li_speaking "你现在倒是令我惊讶呢。"
    qian_speaking "是吗……哈哈……"
    qian "我缓缓地吐出一口气。\n其实我自己也是。哪怕是半个月前的我，也不可能会想到我现在沦落成这样……"
    qian "从未想过自己的生活会完全失常，也从未想过荆棘之城建立的骗局……但不管怎样，我必须要回去那里，去找出所有事情的原因……"
    hide liimg
    show liimg black o at char_right 
    li_speaking "不过，你是从那里出来的，回去的时候不会被发现吗？"
    qian_speaking "我不确定，不过……我现在脸都成这样了，风险小很多。"
    qian_speaking "至少一开始大概不会查得那么严，不然带不了这么多人进城……之后的事情再随机应变吧。\n不过，现在怎么说都是在赌了。"
    hide liimg
    show liimg black ask at char_right 
    li_speaking "的确，你的风险更高，真的要去？"
    hide qianimg
    show qianimg black closecalm mask at char_left
    qian_speaking "……是啊。"
    li_speaking "这个流程会持续几天，不用太着急。先准备一下，你也要休息好，之后去看能不能混进去吧。"
    hide qianimg
    show qianimg black mask at char_left
    hide liimg with easeoutright
    qian_speaking "嗯……"

    scene bg_liroom0 with fade
    qian "黎沙有其他事出去后，我躺在床上，总觉得有些憋闷。"
    qian_speaking "……真的可行吗……我……"

    show cg_qian20 at cg0 with Fade(0.2,0.2,0,color="#fff")
    pause(0.2)
    qian "焦虑和迷茫让我无法继续待在房间，只好带上披风走到室外。"

    scene bg_sand1 with fade
    qian "难闻的尘土气息扑面而来，我紧了紧领口，第一次以平静的心情看着这个地方。"
    qian_speaking "……嗯？"
    qian "脚下突然有阻力传来，我低头一看，是一团深黑色的纠缠脉络。"
    window hide
    show cg_flower0 at cg0 with dissolve
    pause(1.5)
    show cg_flower1 at cg0 with dissolve
    window show
    qian "我蹲下用手拨开，不出意外地被扎得一痛：黑色脉络上生满棘刺，拨开后能看到白色小花。"
    show cg_flower2 at cg0 with dissolve
    qian "果然是，荆棘花……在布满灰尘的视野里，这片白色格外显眼。那是只要有一点机会就能够肆意生长的植物，即使在自然环境贫瘠的荆棘之城也能盛开——也是城市名字的起源。"
    qian "一直以来，我认为那是城市的独有品种，象征着荆棘之城的坚韧、不屈，被印刻在城市印章上，同样是我的信念。"
    qian "但……现在看来，那也是虚假的。和城市无关，它在哪里都一样自由生长。"
    qian "……"



    scene bg_tall1 with fade
    "滴——"
    unknown "身上的东西都解开看看。"
    unknown "……啧。"
    unknown "嗯，好了，过去排队吧。"
    show qianimg coat still mask at char_left with easeinright
    qian_speaking "……"
    hide qianimg
    show qianimg coat closecalm mask at char_left
    qian "我不着痕迹地喘了一口气，第一步成功了……她们真的只是简单检查了身体，用的是我没见过的设备，但似乎并没有高级的功能。"
    
    scene bg_tall0 with Fade(0.2,0.2,0.2)
    qian "在遍布疮痍的黄沙之上，这座高高拔起的城市格外显眼。"
    show liimg coat o at char_right with easeinright
    li_speaking "还真是壮观啊。"
    show qianimg coat mask at char_left with easeinleft
    qian_speaking "嗯……"
    hide liimg
    show liimg coat laugh at char_right 
    li_speaking "真是好奇，掠夺了多少，才能建出来这样的东西。"
    qian_speaking "……\n……是啊……"
    show dark with dissolve
    qian "从下而上，荧光蓝色的保护罩隔绝了外界的一切。\n我第一次以这样的角度看见荆棘之城。"
    qian "它是如此宏伟，壮观……如果是以前的我，一定会如此感慨吧。"
    qian "然而现在……我已经不知如何面对。"

    scene bg_ele1 with fade
    show liimg black at char_right with dissolve
    li_speaking "有发现什么吗？"
    show qianimg black o mask at char_left with dissolve
    qian_speaking "没什么问题……"
    hide liimg
    show liimg coat o at char_right 
    li_speaking "嗯……之后再看吧。"
    qian_speaking "……"
    qian "我没有继续说话。\n这里实在太挤，我几乎整个人贴在黎沙的胸口。身上只剩最内层的衣服，说的每句话都能带起微妙的共振。"
    hide liimg
    hide qianimg
    window hide
    show cg_li40 at cg0 with dissolve
    pause(1.5)
    window show
    li_speaking "你那是什么表情……害羞？"
    qian_speaking "没有。况且我们都一起睡过了。"
    li_speaking "啧……你这话怎么听着怪怪的。"
    qian_speaking "……是你先说的吧。"
    show cg_li41 at cg0 with dissolve
    qian "……总觉得有些尴尬。为了分散注意力，我把视线再次投向四周。"
    qian "这里像是一个大型快递箱，而我是箱子里的货物。人们拥挤着，脸上大多是焦虑和雀跃交织的神情，窸窣的交谈声不断传出，音量不大，在耳边嗡嗡作响。"
    qian "脚下的地板在不断上升，载着一箱的期盼。"

    scene bg_black with dissolve
    "如果要去的地方并不是想象的那样，而只是另一个火坑呢？"
    qian "黎沙的话语蓦地在我脑海里跳出，我捏紧手掌心——此时此刻，才发现它已经浸满汗水——无法辨认出周围的表情是真心实意，还是无法选择。"
    qian "但是就算能辨认出又怎么样。"

    scene chaos0 with dissolve
    unknown "新一批的来了。"
    unknown "是吗？好……\n那边的，过来排队。"
    qian "不知什么时候，上升停止了，刺眼的光亮从打开的门缝里传来。"
    qian "我若有所思地看着眼前的移动终端——上面不是我的名字，没有通行号码，所有活动也不会被中央系统记录。"
    scene bg_edge with Fade(0.2,0.2,0.2,color="#fff")
    qian_speaking "原来是这样……"
    qian "这里是D层的外侧，城外的人被分散安置在各处，进行简单的工作，不能透露自己的信息，同时被要求写下每天的个人日记。"
    qian_speaking "D层管理松散，就是这样进来的啊……"

    scene bg_edge with Fade(0.2,0.2,0.2)
    unknown "你要去哪？"
    qian_speaking "呃，抱歉……我走错了。"
    unknown "别到处乱跑。"
    qian "直到关上房间的门，我才终于从形影不离的视线中逃出来——虽然被分散了，但似乎到处都有严密的监视，我只要偏离平时的路线就会引来关注。"
    qian "办不到吗……\n那只能等了，等着看她们接下来要做的事情……"
    qian "如果以前的人都失去联系，那现在这个平静的阶段一定不是最终结果。之后，之后一定发生了什么……"
    "……"

    scene bg_office_6 with Fade(0.2,0.2,0.2)
    unknown "你的工作做得不错，我们决定破例将你调至A层，现在就走吧。"
    qian_speaking "……知道了。"

    scene bg_ele with Fade(0.2,0.2,0.2)
    horr "咚……咚……"
    qian "脚下的地板在微微震颤，是不断上行的中枢直行电梯。"
    horr "咚……咚……"
    qian "通过透明玻璃，能够看见逐渐变亮的天色。"
    qian "果然，果然是这样……\n我的心脏正在高速跳动……几乎要震聋我的耳朵。"
    qian "从未想过，我会以这样的方式回到这里。\n工作只是幌子，目的是找关系顺利将人带入A层。\n也许我马上就要接近秘密了……那里会不会……有关于家人的线索。"

    scene bg_scene with fade
    show liimg black o at char_right with dissolve
    show qianimg black mask at char_left with dissolve
    li_speaking "目前为止，似乎还没发生什么。"
    qian_speaking "有啊，我们分散之后又被送回另一个拥挤的房间了。"
    li_speaking "……也是。所以你也是吗？工作，被要求写日记，然后被送到这个什么A层。"
    hide qianimg
    show qianimg black o mask at char_left
    qian_speaking "嗯，是啊……"
    li_speaking "什么都没发生……目前为止。但是这么多要写的信和日记，就是寄出去的那些吧。"
    hide liimg
    show liimg black ask at char_right 
    li_speaking "所以之后一定会发生什么事，让我们这些人连信都不能继续写了。"
    hide qianimg
    show qianimg black still mask at char_left
    qian_speaking "也许就是即将发生的事情……"
    li_speaking "嗯。"
    qian_speaking "……"
    "哧——"
    qian "飞行器平稳地降落。\n我们都沉默下来，无言等待即将到来的，不知道是什么的东西。"
    hide liimg with easeoutright
    hide qianimg with easeoutright
    window hide
    scene bg_cut30 at cg0 with Dissolve(3)
    pause
    scene bg_labfloor with Fade(0.5,0.5,0.5,color="#fff")
    window show
    qian "一层，两层，三层……我跟着长长的队伍走上楼梯。而后，洁白冰冷的走廊在眼前展开。\n不是室外……从风格来看，更像是某个大型研究基地。"
    qian "研究基地……我突然想到所有事情的开端，惊得差点忘记了呼吸。"
    qian "……她们不就是在研究所工作的吗？A层不小，但这种面积的大型研究所，我想不会有太多。况且……我的直觉告诉我，绝对是同一个地方。"
    show blur with shake
    qian "这么多异常的巧合聚集在一起，就绝对不是巧合。"
    li_speaking "你怎么了？"
    hide blur with dissolve
    qian_speaking "嗯？啊……我没事。"
    qian "被黎沙提醒，我才发现自己全身都在颤抖。没关系……还好人很多，即使我的反应如此明显也没有被注意到。"
    show liimg black laugh at char_right with dissolve
    li_speaking "真是好奇，你们到底烧了城外多少资源？这么豪华……肯定不止这一个地方吧。"
    show qianimg black still mask at char_left with dissolve
    qian_speaking "……"
    qian "她是笑着说的，声音里却没有多少真实存在的喜悦——这也是显而易见。"

    scene bg_labfloor with Fade(0.2,0.2,0.2,color="#fff")
    qian "跟随前面的人走过几条相同的走廊，我已经有些失去方位。在一排同样的门前，我们进入一个巨大的房间。许多拥挤的隔板，床架，橱柜，以及许多、许多穿着一致的年轻人。"
    scene bg_bigroom with Fade(0.2,0.2,0.2,color="#fff")
    qian "和门口不同，房间里几乎没有什么声响，没有嘈杂激动与紧张，只有平静到死寂的深水。"
    qian "惨白色灯光照得人也惨白，像夏夜故事里浪漫的的幽灵传说。只可惜这里不是夏天，没有浪漫，只有人挤人导致的无限热意和逼仄，一波又一波拍打我的身体。"
    show white_fem at char_left with dissolve
    white_speaking "换好衣服的过来这边。\n大家也不用担心，只是换了个地方为我们工作而已。只是这是实验室，涉及机密，生活上的不便还请谅解。"
    show qianimg white mask at char_right with easeinright
    qian_speaking "……"
    qian "我有些不习惯地扯了扯衣服和脖子上挂着的标签，说不清的感觉令人烦躁。奇怪的机器覆盖我的全身，仿佛在扫描什么。"
    
    scene bg_bigroom with fade
    show qianimg white mask at char_left with easeinright
    qian_speaking "这是……？"
    show white_fem at char_right with dissolve
    white_speaking "不要问那么多，让你做什么做就行了。"
    white_speaking "也不要想着别的啥的，我在这等着你吃完。\n之后经常要做，早点习惯。"
    qian_speaking "……"
    hide qianimg
    show qianimg white still mask at char_left
    qian "的确现在没有办法了……我看着手里的药片，在刺目的注视下把它塞进喉咙。"
    white_speaking "张嘴。\n嗯……行了，去标着你编号的地方吧。"

    scene bg_bigroom with fade
    show liimg white at char_right with dissolve
    li_speaking "你吃了吗？"
    show qianimg white closecalm mask at char_left with dissolve
    qian_speaking "还能怎么办？不都有人盯着吗。"
    li_speaking "……"
    hide liimg
    show liimg white o at char_right
    li_speaking "要不，试试催吐？"
    hide qianimg
    show qianimg white mask at char_left
    qian_speaking "嗯……但要等她们走了。\n不知道这里到底是做什么的，也不知道她们到底是谁。"
    li_speaking "真正的组织者大概见不到。"
    qian_speaking "还是要先摸清这里的情况……按照这个规定，我们没办法出这个房间，只能在里面看看了……"
    qian "四周并不安静，恐慌和迷茫在房间里蔓延——也是，本以为新生活已经开始，突然又被带走，都会感到奇怪吧——没人注意到我和黎沙的对话。"
    hide qianimg
    show qianimg white still mask at char_left
    qian "我不动声色地环绕整个房间。这里只有一扇门，先前看到的隔板把空间分成不同的区域，大约是用来睡觉的和检查的，十分简陋。"
    qian_speaking "……\n总觉得，有种很不舒服的感觉。"
    li_speaking "什么？"
    qian_speaking "不，没事……我们去洗手间吧。"
    li_speaking "好。"
    scene bg_bigroom with Fade(0.2,0.2,0.2)
    show blur with vpunch
    qian_speaking "呃，呕……呕啊……咳……呕……"
    qian "我的手指高速颤抖着，无序地在嗓子眼打转。\n随着令人反胃的酸味上涌，恶心的黏腻液体从我嘴角溢出。"
    qian_speaking "呜……咳……哈……\n……我这边也是，果然已经被消化了，没什么用。"
    li_speaking "都已经这样了，至少她们肯定不会这么快下杀手，不会死就之后再看吧。"
    qian_speaking "……嗯，也是。"

    scene bg_bigroom with Fade(0.2,0.2,0.2)
    show liimg white at char_right with easeinright
    li_speaking "在看什么？"
    show qianimg white mask at char_left with dissolve
    qian_speaking "在确认……"
    li_speaking "嗯？"
    qian "我盯着镜子里的自己，好一会，才重新移开视线。"
    hide qianimg
    show qianimg white still mask at char_left
    qian_speaking "我们都胖了。嗯，说胖不太准确……这是和以前相比。\n应该说，看起来体型健康了很多。"
    hide liimg
    show liimg white ask at char_right
    li_speaking "不是好事吗？"
    qian_speaking "是这样，但是太快，也太统一了……我只是觉得有些奇怪。"
    li_speaking "哦，我懂了。你是觉得，是因为这几天吃的药是吗。"
    qian_speaking "嗯……她们总不会这么好心……不过，可能是我想太多。"
    hide liimg
    show liimg white o at char_right
    li_speaking "多提防不是什么坏事，虽然暂时没办法，总之留个心眼吧。"

    scene bg_bigroom with Fade(0.2,0.2,0.2)
    qian "我的预感很快得到了证实。"
    qian "分发的日程表上多了几行字。\n进行性交，直到受孕为止。\n抽血，加药，检测。"
    show qianimg white shock mask at char_mid with dissolve
    qian_speaking "……"

    scene bg_bigroom with Fade(0.2,0.2,0.2)
    show qianimg white still mask at char_left with dissolve
    qian_speaking "开什么玩笑……疯了吗？"
    qian_speaking "生育早就可以用机器做完全套流程了，为什么要用这么原始的方法……"
    show liimg white ask at char_right with dissolve
    li_speaking "……\n虽然不是很懂你们的什么机器，不过，大概是为了省钱吧。"
    hide qianimg
    show qianimg white shout mask at char_left
    qian_speaking "哈？"
    hide liimg
    show liimg white closeask at char_right
    li_speaking "需要这么多孩子，用机器肯定耗资源，但找我们这种人……只要有个能放得下的地方，让人自己交配不是很便宜吗。"
    hide qianimg
    show qianimg white still mask at char_left
    qian_speaking "……"
    qian "需要这么多人生育吗……所谓的实验到底是在做什么……那些生下来的人都去哪了？"
    hide qianimg
    show qianimg white shout mask at char_left
    qian_speaking "……\n不能再继续等时机了。"
    hide liimg
    show liimg white still at char_right
    li_speaking "……就是说，今晚行动吗？"
    hide qianimg
    show qianimg white still mask at char_left
    qian_speaking "嗯……谁知道她们之后还会让人做什么。"
    li_speaking "也对……就这样吧。"
    scene bg_bigroom with Fade(0.2,0.2,0.2)
    show dark with dissolve
    qian "所有灯光都暗下来后，整个房间像一个大型的停尸房。今天把晚饭塞到其他人那里之后，果然晚上不会那么困了。"
    qian "我小心翼翼地移动身体，才没有在这拥挤的床铺间碰到别人。"
    window hide
    show cg_li50 at cg0 with dissolve
    pause(1.5)
    window show
    li_speaking "我感觉像在做梦。"
    qian_speaking "……为什么？"
    li_speaking "没想到我真的到城里来了。也没想过，你们的生活原来真的这么平静……哪怕是在这种地方……"
    qian "黎沙的声音平静而缥缈，像一股微风吹进耳朵。我有些难以理解她的感慨，无论是现在，还是城外，都远远比不上我之前的生活。"
    qian "因而，一种更深刻的茫然和疼痛挟住了我。"
    li_speaking "我好像……也有些理解了。只是交配而已，就算在这里被她们折腾，那也是活着啊。"
    qian_speaking "……\n你是犹豫了吗？"
    qian "出声后，我才发现我的声音也在发抖。"
    li_speaking "……\n我不想死。\n我要活下去。"
    qian_speaking "……"
    qian "我的豪言壮志让我自己也被欺骗得忘记了危险性，只有切身体会到这件事即将到来时才能意识到。\n我真的要去做一件出格的事，甚至会威胁到生命。"
    li_speaking "抱歉……让你看笑话了。"
    qian_speaking "不，怎么会……"
    show cg_li51 at cg0 with dissolve
    li_speaking "没有太多时间了……我听你的。"
    qian_speaking "……！"
    qian "她的双眸直直地看向我，那是摇晃、孤注一掷、混合着坚定的眼神。\n我——"
    menu:
        "【放弃】":
            jump q2_3_1_1_1
        "【继续计划】":
            jump q3_3


label q2_3_1_1_1: # ending here
    scene bg_bigroom with Fade(0.2,0.2,0.2)
    show dark
    qian_speaking "那……那就，算了吧……"
    qian "我艰难地吐出几个字，每个音节都仿佛在拉扯喉咙，疼得要命。"
    qian "即使设想了那么多，在真实的世界到来前，我不知道选择会有如此大的力量。"
    qian "手掌将衣服攥得湿透，我却还是慢吞吞地说完了。"
    li_speaking "好。"
    qian "……"
    show blur with dissolve
    qian "……啊……"
    scene bg_black with Fade(0.2,0.2,0.2)
    qian "我还是，逃避了……"

    scene bg_lab1 with Fade(0.5,0.5,0.5,color="#fff")
    unknown_inn "头好痛……"
    unknown_inn "这是哪……我是谁……？"
    show white_fem at char_mid with easeinbottom
    unknown_inn "眼睛适应光线后，面前的是一个穿着白衣服的女人。"
    white_speaking "现在感觉怎么样？"
    unknown "……呃……你是谁？"
    white_speaking "……\n不记得了？其他的事呢？"
    unknown "什么？"
    white_speaking "真的还是假装的？教授，这个实验品好像又失败了，你过来看看——"
    unknown "我不知道你们在说什么……那个……"
    show blur with dissolve
    unknown_inn "我迷茫地看着眼前的景象，只觉得一切都是那么虚假。"
    unknown_inn "我……究竟是谁？又为什么存在于此呢？"

    # 【Ending：陌生】
    window hide
    show screen ending_title(number=18) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[18] = 1
    return
    