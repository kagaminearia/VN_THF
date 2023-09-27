label q1_2:
    scene bg_street with fade
    qian "不规则的建筑物互相挤压，只在少数地方留下狭小空隙。\n缝隙冰冷阴森，又黑又脏，除了终端上的荧光，什么也看不见。"
    qian "实在不相信这是城市的一部分……我暗自憋闷，随着路牌穿过一道尤其狭长的窄道。"
    scene bg_road02 with fade
    qian "或明或暗的展牌和灯条挂在屋檐，架子，和线缆上，几乎摇摇欲坠。它们不够亮，却撒得到处都是，一闪一闪，投下杂乱晃眼的光晕和阴影。"
    qian "时不时有人影擦肩而过，瞥我一眼，又匆匆离开。\n四周皆是嘈杂，窸窸窣窣，眼花缭乱，令我迷失方向。"
    qian "……好热闹。\n我再次确认时间，现在是凌晨两点。好热闹，和A层的安宁一点也不一样。"
    qian "我却更加茫然——没有认识的人，没有认识的路，连墙面上乱七八糟的涂鸦都像是什么咒语暗号，我也看不懂。"
    qian "终于，我的视线扫到一块亮闪闪的招牌，写着熟悉的文字：\n“酒吧”。"

    scene bg_bar0 with fade
    show bar_fem at char_right with dissolve
    show qianimg o at char_left with dissolve
    short_speaking "怎么了，不再说说你的事情吗？还很难过吧？"
    hide qianimg
    show qianimg still at char_left
    qian_speaking "没事……我只是觉得，跟你说这么多真的好吗？"
    short_speaking "这有什么，事情发泄出来就好多了。对了，也再喝点酒吧，会让你更开心一点哦。"
    qian_speaking "谢谢……"
    qian "她的确是个好人……我原本以为酒吧都是清幽的，放点歌，聊天玩闹而已。谁知道这里尽是浓郁的酒气和汗味，吵吵嚷嚷，还有直接摊在地上的，真是好没素质。"
    qian "好不容易找到个能坐的地方，那些人却只对我哄笑，并不理我，只有温柔地问我发生了什么，她还请我喝酒。"
    qian "不，我想说的不是这个……为什么我会和陌生人聊这么多，还跟着喝了酒呢……\n也许是这个人的话戳中了我，也许是我当真很需要一个借口。也许……"
    
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "……等等，那边怎么了？"
    show bg_bar1 with dissolve
    pause(1)
    hide bg_bar1
    short_speaking "嗯？只是跟我们一样在聊天而已啊，怎么了？还是不要去打扰别人吧，我们再喝点呗？"
    qian "冰凉的液体灌入喉管，令人感到酥麻。酸甜口味，带有些微辣意，我才喝两口就觉得一股气直冲脑门，有些晕乎。"
    hide qianimg
    show qianimg still at char_left
    qian_speaking "是这样吗……总觉得……"
    short_speaking "反正你不用担心啦，来这里的人都是找乐子的。"
    qian "但，那个女生看起来和其他人不是一起的啊，好像也不是很愿意……"

    menu:
        "【无视】":
            jump q1_2_1
        "【插手】":
            jump q1_2_2

label q1_2_1: # ending here
    scene bg_bar0 with Fade(0.1,0.1,0.1)
    show bar_fem at char_right with dissolve
    show qianimg still at char_left with dissolve
    qian_speaking "那……好吧。"
    qian "我还是被面前的人说服了，毕竟，我也没有什么理由直接冲过去啊。\n虽然，还是觉得哪里怪怪的……"
    short_speaking "你知道就好啦，那我们再一起喝点吧！"
    hide qianimg
    show qianimg still at char_left
    qian_speaking "呃，好，好……"
    qian "一杯，又一杯，还有……\n脑袋更加昏沉了，已经分不清上下左右……嗯嗯，不对，我好像是在趴着……"
    show blur with dissolve
    qian "耳边变得朦胧起来，眼前好像也出现幻觉，出现那两个人的身影，成为模糊的景象。原来过度思念，真的会让人产生疾病……"
    qian "……不，不对，太晕了，几乎要对身体失去控制……虽然想到这里，我却完全动不了……！"
    qian "怎么回事……"
    scene bg_black with fade
    unknown "不错啊，终于熬到药效开始了。"
    qian "失去意识前，这是我听到的最后一句话，隐隐约约的，如鬼魅般飘进我的耳朵。"

    # ending
    return


label q1_2_2:
    hide bar_fem
    show bar_fem1 at char_right
    short_speaking "喂，干嘛？"
    hide qianimg
    show qianimg still at char_left
    qian_speaking "……没，我就想看看。"
    qian "突然，我的内心产生一种异样感，仿佛面前人的和善都蒙上一层阴影。虽然有些怵，我还是走到另一边，朝长头发的女生搭话。"
    
    scene bg_bar1 with fade
    qian_speaking "呃……那个？"
    show cg_ying00 at cg0 with dissolve
    window hide
    pause(1.5)
    window show
    unknown "嗯。"
    qian_speaking "你，你还好吗……啊我的意思是你想待在这吗，啊不是……"
    qian "我说出口才想起自己并没有什么理由搭话，于是有些语无伦次。而在我出声后，周围的人瞬间安静，让我更加紧张。"
    unknown "……"
    qian_speaking "啊，抱歉……我打扰了吗……"
    unknown "……"
    unknown "我们先走了。"
    qian "令人不安的沉默后，面前的长发少女终于开口——却不是对我。"
    qian_speaking "诶，怎么……啊诶？"
    qian "她却没多解释，只是用力攥住我的手腕往外走。"
    scene bg_bar1 with fade(0.1,0.1,0.1)
    show crowd with Dissolve(0.5)
    qian "而直到这时，我才注意到周围的人不知道什么时候都围了上来，直直地望着我们。"

    scene bg_road01 with vpunch
    qian "哈啊，哈……差不多了吧。"
    unknown "嗯。"
    qian_speaking "你，他们，你们到底怎么回事啊……嗯，诶……"
    show blur with dissolve
    qian "我被她拉着跑出一段距离才停下来，困惑不已。然而不知是因为太过突然，还是别的什么，我的眼前竟然逐渐变得模糊，摇摇晃晃，身体也快要软下去。"
    qian_speaking "怎么，回事……你……"

    scene bg_black with Fade(0.1,0.1,0.1)
    qian_speaking "嗯……疼……这是哪？"
    scene bg_yingroom0 with vpunch
    show qianimg sad at char_left with easeinbottom
    qian "我猛地从床上坐起来——总觉得这种动作似曾相识……为什么我总是这么倒霉？"
    unknown "醒了？"
    qian_speaking "嗯？"
    show cg_ying10 at cg0 with dissolve
    window hide
    pause(1.5)
    window show
    qian_speaking "是你……！你对我做了什么？为什么要把我带过来？这是哪？"
    unknown "……"
    qian_speaking "我当时担心你的情况……你还这么对我……"
    show cg_ying11 at cg0 with dissolve
    unknown "……\n你不适合这里，回去吧，路上小心点。"
    qian_speaking "哈？你以为是我想来这种地方吗？说得这么轻巧，你以为都和你们D层一样随便吗。帮不了我就算了，找完麻烦还要在这里说风凉话！"
    qian "呜……\n太激动了……连续的意外打击令我烦躁又惊恐，终于在她冷漠的回应后爆发了。"
    
    scene bg_yingroom0 with Fade(0.2,0.4,0.2)
    show yingimg shirt o at char_right with easeinright
    show qianimg at char_left with easeinleft
    unknown "……\n我没做什么，是你被人下药。"
    hide yingimg
    show yingimg shirt at char_right
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "啊……啊？\n所以，你帮了我一把……吗？当时，你拽着我跑出去……"
    qian "她没回话，但大概是这样没错。\n原来不是我帮了她，而是她帮了我……我感到有些赧然，朝陌生人发火，还是因为误会。"
    qian_speaking "对不起……"

    hide yingimg
    show yingimg shirt o at char_right
    unknown "没事。\n药效过了，你不用待在这。"
    qian_speaking "啊，这个，也是……那个，谢谢你……我，我会报答你的。"
    hide yingimg
    show yingimg shirt close at char_right
    unknown "不用。"

    hide qianimg
    show qianimg o at char_left
    hide yingimg
    show yingimg shirt shock at char_right
    qian_speaking "那个，我叫时茜，我们要不要换一下联系方式？等我安顿下来，我会想办法报答你……的？"
    hide yingimg
    show yingimg shirt still at char_right
    qian "我自顾自地快要说完，才发现对面的人有些不对劲——表情似乎有些奇怪，但我也没看出什么来。"
    hide yingimg
    show yingimg shirt stillo at char_right
    unknown "你叫什么？"
    qian_speaking "时茜。"
    hide yingimg
    show yingimg shirt still at char_right
    unknown "……"
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "怎么了吗？"
    hide yingimg
    show yingimg shirt at char_right
    unknown "没事。"
    qian_speaking "嗯，好……还是谢谢你。那我，先走了。"
    hide qianimg
    show qianimg still at char_left
    qian "……"
    qian "……其实我不想走……"
    qian "短时间内经历一系列颠簸后，我的精神实在高度紧绷，惶恐而不安。我迫切地，需要一个支柱……"
    qian "我想要人帮帮我……"
    qian "……"
    hide yingimg
    show yingimg shirt o at char_right
    unknown "等等。"

    scene bg_yingroom0 with Fade(0.2,0.4,0.2) 
    qian_speaking "谢谢你让我留下来休息……我会尽快找到住的地方的。"
    unknown "不用。\n你像一个我认识的人，我并不是……为你。"
    unknown "我叫莺莺。"
    qian "原来如此。我看着莺莺没有表情的侧脸，忽然想起她刚才的微妙表情，也许就是她说的这个原因吧。这算……爱屋及乌？"
    qian "不管怎么样，至少我可以稍微喘口气了……这间房子简陋得过分——黑白灰构成它的全部底色，金属板材拼装成简单的家具——但容纳我和她大概没问题。"
    qian_speaking "那个，我现在还需要做什么吗？"
    ying_speaking "睡觉。"
    qian_speaking "诶？不是刚刚才睡醒……"
    ying_speaking "我要睡。"
    qian_speaking "哦，哦，对不起……谢谢……"
    qian "我后知后觉地意识到，她不仅在我睡着的时候等着我，还把自己的卧室让出来——唯一的床正被我坐着——而自己关上门离开了。"
    qian "所以，她这样对我，也是因为那个“认识的人”吗……我有些羞愧，却又可耻地感到庆幸。"

    ying_speaking "钥匙。"
    ying_speaking "别乱动东西，其他随你。\n我在吃饭的时候回来。"
    qian_speaking "呃，好的，你要——"
    qian "去哪……这两个字还没说出来，她就出门了。\n总觉得……她好像很不待见我，只是把我放在这里。\n不，不应该这么想，我已经很幸运了……"
    qian "那我现在，应该……"
    menu:
        "【什么都不做】":
            $ q1221 = False
            qian "我都已经占用人家的房间了，到处乱走不太合适吧……\n还是等她回来好了……"
        "【观察房间】":
            $ q1221 = True
            qian "虽然莺莺说别乱动，但只是看看不算乱动吧……咳咳……"
            qian "我当然知道自己在强词夺理，可就算感谢她，我总得给自己留点退路：我不会伤害别人，但也最好能够自保……"
            #TODO: 转场
            qian "屋子很小，还没我以前的卧室大，被分成外间和里间，干净得几乎一尘不染，简直无法想象有人类在此长期居住。里间只有一张床，而外间除了桌椅，堆在角落的几个大箱子格外显眼。"
            qian "这是……\n我惊异地看着眼前的那个东西——\n藏在堆叠的箱子的最深处，与黑暗简单的房间格格不入的，闪闪发光的——"
            qian "……莺莺究竟是什么人？"
    
    ying_speaking "……啧。"
    #TODO: 转场
    qian_speaking "啊……！莺莺，你回来了。"
    ying_speaking "……\n动了吗？"
    qian_speaking "啊？"
    ying_speaking "房间里，动过了吗？"
    qian_speaking "……"
    menu:
        "【承认】":
            qian_speaking "没，我只是……看了一下，没动东西。"
            ying_speaking "……你很诚实。"
            qian_speaking "啊，呃，但我确实只是看了看，没做别的……"
            
        "【不承认】":
            qian_speaking "当然没有了……"
            ying_speaking "嗯。"
            qian "她没说信不信，只是深深地看了我一眼。看起来，似乎是没有相信我的话。"
            qian_speaking "那个，我——"

    ying_speaking "……\n是我自己没收好。"
    ying_speaking "不用解释了。"
    qian_speaking "……"
    qian "我感到有些愧疚，再怎么说，也是偷偷翻了别人的东西。但她完全没有要继续对话的意思，我也只好作罢。"

    jump q2_2


    

