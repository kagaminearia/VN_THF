label q2_1:
    scene bg_cafe0 with Fade(1,1,1)
    show chiimg closesmile at char_right with easeinright
    chi_speaking "你好~又见面啦，我说的没错吧！"
    show qianimg shirt o at char_left with easeinleft
    qian_speaking "……\n是啊。请问这次的故障问题是什么？现在机器不在这边吗？"

    hide chiimg
    show chiimg o at char_right
    chi_speaking "对呀……出了点意外，可能要晚点才能送过来了，不好意思啊。"
    qian_speaking "嗯，这个没事的……不过，如果不着急的话，可以在东西到这里之后再联系公司，这样也不用麻烦你等在这里。"
    
    hide chiimg 
    show chiimg warm at char_right
    chi_speaking "不麻烦啊，我们可以先做点别的。"
    qian "她捏捏垂下的发尾，面上带笑地看着我，水色的眼眸里就像在闪动真正的水波，名为好奇。\n我有些受不了这样直接的目光，稍稍瞥开了眼睛。"
    
    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "是，是吗……"

    hide chiimg 
    show chiimg laugh at char_right
    chi_speaking "就随便聊聊嘛。\n啊，对了，要不你帮我尝尝这个味道怎么样？"

    hide qianimg
    show qianimg shirt o at char_left
    qian "可是——\n我的话还没说出口，被她递过来的一杯饮料堵住。\n淡淡的香甜气味让喉咙不自觉变紧，到D层之后，我很久没接触过鲜活的食物。\n难以拒绝…"
    
    scene bg_cafe0 with Fade(0.1,0.1,0.1)
    show chiimg close at char_right with easeinright
    chi_speaking "感觉怎么样？"
    show qianimg shirt o at char_left with easeinleft
    qian_speaking "呃，挺好的。"
    qian "我唾弃这样装腔作势，故作深沉的自己，但还是刻意压低了声音，生硬地回应。"
    
    hide chiimg
    show chiimg laugh at char_right
    chi_speaking "太好了，谢谢你！"
    qian_speaking "也没什么……"
    qian_speaking "咦，机器还没送到吗？"

    hide chiimg
    show chiimg o at char_right
    chi_speaking "我看看哦……好像因为别的事情耽误了，大概还要一会儿。"
    
    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "这样啊……"
    qian "我在心里叹了口气，一时间竟然不知道怎么接话，只好又调出那张通行证的信息：剩余时间已经不多。"
    chi_speaking "对哦，好可惜……那只能下次再找人了。\n不过，来A层也要不少时间，为什么不在这边多待一会？这样你们也不用那么辛苦了。"
    
    hide qianimg
    show qianimg shirt sad at char_left
    qian_speaking "……"
    qian "迟玉虽然这么说，脸上却看不出可惜，只是好奇。我突然后知后觉地意识到，自己面对她时感到的不和谐感。"
    qian "一种我以前很熟悉，而现在逐渐消解的天真。"
    qian "面对那汪清澈的浅蓝色湖水，我实在很难回答她。"


    scene bg_room0 with fade
    qian "回到房间，我查看光屏页面的时候，联系人的头像闪了闪，是迟玉发来的消息。"
    # screen mode
    chi_msg "谢谢你今天陪我聊天^_^"
    chi_msg "下次我再找你过来玩吧"
    chi_msg "机器也还没有修好呢"
    qian_msg "好的"
    qian_msg "我会帮你解决问题"
    chi_msg "其实你只要过来陪我待着就好啦"

    show qianimg still at char_mid with dissolve
    qian "……\n她毫不掩饰自己有其他目的——对A层的人来说，随意使用他人的确是一种日常。\n只是，我到D层后才知道原来其他人是不一样的。"
    qian "……似乎有些难受。\n然而我又同时意识到，这对我来说是个极好的机会——迟玉是A区人，对我大概印象不差，看起来天真善良……"
    
    qian_msg "好啊^_^"

    qian "啊，我也终于会这种方式了……"
    chi_msg "待会我还有事"
    chi_msg "那，之后我再找机会让你过来哦"
    qian_msg "嗯嗯^_^"
    nvl clear
    hide qianimg still
    show qianimg o at char_mid
    qian "不过……为什么是找机会？我没有去深究，眼下更重要的是……我似乎已经取得了不错的进展——在和迟玉的接触上。"
    qian "那，之后……？"

    menu:
        "【和她继续保持关系】":
            jump q2_1_1
        "【找她打听家里人的情况】":
            jump q2_1_2


label q2_1_1:
    hide qianimg 
    show qianimg shirt still at char_mid
    qian "不，现在就直接说可能还是太激进了……A层的人不管是谁，在身份上都会对现在的我带来危险。"
    qian "还是先和她保持联系，多接触一段时间，从别的地方观察一下吧……"
    
    scene bg_factory1 with fade
    show qianimg shirt still at char_right with easeinright
    qian_speaking "迟玉……"
    show grey_fem at char_left with easeinleft
    unknown "你啊，在说迟玉嘛？"
    
    hide qianimg
    show qianimg shirt o at char_right
    qian_speaking "啊？是，怎么了……"
    qian "我没想到自言自语会被人听到，还是没说过话的同事，一时有些摸不着头脑。"
    coworker_speaking "就八卦呗，你们小年轻还知道这个人？最近又有她的消息了？那孩子可真是个厉害的……"
    qian_speaking "呃，那个，什么……"
    coworker_speaking "说实在的，年轻人还是要做到她那样啊，D层出生的，一路往上爬到那么高，当记者采访蓝石还能被看中，是真厉害……不过到A层就没消息了，估计也是看不上咱们这。"
    qian "等等，这是什么意思……她和我好像完全不在说同一件事，可……让我很在意。"
    qian_speaking "那是……那是什么时候的事？"
    coworker_speaking "哎？合着你不知道啊？我就说嘛……那你在这嘀咕啥呢？"
    
    hide qianimg
    show qianimg shirt shout at char_right
    qian_speaking "不是！我是听家里人说过，但是没说过具体的事情……"
    coworker_speaking "这样啊，的确是你们的榜样，可以讲讲的。我想想啊……那是二十多年前的事吧，蓝石科技刚做起来，特别厉害，迟玉也抓住了这个机会啊，出了特别多报道。"
    
    hide qianimg
    show qianimg shirt shock at char_right
    coworker_speaking "说实在的，我感觉那报道她没发挥好，不是以前的风格，但人家就是厉害，换了风格也能被蓝石看中，就带到A层去了。然后咱们就不知道喽，不过A层肯定哪哪都好啊。"
    coworker_speaking "不过啊，虽然咱嫉妒，但也得恭喜她……后来D层越来越乱，咱们都快活不下去了，看着有人离开也好啊……"
    coworker_speaking "行了行了，我讲这么多干啥……工作，工作去了。"
    
    hide qianimg
    show qianimg shirt sad at char_right
    qian_speaking "这，这样啊……谢谢……"

    scene bg_factory with Fade(0.1,0.1,0.1)
    qian "……"
    qian "二十多年前，那肯定不是现在的迟玉……她看起来最多也就十八岁吧，和我一样大……可是同样的名字，同样和蓝石有关，怎么看都觉得很奇怪……"
    qian "奇怪了，这似乎和我也没什么关系，为什么想到那张笑脸和那双水蓝色的眼睛，心里还是生出难以言喻的难过。"
    qian "这样的事情，还是不跟她讨论了……\n我本能地，想要隐瞒这件事。"

    scene bg_cafe0 with fade
    qian "阳光明媚，今天荆棘之城的天气设定是晴天。满是落地窗的一层小楼被打理得精致有序，人造光线透过雕花玻璃映出好看的形状，在迟玉的额角留下一抹光晕。"
    qian "我怀念这样久违的，温暖平和的环境，一瞬间竟然看得有些痴迷了。"

    show chiimg at char_right with easeinright
    chi_speaking "你在看什么，有什么特别的吗？"
    show qianimg shirt o at char_left with easeinleft
    qian_speaking "啊，没，就是觉得你这环境挺好的……"

    hide chiimg
    show chiimg close at char_right
    chi_speaking "你喜欢啊？那你多来玩呀。"

    hide qianimg
    show qianimg shirt sad at char_left
    qian_speaking "那不太行啦……"

    hide chiimg
    show chiimg o at char_right
    chi_speaking "是来A层太远太累了吗？"
    qian_speaking "也不算吧，就是，不太方便……"
    chi_speaking "那我就说要维修机器，然后每次找你过来就行了呗。"
    qian_speaking "……所以你根本没想着要我修机器啊。"

    hide chiimg
    show chiimg close at char_right
    chi_speaking "嘿嘿。"
    qian "迟玉眨了眨眼，没有否认的意思，只是笑着看我。裙摆和胸口的的花边随着她一起轻轻摇晃，划出漂亮的旋律，引我想要合唱——但还是止住了任何向外飘逸的想法。"
    
    hide chiimg
    show chiimg closesmile at char_right
    chi_speaking "反正不管用什么理由，能把你叫来就行啦。只要我说一下，又不会有人拒绝我，真的很方便呢！"
    qian "的确，是A区的话，大多数人都不可能会拒绝……\n这对我来说算是好消息，但我却莫名有种堵着的感觉。"
    
    hide qianimg
    show qianimg shirt smile at char_left
    qian_speaking "好啊，那我尽量来找你。"
    chi_speaking "那就很好啦。"

    scene bg_cafe0 with Fade(1,1,1)
    show chiimg o at char_right with easeinright
    chi_speaking "哎，你身上怎么都湿了？快过来我帮你擦一下。"
    show qianimg shirt close at char_left with easeinleft
    qian_speaking "啊不用……啊，呃……谢谢。"
    qian "迟玉围着我转圈，把我身上的水汽都擦掉。柔软的发丝和宽大的裙摆时不时扫过我的皮肤，让我动也不敢动，只是僵硬在原地。"
   
    show cg_chi20 at cg0 with dissolve
    window hide
    pause(1)
    window show
    chi_speaking "你也很喜欢雨吗？不过就算喜欢，也不能特地跑出去淋湿啊。"
    qian_speaking "我可没有特地跑出去……这么大的雨，走在路上就是会打湿的，所以其实没事的，不用帮我擦……"
    chi_speaking "什么啊，不都是有雨雪通道的吗，你不走才会被淋湿啊。"
    qian_speaking "……D层没有那些东西的，总之，不太方便吧……"
    chi_speaking "啊？这样吗？那真的很麻烦诶……"
    qian_speaking "嗯……"
    qian "我的心绪忽然沉下来，这是怎么了……简直就像这天气似的，阴晴不定，叫我感觉麻烦又难受。"

    scene bg_cafe0 with Fade(1,1,1)
    show chiimg sad at char_right with easeinright
    chi_speaking "唉，偶尔我也想自己出去啊，也不用总是找借口让你过来……什么时候会有那一天呢？"
    
    show qianimg shirt o at char_left with easeinleft
    qian_speaking "诶……啊。那个……不能出去么？"
    qian "迟玉那明显不同于平时的情绪令我有些不安，我顿了顿，摸不准她的意思，只好小心地试探。"
    
    show cg_chi30 at cg0 with dissolve
    window hide
    pause(1.5)
    window show
    chi_speaking "是啊，我，我的母亲，她不让我去外面的地方。她说外面太危险了，不适合我，我只要待在家里就好……"
    chi_speaking "可能她也有没告诉我的理由，但我有时候还是会想……啊，我是不是说太多无聊的事了。"
    qian_speaking "怎么会这样……没事，你说什么都可以。"
    qian "我很想说什么，说出的的话却干巴巴的。"
    show cg_chi31 at cg0 with dissolve
    chi_speaking "……所以，你能来这里陪我，我真的很开心。\n谢谢你哦，时茜。至少现在你在这里，我……那个，我很幸运……"
    qian "什么啊……为什么看到她泛红的脸颊，我的面部也隐隐做烧起来……"
    qian "不行，我想要说点什么来转移话题……"
    menu:
        "【衣服好看】":
            scene bg_cafe0 with Fade(0.3,0.3,0.3)
            show qianimg shirt o at char_left with easeinleft
            qian "那个，你的衣服很好看啊，感觉很适合你。"
            qian "许久没有机会说这些话，我十分笨拙地在脑内搜刮恰当的词汇，话题实在生硬。"
            qian "迟玉似乎完全不在意我的卡壳，而是十分开心地接了话。和我不同，她的笑容是如此明朗，不含任何杂质与阴霾，比阳光更甚，驱散我身上的水汽。"
            show chiimg close at char_right with easeinright
            chi_speaking "这是……我妈妈买给我的，很好看吗？"

            hide qianimg
            show qianimg shirt smile at char_left with easeinleft
            qian_speaking "是啊。"

            hide chiimg
            show chiimg closesmile at char_right
            chi_speaking "谢谢你，我也觉得很好看，但还是第一次有别人这么说。"

            show cg_chi40 at cg0 with dissolve
            window hide
            pause(1.5)
            window show
            qian "迟玉站起身转了个圈，裙摆再次跟着她的动作一起跳舞，每个节拍都恰好踩在我心跳的节奏。"
            chi_speaking "时茜，我好开心！"
            qian_speaking "嗯。"
            qian "不自觉，我的语气也被她所感染，变得轻快起来。"
            
        "【眼睛漂亮】":
            scene bg_cafe0 with Fade(0.3,0.3,0.3)
            show qianimg shirt o at char_left with easeinleft
            qian "那个，我一直觉得你的眼睛很漂亮，感觉和这种天气很像，但更好看……啊。"
            hide qianimg 
            show qianimg shirt sad at char_left
            qian "这转折似乎太生硬了些……但我没能继续想下去，因为迟玉的表情突然暗淡了。"

            show cg_chi50 at cg0 with dissolve
            window hide
            pause(1.5)
            window show
            chi_speaking "抱，抱歉……我的眼睛不好看的，可以不要这么仔细看吗……"
            qian_speaking "你怎么会这么想——"
            chi_speaking "真的不好看……\n真对不起，说这些扫兴的话。"
            qian_speaking "没有的事……我没有别的想法，只是想夸你好看。\n我，我是真心的，那个……"
            show cg_chi51 at cg0 with dissolve
            chi_speaking "……真的吗？我的眼睛，不丑吗？"
            qian_speaking "当然不丑！"
            show cg_chi52 at cg0 with dissolve
            chi_speaking "……这样啊。"
            qian "迟玉只是轻轻呢喃，没有继续说话。我顿了顿，心底突然生起勇气。"
            qian_speaking "我！我就很喜欢你……你的眼睛。"
            chi_speaking "那，那个……！"
            show cg_chi53 at cg0 with dissolve
            chi_speaking "……我，我也是……我喜欢，你，你的眼睛。"
            qian "我的耳朵突然开始轰鸣，像是被不真实的泡沫包裹，淹没。虽然不真实，却令人难以逃脱。"
    

    scene bg_cafe0 with Fade(0.3,1,0.3) 
    show chiimg laugh at char_right with easeinright
    chi_speaking "今天我做了新的口味哦，这杯饮料里加了点荆棘花瓣！"
    show qianimg shirt o at char_left with easeinleft
    qian_speaking "荆棘花还能用来做调料吗？嗯……好像没什么特别的味道，挺好喝的。"

    hide chiimg
    show chiimg warm at char_right 
    chi_speaking "第一次尝试啦，因为我很喜欢这朵花嘛。"
    qian_speaking "是哦，听说以前在大家快饿死的时候就是吃荆棘花活下来的，因为有荆棘花和那时候坚持的人才有现在的城市，真的很……"
    
    "叮，叮——"
    hide chiimg 
    show chiimg o at char_right
    chi_speaking "咦，怎么会有人来？啊……"
    hide qianimg
    show qianimg shirt still at char_left
    qian "我的话被突兀的门铃声打断，而迟玉的惊呼让我也不由得开始紧张。余光里的影子在靠近，逐渐和迟玉的影子融为一体。我把脊背用力绷直，假装在认真工作对谈。"
    
    scene bg_cafe0 with Fade(0.1,0.1,0.1)
    show lan0 at char_mid with easeinright
    unknown "这位是？"
    show chiimg sadask at char_right with easeinright
    chi_speaking "啊！她是——"
    show qianimg shirt still at char_left with easeinleft
    qian_speaking "我是来处理订单问题的，刚刚正在讨论……啊，您好。"
    unknown "你好啊，看样子你认识我？"

    hide qianimg
    show qianimg shirt smile at char_left
    qian_speaking "没有人不认识您吧。"
    qian "蓝石，“那个”蓝石——荆棘之城最出名的人物之一，名下有多个科技产业和慈善基金，创造了无数工作岗位，是备受关注的成功人士。"
    hide lan0
    show lan1 at char_mid 
    lan_speaking "哈哈，那就有些夸张了。我早就比不上你们这些年轻人了，来这里工作很辛苦吧，迟玉给你添麻烦了。"
    qian_speaking "没有的事……"
    lan_speaking "现在是还有什么问题吗？"
    hide chiimg
    show chiimg sad at char_right 
    qian_speaking "不，没有……我们基本谈好了。"
    
    hide lan1
    show lan0 at char_mid 
    lan_speaking "嗯。"
    lan_speaking "如果还有别的事情，也尽快解决吧。迟玉……她该休息了。"
    
    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "没有了……那，我就先离开了。"
    qian "不知道是不是我的错觉，和节目上看的不同，蓝石虽然笑得温和，却给人一种无形的压力。也许，是因为我似乎能隐约感觉到……她很想让我快点走。"
    qian "不过，她似乎和迟玉过分熟稔，如果关系亲密，接近迟玉也许可以再和蓝石交好，说不定对我有大帮助……"
    
    hide chiimg
    show chiimg sadask at char_right
    chi_speaking "……要走了吗？"
    hide lan0
    show lan1 at char_mid 
    lan_speaking "是啊，迟玉还有什么事吗？"
    hide chiimg
    show chiimg sad at char_right
    chi_speaking "不……那，拜拜。"
    qian_speaking "……\n感谢您配合我们的工作，如果有问题随时联系公司。…"

    scene bg_city0 with Fade(0.2,0.2,0.2)
    qian "蓝石是生气了吗？会影响到迟玉吗？我还能……见到她吗？\n我的内心突然十分紧张，为什么……一定是因为害怕影响到我之后的工作和计划……"
    show qianimg shirt sad at char_mid with dissolve
    qian "一定是这样……所以才让我现在还想再看她一眼。"
    qian "想到这里，我的脚步顿了顿，才发现自己走得很慢，现在刚离开院子的门口而已。既然这样，那就刚好再看一眼……\n……嗯……？这是……"
    
    scene bg_city0 with Fade(1,1,1)
    with vpunch

    qian "呼……哈啊……因为剧烈跑步，我停下来之后还止不住喘息。血液在血管里高速流动，让我的思绪更加活跃。先前看到的画面在大脑里不断闪回，我无法理解，又忍不住来回回想。"
    show qianimg shirt shock at char_mid with easeinbottom
    qian "那是什么情况？蓝石的动作超出我的预料，我不明白，亲人之间，或者家人之间，应该是那样的吗？……我不懂，甚至，我现在连我自己都不太懂了……为什么我要那么着急跑开？为什么我会难受？"
    
    show cg_chi60 at cg0 with Fade(0.2,0.9,0.2)
    show cg_chi61 at cg0 with Fade(0.2,0.9,0.2)
    show cg_chi62 at cg0 with Fade(0.2,0.9,0.2)
    show cg_chi63 at cg0 with Fade(0.2,0.9,0.2)
    show cg_chi64 at cg0 with Fade(0.2,0.9,0.2)
    show cg_chi65 at cg0 with Fade(0.2,0.9,0.2)
    pause(1)

    scene bg_city0 with Fade(0.3,0.5,0.3)
    with vpunch
    qian "胃部感到难受，像是什么东西搅在一起，有些酸，有些痛……\n到最后，所有的思绪融化成下意识的自言自语。"
    qian "……\n迟玉……"

    scene bg_factory1 with fade
    show stf at char_left with easeinleft
    unknown "时茜小姐，有人找你。"
    show qianimg shirt o at char_right with easeinright
    qian_speaking "什么？"
    qian "我惊讶于别人礼貌的口气，也不认为到了D层之后，会有什么人特意来这里找我。\n但听到那人的名字后，不知道为何，一种“果然”的感觉油然而生。"
    hide qianimg
    show qianimg shirt still at char_right
    qian_speaking "好，我知道了。"
    qian "蓝石……默念这个名字的时候，我的心底泛上一阵莫名的疼痛，说不清楚，却令我难受不已。"
    show cg_chi65 at cg0 with Fade(0.1,0,0.1,color="#ffffff")
    pause(0.5)
    hide cg_chi65
    qian "脑袋控制不住地涌上回忆的景象，不断靠近的身体，抚摸，触碰，如提线木偶般的动作，往下，向上。"
    qian "一边是我从小尊敬的人，一边是……迟玉——我不知道，该如何形容她——不论是谁我都不想有不好的猜测。可现在，我的思绪却持续飘得越来越远，越来越乱。"
    qian "迟玉……你为什么？"
    unknown "您在听吗？"
    hide qianimg
    show qianimg shirt o at char_right
    qian_speaking "啊，不好意思……蓝石女士她，现在在外面是吗。"
    unknown "不是，但她需要你去一个地方。"
    hide qianimg
    show qianimg shirt still at char_right
    qian_speaking "好的……"

    scene bg_lanroom with Fade(0.3,0.3,0.3,color="#fff")
    qian "这是个宽敞整洁的封闭房间，家具是统一的银白色，摆放得整整齐齐。我有些局促地站在门口，和周围格格不入。\n私人载具竟然能有这么大位置，不愧是蓝石科技……"
    show qianimg shirt o at char_left with easeinleft
    qian_speaking "那个……"
    show stf at char_right with easeinright
    unknown "请在里面等一会，之后会有人来找你。"
    qian_speaking "好的……"
    hide stf with easeoutright
    hide qianimg
    show qianimg shirt still at char_left
    qian "门关上了，只剩死一样的安静。我有些不安，不知道即将到来的是什么。\n……是因为发现我看到了那件事吗？还是因为认出了我，会说什么吗？"
    qian "……"
    unknown "茜……时茜……"
    hide qianimg
    show qianimg shirt o at char_left
    qian_speaking "……谁？是有人在叫我吗？……我——唔唔唔！！"

    show cg_chi70 at cg0 with dissolve
    window hide
    pause(1.5)
    window show
    chi_speaking "小声点……你果然在里面啊。"
    qian_speaking "你怎么来了？！怎，怎么了吗？"
    chi_speaking "我——我想见你。"
    qian "……什么？\n那一瞬间，我的大脑有些空白，无法理解这语句的含义。从耳郭开始，热意向内扩散，烧得我脑袋嗡嗡作响。"
    
    scene bg_lanroom with Fade(0.1,0,0.1,color="#fff")
    show qianimg shirt sad at char_left with easeinleft
    qian_speaking "那，那个，什么意思……呃，你，我……"
    show chiimg sad at char_right with easeinright
    chi_speaking "呼……累死我了……我，好不容易过来……"
    hide chiimg
    show chiimg sadask at char_right
    chi_speaking "那个，啊……你相信我吗？"

    hide qianimg
    show qianimg shirt still at char_left
    qian "——你相信我吗？\n没头没尾，如此突兀的一句话。"

    hide qianimg
    show qianimg shirt shout at char_left
    qian_speaking "等等，那是……什么意思啊？"

    hide chiimg
    show chiimg sad at char_right
    chi_speaking "没什么啦，我只是突然好奇……不过你就告诉我吧……你会吗？不管我说什么……你会相信我说的话吗？你会相信我吗？"
    
    hide qianimg
    show qianimg shirt shock at char_left
    qian "这……\n我从未见过迟玉这样的表情。\n她并不说别的，只是直直地盯着我，仿佛非要我说出一个结果。"
    qian "我……"
    menu:
        "【相信她】":
            jump q2_1_1_1
        "【不相信她】":
            jump q2_1_1_2


label q2_1_1_1:
    scene bg_lanroom with fade
    show qianimg shirt still at char_left with dissolve
    qian_speaking "……我知道了……我相信你。"
    show chiimg sadask at char_right with dissolve
    chi_speaking "真的吗？你一定会相信我吗？真的会吗？"
    hide qianimg
    show qianimg shirt smile at char_left
    qian_speaking "嗯，我会的。"

    qian "说实话……我不太明白现在的情况。但迟玉的眼神令我无法拒绝——那就像一只受伤的小动物，非常需要肯定和安抚。"
    qian "于是我就会这么做。"

    hide chiimg
    show chiimg sad at char_right
    chi_speaking "谢，呜……谢谢你。"

    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "所以……是有什么事呢？"

    hide chiimg
    show chiimg sadask at char_right
    chi_speaking "啊……\n那个，那个啊……\n……现在，从这里逃跑吧？"
    
    hide qianimg
    show qianimg shirt sad at char_left
    qian_speaking "……什么？"
    chi_speaking "你说了你会信我的！"
    qian_speaking "我，我是相信你但是……为什么啊？"
    qian "迟玉似乎处在高度紧张的状态中，我稍有疑问就即将爆发。被她的情绪影响，我也变得紧张起来。"
    
    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "况且，就算要跑我也不知道怎么做啊……我不了解，但这里似乎也是到处有人在管的吧……"
    
    hide chiimg
    show chiimg sad at char_right
    chi_speaking "啊，这个……"
    qian_speaking "所以到底怎么了？"

    hide chiimg
    show chiimg sadask at char_right
    chi_speaking "那个啊……我觉得……我，不，蓝石可能会对你做不好的事……"

    hide qianimg
    show qianimg shirt sad at char_left
    qian_speaking "……是因为那个吗？因为我看到你们在，那个……"
    qian "虽然我真的被吓到了，但是就因为那个也不至于吧……正当我想的时候，却看到迟玉的脸色变得煞白。\n等等……难道不是那件事？"
    
    hide chiimg
    show chiimg afraid at char_right
    chi_speaking "那，那个……你别说……不要，说出来……"
    qian_speaking "对不起，我没有那个意思……我不说了，你说吧，刚刚你的话应该还没说完吧？"
    
    hide chiimg
    show chiimg sad at char_right
    chi_speaking "嗯，嗯……好。我也是，对不起……之前她，蓝石问我的时候，我觉得奇怪，就去查了一下你的信息……她们好像有关系，而且不太好……"
    
    hide qianimg
    show qianimg shirt still at char_left
    qian "迟玉说得前言不搭后语，磕磕巴巴，断断续续。但我仍然捕捉到那个最重要的地方——蓝石和我家的事有联系，和管理局报告的也是她。"
    
    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "别紧张……没事的。就算，就算蓝石会以此要挟我，那也可以谈条件试试啊……要钱或者别的，都，都没关系——"
    
    hide chiimg
    show chiimg afraid at char_right
    chi_speaking "不，不是这样的……！"
    qian "也就是说……我现在的处境，蓝石就是唯一元凶……"
    qian "我不想相信蓝石会做出那种事，可没有反驳的证据，因而说话也完全没有底气。可迟玉听完却更加紧张，几乎有些惊恐地打断我的话。"
    
    hide chiimg
    show chiimg sadask at char_right
    chi_speaking "不是那样……你，啊……过来一下！"

    hide qianimg
    show qianimg shirt shock at char_left
    qian_speaking "啊？喂——"

    scene bg_darkroom with Fade(1,1,1)
    qian_speaking "这，这是……"
    qian "就在刚才，她直接摸上中央长桌上的屏幕，而后一声轻响，这个本来就很大的房间里，竟然又打开了一扇门。"
    show cg_wall at cg0 with dissolve
    qian "墙上贴满了大大小小的照片，无一例外，全是黑发黑眸的少女。\n——和迟玉长得一模一样。"
    qian "我的心里突然出现荒谬又合乎情理的猜测。\n或许这就是，那个“迟玉”……"
    
    scene bg_darkroom with Fade(0.2,0,0.2)
    show chiimg afraid at char_right with easeinright
    chi_speaking "……那个，这边……"
    show qianimg shirt sad at char_left with easeinleft
    qian_speaking "啊，这是什么东西，文件吗……人类，定制计划？等等，你还好吗？"
    qian "迟玉从进门就开始颤抖，一系列的反常让我连这庞大的信息量也顾不上，生怕她出什么事。"
    
    hide chiimg
    show chiimg sad at char_right
    chi_speaking "真的，没事……我只是不太喜欢这里……"

    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "是，是啊……这里都没什么光线，有点压抑……你经常来这里吗？"
    chi_speaking "我，我……不是，蓝石，蓝石她会叫我来……"
    qian "……她们到底发生了什么？我扶住迟玉，她柔软的头发无序地散开，视线透过缝隙，落在墙上的照片上。\n难道……"
    
    hide qianimg
    show qianimg shirt sad at char_left
    qian_speaking "蓝石她……她是，你妈妈？"
    hide chiimg
    show chiimg sadask at char_right
    chi_speaking "……是，的……"
    hide qianimg
    show qianimg shirt shock at char_left
    qian "竟然真的是这样！我震惊无比，重新仔细地朝着那些照片看去，可……"

    hide qianimg
    show qianimg shirt sad at char_left
    qian_speaking "这些照片……是你吗？"

    hide chiimg
    show chiimg sad at char_right
    chi_speaking "不是我……\n这是，另一个迟玉……是，我要成为的迟玉……"
    qian_speaking "果然……那是什么意思？眼睛颜色不同，但其他都……"
    hide chiimg
    show chiimg afraid at char_right
    chi_speaking "果然我不像吗……？因为我不好看吗？我要怎么才……不，不对……\n对不起，我有些乱了，你不要管我……我先，关掉通知系统，至少能多点时间……"
    qian_speaking "我，好，你……你别着急…… "
    qian "迟玉显然有些受到刺激，我只好先让她自己缓一缓，而我拉过台灯照明，继续刚才没读完的文档。\n人类定制……不知为何，这个组合起来的名词让我感到难受。"
    
    nvl_mode "人类定制。目标：迟玉"
    nvl_mode "现存实验：外表略有差距，已有进步，性格差距过大。可用，仍是失败品"
    nvl_mode "外表：将已有基因插入受精卵，控制遗传\n将于……提供怀孕条件"
    nvl_mode "记忆：对大脑进行改造，需要提取/注入记忆\n可利用D层……装置实验……"
    nvl_mode "注：可能会导记忆混乱或大脑损伤；及时更换实验品"
    nvl_mode "……"
    nvl_mode "重大失误，黄……需提取她们曾经……以及实验记录，继续研究……"
    


    qian "快速扫过文档，杂乱的手稿和大量的信息让我有些怔愣。\n所以，从照片来看……蓝石是老板，迟玉是实验品……？然后，我家里人参加了这个项目，之后就没有消息……"
    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "这都什么跟什么啊……蓝石到底做了什么，她为什么要这么做……"
    unknown "要不要试着猜一下？"
    hide qianimg
    show qianimg shirt shock at char_left
    qian_speaking "什么都不知道怎么猜……\n！！！"
    show lan0 at large2 with easeinbottom
    qian "我猛地转过头，只见不知道什么时候，蓝石正站在房间的门口，微笑看着我和角落里的迟玉。"
    
    scene bg_darkroom with Fade(0.1,0,0.1)
    show qianimg shirt shock at char_left with dissolve
    qian "什么时候来的……我毛骨悚然，放在台灯把上的一只手开始颤抖，灯光也跟着摇曳。\n没人说话，房间里安静得像一具棺材，我吞口水的声音也变得突出。"
    show lan1 at char_mid with easeinright
    lan_speaking "怎么了？不是还有话要说吗？"
    hide qianimg
    show qianimg shirt still at char_left
    qian "难以想象，仅仅是短短几分钟，我对蓝石的印象已经发生巨大改变。此时此刻，没有先前的激动，只有恐惧。"
    qian "也许这就是所谓的气势，只有面对面才能感受到……她的语气像开玩笑，我却几乎喘不过气。\n怎么办……怎么办，现在应该——"
    menu:
        "【拖延时间】":
            jump q2_1_1_1_1
        "【趁她不注意冲出去】":
            jump q2_1_1_1_2


label q2_1_1_1_1:
    scene bg_darkroom with Fade(0.1,0,0.1)
    show lan0 at char_right with easeinright
    show qianimg shirt still at char_left with easeinleft
    qian "我还是不知道到底是什么情况，但不管怎么样……先尽可能拖延时间。\n我侧过身半挡在迟玉身前——就算要做什么，也是两个人胜算更大。"
    qian "除了没意识到蓝石的动静，事实上，我也没有听到迟玉的动静……她还好吗？那个角落，就如死一般寂静……只好见招拆招了。"
    hide qianimg
    show qianimg shirt shout at char_left
    qian_speaking "……真的可以让我猜吗？那，从哪件事开始猜比较好？"
    lan_speaking "随你吧。我还是有时间听你讲点废话的。"
    hide qianimg
    show qianimg shirt still at char_left
    qian_speaking "……好。\n迟玉，和你是什么关系？家人吧，母女？……这些照片是谁？不是迟玉吧……为什么，是一样的？另一个又是谁？"
    qian "我努力搜刮词汇，试图吸引她的注意，希望她不要注意我轻推迟玉的动作……\n直到靠近，我才发现这具身体正在剧烈颤抖。"
    lan_speaking "猜得不好，只有基础知识。\n对了，你找迟玉帮忙？她可不会听你的。"

    hide qianimg
    show qianimg shirt shock at char_left
    qian_speaking "怎么，会……所以你对她做了什么？和墙上的照片有关？"
    hide lan0
    show lan1 at char_right
    lan_speaking "说什么呢。迟玉是个听话的孩子啊，在这里当然只听我的话了。"
    hide qianimg
    show qianimg shirt still at char_left
    qian "嘶……我的想法被轻易看透，她似乎只是像看戏一样等我进行下一步。\n但到底怎么回事……迟玉，蓝石，到底我应该……"
    qian_speaking "……"
    lan_speaking "不然你问问她？\n迟玉，抓住你前面的那个人。"
    show chiimg black at char_mid with easeinbottom
    hide qianimg
    show qianimg shirt shock at char_left
    qian_speaking "什——呜！"
    qian "糟……！\n——！\n迟玉的声音骤然放低，我就知道事情不对，但还是来不及……一双手臂从后面伸出来，用力箍住我的胸口。"
    
    show cg_chi80 at cg0 with dissolve
    window hide
    pause(2.3)
    window show
    chi_speaking "对不起，我必须……\n我必须听蓝石的话，不然，不然……"
    qian_speaking "……你为什么非要这么做？！喂……！迟玉！蓝石！"
    lan_speaking "我只是可以做，就做了而已。她是我的东西，轮不到你说。"
    lan_speaking "也该差不多了吧，嗯，让我看看，怎么还没人来解决你们。"
    qian "不行，不知道她要做什么，但是马上就要没时间了……必须要做点什么，打乱她的节奏……"
    menu:
        "【劝说迟玉】": # ending here
            scene bg_darkroom with Fade(0.1,0,0.1)
            show qianimg shirt shock at char_left with dissolve
            show chiimg black at char_mid with dissolve
            qian_speaking "迟玉……迟玉……！放开我！"
            chi_speaking "……"
            show lan1 at char_right with easeinright
            lan_speaking "别挣扎了，乖乖等着。"
            qian_speaking "……迟玉……求求你，别抓着我了……你不是说要一起逃跑的吗……"
            hide lan1 with moveoutright
            qian "蓝石似乎出去接人了，只留下我和死死抓住我的迟玉。以前看不出来，她的力气竟然这么大，我除了能转头，其他完全动不了。"
            chi_speaking "对不起，对不起……我是失败品，我必须要听蓝石的话……不能反抗，会被惩罚的……对不起，对不起……"
            qian_speaking "迟玉……"
            scene bg_black with Fade(0.1,0,0.1)
            with vpunch
            qian "颤抖，剧烈的颤抖。被她用力挟着，那仿佛刻骨的压抑情感也排山倒海般席卷而来。\n被这样的气势压制，我竟一时忘了做出反应。"
            qian "以至于直到脚步声近在身后，我才察觉。"
            qian "这样啊……我到底还是太弱小了。"
            qian "……"
            qian_speaking "……迟玉，还是谢谢你。"
            qian "……"

            # 【Ending：可惜】
            window hide
            show screen ending_title(number=4) with Fade(0.5,0.5,0.5)
            pause
            $ persistent.ending[4] = 1

            return 

        "【劝说蓝石】": # ending here
            scene bg_darkroom with Fade(0.1,0,0.1)
            show qianimg shirt shock at char_left with dissolve
            show chiimg black at char_mid with dissolve
            qian_speaking "……对了，我们本来是要做什么事？"
            show lan1 at char_right with easeinright
            lan_speaking "难为你还记得，可你这样不守规矩，还想着别人原谅吗？"
            hide qianimg
            show qianimg shirt shout at char_left
            qian_speaking "那个……你还和我家里人有联系的吧……你想要什么的话，让我们联系上，我们都可以尝试给你的……"
            lan_speaking "别想了，我不需要你想的那些东西。"
            qian_speaking "不需要你也不用再继续找她们了啊！为什么非要现在这样，我什么都不会说出去的……"
            lan_speaking "是吗？的确很可惜。"
            qian_speaking "可惜什么啊……"
            lan_speaking "她们已经死了，虽然不是我杀的。"
            hide qianimg
            show qianimg shirt shock at char_left
            qian_speaking "……\n你说什么？"
            qian "……\n……\n……"
            qian "我从未想过，这个时候会突然出现这样一句话，就像葬礼上突然出现小丑一样荒诞而不合时宜。\n我无法理解，拒绝理解这句话。"
            lan_speaking "唉，真是可怜。本身这么脆弱，何必还要去管太多？"
            qian_speaking "……"
            lan_speaking "说过了吧，就乖乖听话不好吗。"
            qian_speaking "……\n才不是，不是这样的……就算那样，我想要知道真相……我想知道，你这么做的理由！"
            lan_speaking "可惜了。"
            qian_speaking "可惜什么……"
            qian "有些嘈杂的声音从门外传来，一晃眼的时间里，几个高大的女人围住了我们。"
            scene bg_black with Fade(0.1,0,0.1)
            with vpunch
            qian "这样啊……原来是在可惜我来不及了。"
            qian "……"
            qian "……"

            # 【Ending：可惜】
            window hide
            show screen ending_title(number=4) with Fade(0.5,0.5,0.5)
            pause
            $ persistent.ending[4] = 1
            
            return


        "【其他】":
            jump q3_1


label q2_1_1_1_2: # ending here
    scene bg_darkroom with Fade(0.1,0,0.1)
    qian "她在等我回答，现在直接冲出去或许能达到出其不意的效果……至少先离开这个地方——"
    qian "我咬咬牙……走——！"
    lan_speaking "——嗯？"
    show bg_black with shake
    qian_speaking "哈……呃——！！！"
    show bg_black with shake
    "砰！"
    scene bg_darkroom with Fade(0.1,0,0.1)
    qian "发生了什么……好痛……\n我的大脑无法处理过量讯息，只剩下铺天盖地的疼痛。"
    show lan1 at large2 with easeinbottom
    lan_speaking "没死吧？年轻人身体有点差啊。"
    qian_speaking "喂，你……咳……这是违规的吧？！"
    lan_speaking "自然不是，电流值在安全范围内。"
    qian "疯了吧……我震惊地盯着她手里的电击器，身体的本能驱使我想要逃跑，可连后退都做不到。\n我全身无力，只能勉强靠手臂支撑身体。"
    lan_speaking "可惜了，真是不听话。"
    qian_speaking "你，咳，到底要做什么啊……迟玉，你都不在乎她的吗？！"
    lan_speaking "……\n谁知道呢？跟你没关系。"
    lan_speaking "别害怕成这样，我可不会亲自杀人。\n只需要你先睡一觉，之后就好了。"
    qian_speaking "不，别，不要……别这样……呜……啊啊啊啊——"
    show bg_black with shake
    "……\n……"
    scene bg_black with Fade(0.1,0,0.1)
    qian "……\n又一次全身的疼痛让我眼前一黑，然后，我什么都感觉不到了。"


    # 【Ending：麻痹】
    window hide
    show screen ending_title(number=3) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[3] = 1
    return


label q2_1_1_2: # ending here
    show cg_chi65 at cg0 with dissolve
    pause(2)
    hide cg_chi65

    qian "脑海里忽然又蹦出之前的画面……我不由得在心里质问自己，我真的可以吗？真的可以……就这样相信她吗？"
    scene bg_lanroom with Fade(0.1,0,0.1)
    show qianimg shirt sad at char_left with dissolve
    show chiimg sadask at char_right with dissolve
    qian_speaking "那个，我……"
    hide chiimg 
    show chiimg sad at char_right
    chi_speaking "……\n我知道了……抱歉，我这个要求果然很不合理吧……"
    qian "我的话没能说完，但显然她已经明白答案。"
    hide qianimg 
    show qianimg shirt still at char_left
    qian_speaking "对不起……"
    hide chiimg 
    show chiimg sadask at char_right
    chi_speaking "没，没事……那个……啊。"
    show lan1 at char_mid with easeinbottom
    qian "开门声打断了迟玉。\n门口站着的是蓝石，她挑了挑眉，似乎心情很好地开了个玩笑。"
    lan_speaking "哎呀，我来得不是时候，打扰到你们说话了吗？"
    hide chiimg 
    show chiimg afraid at char_right
    chi_speaking "没！没有……"
    hide qianimg 
    show qianimg shirt smile at char_left
    qian_speaking "您好，我们正在等您呢。"
    lan_speaking "让你久等了，不过，迟玉好像今天还有别的事情吧，怎么也过来了？"

    hide chiimg 
    show chiimg sad at char_right
    chi_speaking "那个……"
    lan_speaking "我知道你关心朋友，但也不用急这一会是不是？我们聊一些她家里的事，也不好让迟玉一起听吧？"
    hide chiimg 
    show chiimg sadask at char_right
    chi_speaking "我……"

    hide qianimg 
    show qianimg shirt o at char_left
    qian_speaking "对呀，你要是有事，还是先去做你的事情吧。"
    qian "听到蓝石的话，我印证了猜测，顿时有些坐不住——果然，能接触到蓝石对自己是有帮助的，说不定，很快就能有她们的消息……"
    
    hide chiimg 
    show chiimg sad at char_right
    chi_speaking "……\n好。"
    chi_speaking "时茜……谢谢你。"
    hide qianimg 
    show qianimg shirt still at char_left
    hide chiimg with moveoutright
    qian "嗯……？为什么，突然……\n但迟玉没有再说什么，只是深深地看了我一眼，而后从房间里离开了。"
    qian "她……没事吧？希望没事吧……\n我很快把这件事暂时抛在脑后，因为别的事让我更加在意。"
    
    scene bg_lanroom with Fade(0.1,0,0.1)
    show lan0 at char_right with dissolve
    show qianimg shirt o at char_left with dissolve
    lan_speaking "时茜是吧？我之前问过迟玉，就觉得有些熟悉，关于你家里的事情……你自己有什么想法吗？"
    qian_speaking "那个，我也不知道，但是……"
    lan_speaking "唉，说来你也真是不容易，还年轻呢，就遇上这些麻烦事。你之前是不是还找过别人？有没有人跟你说过什么？"
    qian_speaking "我之前……"
    qian "没有比这更合适的机会了。蓝石是A层的，又是这么厉害的人，说不定在管制局那里也会有办法……我一五一十地把事情的过程告诉她，这才发现喉咙已经僵硬到干哑。"
    
    hide lan0
    show lan1 at char_right
    lan_speaking "别紧张，喝点水，休息会吧。"

    hide qianimg 
    show qianimg shirt smile at char_left
    qian_speaking "谢谢您……"
    qian "我仍然有些紧张，手指摩挲着杯檐，心脏仿佛快要跳出。"
    qian "不，不对，不只是心脏，我整个人都绷紧了，连嗓子也收紧得几乎要喘不过气……真的是因为紧张吗，这……啊啊……"
    
    show bg_lanroom with shake
    qian "视线忽然有些涣散，我抓着杯子的手一松，掉在桌上发出哐当的巨响，在封闭的房间里格外刺耳。"
    
    hide qianimg 
    show qianimg shirt sad at char_left
    qian_speaking "对，对不起……"
    lan_speaking "不必在意。"
    qian "蓝石仍然是笑着，丝毫没有被我的失态所影响。不知为何，她那毫无破绽的微笑此时此刻却让我有些发凉。"
    qian_speaking "啊，嗯……"
    hide qianimg 
    show qianimg shirt close at char_left
    qian "我几乎已经发不出声音，呼吸也变得无比困难。"
    lan_speaking "好好休息吧。"
    hide qianimg 
    show qianimg shirt shock at char_left
    qian "什么……\n……\n……"
    scene bg_black with fade
    qian "眼前一黑，我失去了意识。"
    
    # 【Ending：突刺】
    window hide
    show screen ending_title(number=2) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[2] = 1
    return


label q2_1_2: # ending here
    scene bg_room0 with fade
    qian "这么说来，正好可以问问家里人的情况，不知道黄女士和钟女士怎么样了……\n我稍微思虑一下，便下定决心，打开和迟玉的对话框。"
    
    qian_msg "如果方便的话，能向你打听个人吗"
    qian_msg "也是A区的，我想你可能会熟悉"
    chi_msg "没问题，你告诉我吧"
    chi_msg "其实我也不认识什么人，不过我会帮你问到的^ ^"
    qian_msg "谢谢你！"
    qian "无论如何，至少这句话我是发自真心……我还真是卑鄙。"

    scene bg_room0 with fade
    qian "没有新的消息。"
    qian "自从那天过后，迟玉就没有再回复过我，我心里焦虑，却没法跟别人说，更没办法直接催她，只好每天数着数过日子。"
    qian "但我没想到，在她之前，有其他人先行找上门。"

    scene bg_factory with fade
    show stf at char_right with moveinright
    stf_speaking "时茜小姐，有人找你。"
    show qianimg shirt o at char_left with moveinleft
    qian_speaking "什么？"
    qian "我惊讶于别人礼貌的口气，也不认为到了D层之后，会有什么人特意来这里找我。\n那人的表情变得有些微妙，罕见地沉默一会，才继续说。"
    stf_speaking "蓝石找你，你怎么会认识那样的人？"
    hide qianimg 
    show qianimg shirt sad at char_left
    qian "蓝石？\n是“那个”蓝石。我当然知道是哪个蓝石。\n荆棘之城最出名的人物之一，名下有多个科技产业和慈善基金，创造了无数工作岗位，是备受喜爱的成功人士。"
    qian "竟然是她？她怎么会来找我？难道说……我蓦地想起那个轻盈的身影。\n迟玉最近没有回复，是真的去帮我联系人了吗？"
    qian "我虽然报着不纯的心思，但完全没想过她真的会帮我……那可是蓝石啊，她一定有办法。"
    hide qianimg 
    show qianimg shirt still at char_left
    qian "激动？害怕？欢喜？感激？我说不清是什么心情，只剩下混乱。"

    scene bg_factory with fade
    show lan0 at char_right with dissolve
    show qianimg shirt smile at char_left with dissolve
    qian "头发像丝绸垂于身侧，岁月在她身上留下美妙的痕迹，举手投足皆是气韵，绘成美丽的画卷。\n我第一次亲眼看到，这是，蓝石……"
    qian_speaking "您好。"
    qian "我拘谨地捏了捏手指，难以想象自己会感到“窘迫”。但在她这样的人面前，即使我现在还在A区也许也会做出相同的反应。"
    lan_speaking "你好。\n年轻人真有精气神啊，你就是时茜吗？"
    qian_speaking "是的，那个，请问您是认识……"
    qian "我有些失态，完全不等铺垫就已经下意识急忙开口。但即使我有些失礼，她还是笑眯眯地看着我。"
    lan_speaking "我都听说了，是家里人的事吧？难为你这么操心了。我还算是有点人脉，要不然还真不知道怎么办。她们的事情你还有找别人问过吗？有没有试过其他方法？"
    hide qianimg 
    show qianimg shirt sad at char_left
    qian_speaking "没有，我一直不知道该怎么办，现在找人也是想着撞运气……"
    lan_speaking "这样啊，真是辛苦你了。不过你也不用太担心，我们一起去她们工作的地方看看吧，说不定就能有线索呢。"
    hide qianimg 
    show qianimg shirt shock at char_left
    qian_speaking "啊，真，真的可以吗？！"
    lan_speaking "毕竟我有一点人脉嘛。"
    hide qianimg 
    show qianimg shirt close at char_left
    qian_speaking "谢谢，谢谢您……"
    qian "我几乎有些语无伦次了，但她只是温和地对我笑，简直就像……在看家里的晚辈一样。"

    scene bg_lanroom with fade
    qian "蓝石的交通工具是特别定制，样式简约，细看却全是设计。我几乎是怀着忐忑的情绪跟在她的身后。"
    show lan0 at char_right with dissolve
    show qianimg shirt still at char_left with dissolve
    lan_speaking "怎么了，紧张？是有什么想说的吗？"
    qian_speaking "嗯，那个……"

    menu:
        "【问家里人】":
            $ q2121 = True
            qian_speaking "那个，您觉得我什么时候能见到我家人呢？"
            lan_speaking "这个啊……没事，你们很快就会团聚了。"
            hide qianimg 
            show qianimg shirt o at char_left
            qian_speaking "真的吗？那太好了！谢——诶？"
        "【问迟玉】":
            $ q2121 = False
            qian_speaking "您知道……迟玉怎么样了吗？那个，应该是她帮我联系您的吧，所以……"
            lan_speaking "……\n她很好。"
            hide qianimg 
            show qianimg shirt o at char_left
            qian_speaking "这样啊，那太好了，她一直没找我，我还有点担心呢。"
            lan_speaking "没事，你以后就不用担心了。"
            qian_speaking "诶，好，真是麻烦您了……那——啊？"

    hide qianimg 
    show qianimg shirt shock at char_left
    qian "我剩下的话没能说出口——剧烈的疼痛占据了一切注意力。"
    qian_speaking "怎，回事……啊啊……"
    scene bg_lanroom
    show blur with shake
    qian "疼痛……我颤抖地捂住痛感的来源，湿漉黏糊的触感尽数从心口涌出，向外蔓延。\n到底，怎么回事……"
    show blur with shake
    qian "剧烈的疼痛让我眼前发黑，我感到无法呼吸，每个动作都在刺激更多的疼痛。飞溅的血液和漫溢的泪水混合，让一切变得一团糟。"
    qian "视线抽动，我用尽力气调动脖颈的肌肉，看向身侧——这个空间里除了我的唯一存在，蓝石站在那里。"
    show lan0 at large2 with moveinbottom
    qian_speaking "您……"
    lan_speaking "怎么了？"
    qian_speaking "为，什么……"
    hide lan0
    show lan1 at large2
    qian "液体模糊了眼睛，我只能看到蓝石那一如既往的，温和的笑容。"
    if q2121:
        lan_speaking "我不是说过了吗……你们很快就会团聚了。"
    else:
        lan_speaking "我不是说过了吗……以后就不用你担心了。"
    

    # 【Ending：安心】
    window hide
    show screen ending_title(number=1) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[1] = 1
    return
    