label q2_2:
    scene bg_street with fade
    show qianimg at char_left with easeinleft
    qian_speaking "好黑啊……你怎么能走那么快。"
    show yingimg at char_right with easeinright
    ying_speaking "……"
    qian "星星点点的小灯嵌在建筑和道路的各处，即使是白天，D层也同样阴暗。"
    hide yingimg
    show yingimg o at char_right 
    ying_speaking "毕竟你们……这里，这么高。"
    qian "的确，上层的设施挡住了所有的光线……而现在连光亮也是奢侈。生活无聊透顶，我睁开眼看到黑暗，闭上眼还是黑暗，只有那些闪烁的灯光。"
    hide qianimg
    show qianimg o at char_left
    qian_speaking "嗯……\n所以，我们现在是要去干嘛？"
    ying_speaking "带你熟悉。"
    qian_speaking "啊？"
    ying_speaking "你还要在D层住吧。"
    qian_speaking "是啊，虽然我也不想……不过等我家里人联系我就好了，到时候我会再次感谢你的！"
    hide yingimg
    show yingimg still at char_right 
    ying_speaking "……"
    hide yingimg
    show yingimg o at char_right 
    ying_speaking "在那之前，至少你要了解这里。"
    qian_speaking "也对哦……还真是麻烦你了……"
    hide yingimg
    show yingimg stillo at char_right 
    ying_speaking "唉。"
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "怎，怎么了……我做错什么了吗，那个，你之前说过，可以让我留下来的……等我，等我家里人有消息之后我就绝对不会麻烦你了！"
    qian "我自己都觉得这话难听又没脸没皮，但现在她是我唯一能抓住的人了……我不想，不想一个人待在D层……"
    hide yingimg
    show yingimg at char_right 
    ying_speaking "没事。\n走了。"
    hide qianimg
    show qianimg at char_left
    qian_speaking "啊，嗯，好，好的！"
    
    scene bg_road03 with fade
    show qianimg at char_left with dissolve
    show yingimg at char_right with dissolve
    qian_speaking "D层的东西……虽然看起来很烂，不过都好便宜啊。"
    ying_speaking "工钱才多少。"
    hide qianimg
    show qianimg o at char_left
    qian_speaking "呃，是很少的意思吗……等等，这是个位数吗？只是这么点？"
    hide yingimg
    show yingimg still at char_right
    ying_speaking "……"
    qian_speaking "我不了解啊……对不起……"

    scene bg_road05 with fade
    qian_speaking "那是什么？"
    qian "出门的时候比较急，也还没适应昏暗的环境，现在回去的时候才注意到居民楼旁边格格不入的“那个东西”。"
    ying_speaking "不重要。"
    qian_speaking "可是那上面有“蓝石科技”的标志啊，那么显眼，你都不感兴趣的吗？你们D层不知道蓝石这个人吗，她公司经常在这边做慈善活动啊……"
    ying_speaking "不去。"
    show cg_ying20 at cg0 with dissolve
    window hide
    pause(1.5)
    window show
    qian_speaking "喂……"
    qian "就在我们拉扯的时候，又有几个人从旁边来回经过，让我更加好奇。"
    ying_speaking "走了。"
    qian_speaking "唉……等等！"

    scene bg_yingroom0 with fade
    show qianimg at char_left with dissolve
    show yingimg shirt at char_right with dissolve
    qian_speaking "不开灯吗？"
    ying_speaking "太亮。"
    qian_speaking "……呃，是因为太贵了吗？那个，我记得你之前说……"
    ying_speaking "算是。"
    qian_speaking "好吧……\n那你每天出去那么久，是在做什么啊……"
    ying_speaking "赚钱。"
    qian "我当然知道是赚钱，但具体……\n和莺莺对话实在太困难，感觉她不想跟我多说什么。不过这也理所应当吧，毕竟我添了麻烦……"
    qian_speaking "我能一起去吗？我是说，我可以帮你做点什么，之类的……"
    ying_speaking "不需要。"
    qian_speaking "好吧……"
    
    scene bg_street with Fade(1,1,1)
    qian "……"
    show yingimg at large2 with easeinbottom
    ying_speaking "你还是要去看吗？"
    hide yingimg
    show qianimg shock at char_mid with my_shake
    qian_speaking "……哇啊！你，你吓死我了……"
    hide qianimg
    qian "幽幽的女声从背后传来，在黑暗里差点把我吓得心跳骤停。等我意识到是莺莺的声音，才缓缓吐出一口气。"
    show qianimg o at char_left with dissolve
    qian_speaking "你怎么醒了……"
    show yingimg at char_right with dissolve
    ying_speaking "……"
    qian_speaking "我只是，呃，睡不着，所以想散散心……"
    hide yingimg
    show yingimg o at char_right
    ying_speaking "去哪？"
    hide yingimg
    show yingimg still at char_right
    qian_speaking "就在周围随便走走啊……呃，好吧，我知道了……就看一眼也不行嘛？我都不知道那是什么诶。"
    hide yingimg
    show yingimg stillo at char_right
    ying_speaking "好吧。"
    qian_speaking "那一起去吧！"

    scene bg_street with fade
    qian "这个东西和周围的环境格格不入：巨大华丽的招牌，低调却精致的金属外壳，仅能容纳单人的神秘房间……共同构建成了这个特别的角落。"
    qian "在我们到的时候，刚好有人从门口出来。外面光线很暗，看不清她的表情，只感觉她似乎不太想离开，脚步缓慢而虚浮。"
    show yingimg still at char_right with dissolve
    ying_speaking "进去吧。"
    show qianimg o at char_left with dissolve
    qian_speaking "呃，你呢？"
    ying_speaking "等你。"
    qian_speaking "好，好的，谢谢……"

    scene bg_device
    qian "简约的房间里只有一张看起来设计很复杂的椅子，旁边贴着各种告示和指南——价格不算太贵，但也不便宜，是一个刚好狠下心就能尝试一次的价格。"
    qian_speaking "又让她帮了我一次啊……"
    qian "“蓝石科技出品”，“梦境机器”，“将为你定制只属于你的电影，实现你心里的愿望”……这说明写得好玄乎，但如果是蓝石科技，却意外地有可信度……"
    qian "都到这里来了，我实在按捺不住自己的好奇心。我坐上椅子，立马被旁边的卡扣控制住，一个巨大的防护罩从椅子上展开，罩住我的整个身体。"
    qian "光屏在视野中亮起：“使用声明：1.……”\n谁会真的一条条看过去……我很快按下“同意”，随即眼前一黑。"
    "……\n……"

    scene bg_prolo_01 with fade
    unknown "时茜，又在看什么呢？"
    qian_speaking "啊，黄女士！回来好晚！"
    qian "微风拂面，温暖的阳光透过落地窗，照进宽敞的室内，把家具们和书架上的书都染上一层金黄。\n我把手中的柔软抱枕扔出去，一下从沙发上跳下来。"
    "要上班啊，我这算早的，小钟还没回来呢。"
    qian_speaking "好吧，可是我觉得你们偶尔也可以陪我一起玩一会啊。"
    "行行，有时间一定，你也可以去找那个姐姐玩啊。"
    qian_speaking "那，那是……"
    "哟，不想去？"
    qian_speaking "才没有！"
    "行啦，该干啥干啥去，今晚可以三个人一起吃饭哦，等会小钟就回来了。"
    qian_speaking "好啊！"
    scene bg_prolo_01 with Fade(0.1,0.1,0.1)
    unknown "时茜，别乱扔东西！"
    qian_speaking "我马上就去收……别生气嘛钟女士。"
    "我还生气呢，我就是太惯你了。"
    "赶紧收完过来吃东西，我们刚做好的待会凉了。"
    qian_speaking "知道啦！"

    scene bg_black with fade
    "……\n……"
    unknown "时茜……时茜？"

    scene bg_road06 with vpunch
    qian_speaking "啊……啊！嗯……"
    show yingimg o at char_mid with dissolve
    ying_speaking "醒醒。"
    qian_speaking "啊，对，我知道！我醒着呢，那个，我们该回去了，回去吧……"
    hide yingimg
    show yingimg still at char_mid
    ying_speaking "……\n已经到了。"
    qian_speaking "啊，啊，嗯……"
    qian "……"
    qian "头痛欲裂……总觉得像有人用针扎进了我的大脑……也许是因为看到那些场景让我难受吧……可说到底，那个机器是怎么做到的……"
    qian "我的脚步一浅一深地跟在莺莺身后，缓慢地往来时的路走。转过弯，我忍不住最后一瞥那个方向。"
    qian "远处的庞大招牌像漆黑森林中的唯一灯塔，吸引无数迷路的人。\n难怪叫做“梦境”，难怪昂贵，难怪总是看到有人……"
    
    scene bg_yingroom0 with fade
    show yingimg shirt at char_right with easeinright
    ying_speaking "该睡了。"
    show qianimg o at char_left with dissolve
    qian_speaking "是，是啊……"
    ying_speaking "我锁门了。"
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "嗯，你……别看我了，我不会再出去了……"
    ying_speaking "好。"
    hide qianimg
    show qianimg at char_left
    qian "我松了口气，她一如既往的冷淡态度如今反而让我好受，也许那是一种仍然熟悉的认知带来的心安感觉。"
    qian_speaking "谢谢你啊。"
    hide yingimg
    show yingimg shirt close at char_right
    ying_speaking "……\n睡吧。"

    scene bg_black with Fade(0.1,0.1,0.1)
    "……"

    scene bg_yingroom0 with Fade(0.1,0.3,0.2)
    show qianimg shock at char_mid with dissolve
    qian_speaking "……哈啊！"
    hide qianimg with dissolve
    qian "好黑……还是不习惯这个地方……\n从梦中惊醒，心脏还在狂跳不止，我捂住胸口，忍不住大口喘息着，而衣领已经潮湿一片。"
    qian "又做梦了……梦境是假的，可角色和内容太过真实。我最怀念的，家人在的时光……\n蓦地，我回想起从蓝石科技的机器前离开的人，脸上那晦暗不明的表情。"
    qian "我怔怔地望着床边，仿佛能透过墙壁看到很远的地方，远得从未到过D层的地方。"
    qian "家喻户晓的标志再次划过我的脑海，现在却对我有了不同的意义。\n……我还要再去，那个机器吗？"
    menu:
        "【去】":
            jump q2_2_1
        "【不去】" if q1221 == True:
            jump q2_2_2


label q2_2_1: # ending here
    qian "迷茫和困惑充斥我的内心，可在其中，我还是能听到那不甘心的声音。"
    qian "说到底……为什么偏偏是我呢，凭什么我就要遇到这种事情呢……在这种地方，在这种条件的地方……\n我已经，没有什么好在乎的了……"
    qian "都已经这样了，至少让我做一会梦吧……也许只要把自己沉浸于美好当中，我就不会因为痛苦而崩溃……"
    qian "就算是假的也好，我也想再次感受一下，那种和家人在一起的感觉……"

    scene bg_street with Fade(0.5,0.5,0.5)
    show yingimg at char_right with dissolve
    ying_speaking "又要去吗？"
    show qianimg sad at char_left with dissolve
    qian_speaking "嗯，那个，你要，一起去吗……"
    ying_speaking "不。"

    scene bg_street with Fade(0.2,0.2,0.2)
    "……"
    show yingimg at char_right with dissolve
    ying_speaking "又去。"
    
    scene bg_street with Fade(0.2,0.2,0.2)
    show yingimg at char_mid with dissolve
    ying_speaking "今天也是。"

    scene bg_street with Fade(0.2,0.2,0.2)
    show yingimg still at char_mid with dissolve
    ying_speaking "今天也是。"
    
    scene bg_street with Fade(0.2,0.2,0.2)
    show yingimg stillo at char_mid with dissolve
    ying_speaking "今天也是。"
    
    scene bg_street with Fade(0.2,0.2,0.2)
    show yingimg close at char_mid with dissolve
    ying_speaking "……"
    
    scene bg_black with Fade(0.2,0.2,0.2)
    "……"
    "……"
    qian_speaking "呜，嗯……"
    ying_speaking "怎么了。"
    qian_speaking "我不想，再……"
    qian "莺莺站在身侧，熟悉的气息围绕着我，但已经并不能让我安定下来。此时此刻，我的脑海里只剩那些明亮闪烁的画面，那些本应在A层看到的画面……"
    ying_speaking "嗯。"
    qian_speaking "我不想……但是，我还是……就算是那假的……我……还是想去看……"
    ying_speaking "嗯，我知道。"
    qian_speaking "对不起，我……"
    ying_speaking "嗯，没事。"
    show cg_ying30 at cg0 with dissolve
    window hide
    pause(2)
    window show
    qian "我跪坐在地，几乎整个人靠在她的身上，明明是那么纤细的手臂，却有力地支持我的身体，已经我现在唯一可以依靠的，真实的东西……"
    ying_speaking "……时茜。"
    qian_speaking "呃，啊……"
    qian "莺莺的声音从头顶传来。也许是我产生了错觉，语气分明是一样冷淡，可她刻意压低后，比平时更加深沉厚重，仿佛潮水包裹着我。"
    qian "这样的声音，就像以前在家里听到的一样……"
    qian "就这样也很好……只要我能够找到支柱，哪怕是幻觉……我也要利用幻觉活下去。"
    ying_speaking "嗯……都可以。"

    scene bg_black with Fade(0.1,0.2,0.2)
    ying_speaking "时茜。"

    # 【Ending：美梦】
    $ persistent.ending[8] = 1
    return


image cg_ying4:
    "images/cg/cg_ying41.jpg"
    0.2
    "images/cg/cg_ying40.jpg"
    0.2
    repeat



label q2_2_2:

    qian "不，不行……现在我没有能力，只是靠莺莺的帮助……更何况，那个机器实在太容易让人沉迷，这不是什么好预兆……"
    qian "继续睡觉吧，别再想那些不现实的了……还有，明天还要和莺莺说事情……"

    scene bg_yingroom0 with fade
    show yingimg shirt o at char_right with easeinright
    ying_speaking "什么？"
    show qianimg at char_left with dissolve
    qian_speaking "就是……之前真的谢谢你。不过，你是知道什么吗？"
    hide yingimg
    show yingimg shirt at char_right
    ying_speaking "嗯？"
    hide qianimg
    show qianimg o at char_left
    qian_speaking "我和你只是偶然遇见，虽然很感谢你……但你为什么要这么对我呢……"
    qian_speaking "那个项目很火吧……我用D层的局域网查了，发现D层到处都有设置。很多人推荐，你不但不推荐，还不嫌麻烦地阻止我，为什么要做这么多……？"
    qian "D层能查到的信息不多，每天除了热门的新闻就是各大公司的宣传广告。这其中，蓝石科技占比最大，也是那个项目的发起方。"
    ying_speaking "……\n不是为你。\n那个很贵。"
    qian_speaking "……真的，是这样吗……"
    ying_speaking "嗯。"
    qian_speaking "总觉得被敷衍了……\n我本来是想摊牌，也想诈一诈她，希望她能自己说出什么的……果然这种想法还是太天真了。"
    qian_speaking "好吧……我想太多了。"
    ying_speaking "不，没什么。"
    qian "所以说，那是什么意思啊……总觉得，她身上带着不小的矛盾和谜团。也许她认识我？那说不定能找出什么线索……"
    
    scene bg_black with fade
    qian "黑暗。\n无边的黑暗笼罩着我。"
    show blur with my_shake
    qian "深处似乎有什么东西……白色的，跳跃的线条。\n被我看到的时候，它们突然膨胀，扩散，挤压——"
    qian "好难受……！要，喘不上气了……啊——"
    qian_speaking "呜……！"
    show cg_ying40 at cg0 with vpunch 
    qian "什，什么——！\n我倏地睁开眼，却是莺莺那冰冷的眼神，以及，掐住我脖子的双手。"
    show cg_ying4 at cg0 with vpunch
    qian_speaking "为……什……你……啊啊……"
    qian "我艰难地喘息着，搞不清楚状况，但求生的本能让我用力挣扎，试图突破她的控制。"
    qian "快……快点……用力……！！！"

    $ time = 2
    $ timer_range = 4
    $ timer_jump = 'q222fail'
    show screen countdown
    menu:
        "【推开她】":
            hide screen countdown
            jump q222success


label q222success:
    qian_speaking "哈……啊！！！！"
    scene bg_white with vpunch
    qian "我爆发出惊人的求生意志，一把推开了压在身上的莺莺。"
    scene bg_yingroom0 with Fade(0.1,0.1,0.1)
    ying_speaking "唔……"
    qian "趁她受到冲击，没反应过来的时候，我赶紧连滚带爬地下床，踉跄着跑出了房间。"
    scene bg_corridor with vpunch
    qian_speaking "……可恶，那家伙，哈……到底，要干嘛……"
    qian "我躲在楼层的角落，却并没有看到她出门的动静。她似乎没有要把我赶尽杀绝的意思，可那又为什么……"
    qian "……是因为被我发现了秘密吗？"

    scene bg_yingroom0 with fade
    show bg_mem
    qian "这是……\n我惊异地看着眼前的那个东西——"
    hide bg_mem
    show cg_stone at cg0 with fade
    show bg_mem
    qian "闪闪发光的晶矿石，现今最重要的能源，可维持整个城市的运转，也可用作私人财产交换，价值千金。"
    qian "D层这么穷，她怎么会有这个？"
    qian "……"
    
    scene bg_corridor with fade
    qian "如果是这样，那就能说得通了……可就算知道了这个，我现在该怎么做……"
    scene bg_office_5 with Fade(0.1,0.2,0.1)
    qian "反应过来的时候，我已经下意识地走到管制局附近，和D层格格不入的明亮光线从街的另一侧照进来。\n有问题的话，就要找管制局，一直以来的认知就是如此……"
    qian "然而，我现在却莫名地有些犹豫……要进去吗？"
    menu:
        "【不进去】":
            jump q2_2_2_1
        "【进去】":
            jump q2_2_2_2


label q222fail: # ending here
    qian "可，可恶……到底……为什么，会这样……"
    qian_speaking "你不是……之前还……帮我，的吗……"
    scene bg_black with vpunch
    qian "啊，啊啊……"

    # 【Ending：窒息】
    $ persistent.ending[9] = 1
    return


label q2_2_2_1:
    show qianimg still at char_mid with dissolve
    qian "不，不对……再仔细想想。\n莺莺拥有晶矿石确实很奇怪，但也不是什么特别的秘密，甚至需要杀人灭口。\n"
    qian "也许重点并不在晶矿石，而在于是“我”看到了晶矿石……她害怕我，或者说害怕某些跟我有关的事情。"
    qian "而我现在身上的事……本就和管制局有密切的关系。在这样的情况下，我怎么可能再去找她们……"
    show bfem_0r at char_right with easeinright
    bfem "你来这里有什么事情？"
    hide qianimg
    show qianimg o at char_mid
    qian_speaking "嗯……啊？没事，我走错了……"
    qian "没想到我还没思考完，就被人拦住了话头。而她正是那天把我押送至D层的人中的一个——执行队的人——我不由有些紧张。"
    bfem "之前怎么没来这里？你在D层有认识的人吗？"
    hide qianimg
    show qianimg still at char_mid
    qian_speaking "是啊，不行吗？"
    qian "我没什么好语气，而她只是又看我一眼，而后点点头就离开了。"
    qian "总感觉有些奇怪……不过，这不是我现在需要关注的事。\n想清楚后，我决定还是自己再去调查莺莺，也许就和我家人的事有关系。"
    hide qianimg
    show qianimg at char_mid
    qian "我和莺莺争执在凌晨，现在回去的时间，是她平时会出门的时间。\n正好，可以看看她到底在干什么……"
    
    scene bg_edge with fade
    qian "相似的光景不断从视野两边掠过，垂直拥挤的建筑，崎岖不平的路面，以及阴影缝隙里的人流。\n我在，跟踪莺莺……"
    qian "不知道走了多久，人群密度稀释，空间愈发无序，远处隐约能看到透明的淡蓝色覆盖住所有能看到的区域——那是保护罩，这座城市存活的基础。"
    qian "怎么会跑到这里……我止住向前的脚步，更多的疑惑涌上心头。\n好在莺莺也恰好在前方停下，没有让我丢失她的行踪。"
    qian_speaking "这是……"
    show cg_ying50 at cg0 with dissolve
    window hide
    pause(1.5)
    window show
    show cg_ying51 at cg0 with dissolve
    qian "另一个女人出现在莺莺面前，我连忙躲进集装箱的缝隙里。如果我没看错……那人身穿管制局的衣服。\n她怎么会和管制局有私下联系……"
    ying_speaking "给你晶矿石，让我进去，对吧？"
    place_holder "别废话，难道还骗你不成？"
    ying_speaking "……"
    qian "莺莺伸出手，晶矿石的光芒如同它的价值一般熠熠生辉，甚至能打动管制局的人。\n但是，她到底要去哪……？"
    scene bg_edge with vpunch
    qian "？！"
    qian "我的问题还没得到解决，突如其来的风声打破了平静的场景。"
    show grey_fem at char_left with easeinleft
    place_holder "谁在那里？"
    show bfem_0r at char_right with easeinright
    unknown "是该我问你们，在这里做什么？"
    place_holder "执，执行队……您好。"
    unknown "解释一下？"
    place_holder "这，这是……那个……"
    unknown "……"
    hide grey_fem with easeoutleft
    unknown "——不许跑！"
    scene bg_edge with vpunch
    "砰！"
    ying_speaking "……呜……！"
    qian "突然的枪声穿过我的耳膜，仿佛一道惊雷劈过。\n……怎么会？！怎么有人敢在城内开枪……！"
    qian "我似乎听见莺莺痛苦叫声，而后，踉踉跄跄的脚步声朝我的方向过来。"
    qian "糟糕，现在该怎么办……"

    # QTE here
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'q320_fail'
    show screen countdown
    # can add some click sfx here
    menu:
        "【伸手帮忙】":
            hide screen countdown
            jump q3_2
        "【坐视不理】":
            show qianimg still at char_mid with dissolve
            qian "太危险了，我还是不要插手比较好……"
            hide screen countdown
            jump q3_2_0


label q320_fail:
    show qianimg shock at char_mid with dissolve
    qian "完了……！"
    qian "事情发生得太快，我完全没来得及反应……"
    jump q3_2_0


label q3_2_0: # ending here
    scene bg_edge with vpunch
    "砰！砰！"
    qian "又是几声枪响，开枪的人毫不留情。很快，这一片的纷乱褪去，只剩下开枪者那缓慢沉稳的脚步声。"
    show qianimg shock at char_mid with dissolve
    qian_speaking "呜……\n怎么会……"
    qian "我原以为她们会交涉什么，或许能说出我不知道的情报。\n可我没想到，那个执行队的人竟然会如此轻易而果断地杀死对方，甚至没有犹豫……"
    scene cg_ying60 at cg0 with fade
    window hide
    pause(1.5)
    window show
    qian "怎么会这样……"
    qian "说起来，这大概是我第一次见到她脸上出现这么生动的表情……\n哈……这一点也不好笑。"
    qian "我颓丧地坐在地上，注视着那正在消散的瞳孔。"
    qian "你身上究竟发生了什么事……我不知道，也再也没有机会知道了。"
    qian "这也许是我能找到线索的最后机会，而现在，它也随着她一起消逝在无尽的黑暗中。"
    show cg_ying61 at cg0 with dissolve
    window hide
    pause(1.5)
    show cg_ying62 at cg0 with dissolve
    pause(2)
    scene bg_black with fade
    window show
    qian "不行了……"
    qian "无论如何，我都无法再鼓起勇气，只好在逃避中不断麻木自己。\n怎么会，一个人的生命怎么能如此轻易地就被抹除……"
    show cg_ying60 at cg0 with Fade(0.1,0.1,0.1,color="#fff")
    pause(0.5)
    hide cg_ying60
    qian "也许……\n我隐隐有一种预感，我也许再也忘不了她，直到永远。"

    
    # 【Ending：秘密】
    $ persistent.ending[11] = 1
    return



label q2_2_2_2: # ending here
    qian "像这样的问题，交给专业的人来处理也许更合适……事不宜迟，我平静好自己的气息，快步进入管制局。"
    qian "就在不久前，我的日常从这里开始破灭……管制局，说不定能顺便了解些家里人的事。"
    scene bg_office_6 with fade
    show grey_fem at char_left with easeinleft
    stf_speaking "好的，我们会尽快处理。"
    show qianimg still at char_mid with easeinright
    qian_speaking "尽快是什么时候？"
    stf_speaking "我们会安排。"
    hide qianimg
    show qianimg shout at char_mid
    qian_speaking "不能现在吗？她可是威胁到我的生命安全！"
    stf_speaking "工作繁忙，需要安排。"
    hide qianimg
    show qianimg still at char_mid
    qian_speaking "……"
    qian "明明看到里面的人都在打牌，说什么繁忙……我咬紧牙关，拼命不发出失控的声音。"
    show bfem_0r at char_right with easeinright
    unknown "怎么回事？是你？"
    qian "我转过头，发现是先前闯入我家的黑衣女人。她深深地看了我一眼，而后用没有起伏的语气问道。"
    stf_speaking "啊，您怎么来了……这女的让我们查人，我跟她说别急她还不接受……"
    bfem_speaking "我知道了，查谁？知道终端号码吗？"
    hide qianimg
    show qianimg o at char_mid
    qian_speaking "啊……？知，知道……"
    qian "也许是我的质问态度起了效果，她的态度似乎积极了一些。我之前特地记了终端号，想不到会有用。"
    bfem_speaking "……"
    bfem_speaking "你进来一下。"
    qian_speaking "啊？"
    bfem_speaking "这个人有危险吧？你先在这里休息吧。"
    hide qianimg
    show qianimg sad at char_mid
    qian_speaking "啊？好，好的……"
    qian "我甚至有些受宠若惊，不知道为什么她突然又变得好说话。\n……难道是和我家人有关系了？"

    scene bg_office_1
    qian "我跟着她走进玻璃的另一侧，转过弯，进入房间的里间。"
    qian_speaking "那个，请问是——唔——？！"
    show blood0 at cg0 with dissolve
    qian "声音被硬生生地截断。我难以置信地盯着靠近的有力手臂。"
    scene bg_black with fade
    qian "下一秒，我失去了意识。"

    # 【Ending：惊疑】
    $ persistent.ending[10] = 1

    return 


