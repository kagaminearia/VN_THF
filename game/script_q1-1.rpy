
label q1_1:
    scene bg_office_5 with Fade(0.2,0.4,0.1,color="#fff")
    qian "在荆棘之城，城市管制局处理一切和居民有关的问题。"
    qian "我对管制局的行为感到困惑和愤怒，却不得不承认，也许现在去管制局才是最好的选择。"
    scene bg_office_1 with fade
    show stf at char_right with easeinright
    off_speaking "这是临时的住所和工作信息，时限一周，到期后如工作不通过，管制局不再提供任何帮助。"
    show qianimg at char_left with easeinleft
    qian_speaking "好的……其它问题呢？\n我家里的情况，还有我双亲……"
    qian "我顿了顿，仍然不死心地继续说道。"
    off_speaking "D层身份信息的准备已经完成，如果没有其他需求，请及时结束咨询。"
    
    hide qianing
    show qianimg sad at char_left
    qian "——这难道不是需求吗？我想这样冲她大喊，但无论我说什么，对面的人都油盐不进。"
    qian "我和她一墙之隔，透明的坚硬玻璃阻碍所有来自外部的影响。\n同我的恼怒和激动相比，她的表情毫无波澜——就像我刚刚见到的每个管制局的人那样。"
    qian "……明明，以前在A层的时候，不管什么时候去找管制局的人，她们都会态度友好地回应啊。\n僵持了几十秒，我终于还是受不住，灰溜溜地走出大门。"
    
    scene bg_road01 with fade
    unknown "喂，走路小心点，别撞到人了。"
    qian_speaking "啊……抱歉。\n你们是在这里排队吗？里面没什么人的，在里面等更好。不用在外面……这样吧，看起来不太好呢。"
    qian "来的时候太匆忙，这时我才发现管制局外的广场有不少人，却没有要进去的意思。\n他们只是围在附近，或是靠在墙边，或是坐在地上。横七竖八，什么姿势都有。我没说出口，但实在不太雅观。"
    
    show thin_fem at char_right with easeinright
    thin_speaking "你还是小孩？替家里人来办事的？"
    show qianimg sad at char_left with easeinleft
    qian_speaking "啊？什么意思，不是……"
    thin_speaking "真是不懂事，哎，哪有你这样说话的？跑别人面前嫌弃别人，要是换一个人啊你怕是要吃点教训哦。\n知道D层的管理费多少钱吗？这帮狗东西害得大家都不敢多开灯，就他们这地方最亮，待在这怎么了？"
    thin_speaking "看你这样子也是不懂，等自己赚钱就知道了。他们能有一万种办法从你手里掏钱，不光掏钱还受苦，好好珍惜还不用担心这些事的时候吧。"
    qian_speaking "不是，我没……\n呃，抱歉\n那个我走了再见"
    qian "我实在跟不上她的思路，几乎是逃一般搪塞了对话。等回过神，管理局已经有一定距离。\n它的确是最亮的地方，在整个D层都显得突出而耀眼，像光源吸引昆虫一样聚集大片的人。"
    qian "……"
    
    scene bg_road04 with fade
    qian "这里的建筑又老又旧，又细又长，相互之间挤得很近。不知道是不是我已经产生错觉，我甚至感觉它们不断散发出奇怪的气味。"
    qian "好脏乱……我捏着鼻子走，穿过几条相似的小道，好不容易才看到写着编号的门牌。\n上面的花纹已经掉了一半，只能勉强看出原来的形状。它指着一道狭窄入口，又黑又深。"
    qian "……这真的是人能住的地方吗？我再三确认牌子上的图案，不得不接受现实。"
    scene bg_road05 with Fade(0.1,0.1,0.1)
    qian "更深处没有路灯，我只能靠着终端机上的荧光勉强前进。这片幽幽的光点照亮一小处黑暗，却让人更在意深处没被照亮的东西。\n黏糊，潮湿。"
    scene bg_road06 with Fade(0.1,0,0.1)
    with vpunch
    qian_speaking "好恶心……呃啊！喂……！"
    qian "脚踝被绊倒，腿一软，似乎磕到了很硬的尖角，痛得我甚至站不起来，只好扒着墙一瘸一拐地前进。\n……感觉，我从来没有过这么狼狈的时候。"
    qian "……"
    scene bg_room0 with Fade(0.1,0.4,0.2)
    qian "身前空间不过几米就见底，一块板子横在墙边——如果说那可以被称作是床架的话——被固定住。旁边是矮小的桌子，墙上是一排贴得整齐的小灯，而这就是全部。"
    qian "一切都布满灰尘，带着淡淡的腐烂气息。我难以置信地在门口盯了好一会，才确定这个地方的确就这么大，大约是半个洗手间，曾经的。"
    qian "以前……我赶紧止住思绪，摒弃掉那些会让我动摇的东西，至少现在不应该去想。"
    qian "我讨厌这个地方，讨厌到想要吐。\n但我现在没有任何选择。\n实际上，我已经完全靠着紧绷的精神在继续支撑身体。眼下，也只能在这种地方休息。"
    window hide
    scene cg_qian00 with Fade(0.1,0.4,0.2)
    pause
    scene cg_qian00 at cg0 with Fade(0.1,0.4,0.2)
    pause
    window show
    qian "位置很窄，一道金属栏杆堪堪拦住外侧。\n我蜷缩在角落，腿并排挤在一起，才发现脚已经因为走路而磨破了，滴滴血迹沾湿了床单。"
    scene cg_qian00 at cg1 with Fade(0.1,0,0.1)
    qian "竟然完全没感觉到痛……我有些恍惚地看着流血的皮肤。\n短短一天里发生了太多事情，原来平静的生活这么容易就可以被打破，被搅得天翻地覆。"
    scene cg_qian00 at cg0 with Fade(0.1,0,0.1)
    qian "不知道，无能为力，毫无头绪。\n我明明什么都没做，这种离谱的事情，为什么是我……\n我还，回得去吗……"
    show cg_qian01 at cg0 with dissolve
    qian "我……"
    
    scene bg_factory with Fade(0.1,0.4,0.3)
    show boss at char_right with easeinright
    unknown "第一天上班就迟到，要不是管制局设置的试用期，你现在就可以直接滚蛋了。\n我知道你之前是A层的人，但这里不是A层，别想那些有的没的，没用，好好工作。"
    show qianimg shirt sad at char_left with easeinleft
    qian "面前的人据说是这里的老板，她说话又急又快，我根本来不及跟上节奏。\n见我迟迟没有反应，她的声音拔得更高，像尖刺一般扎进我的头皮。"
    boss_speaking "听懂了没？你是废物吗，回答都不会？"
    qian_speaking "呃啊……嗯。"

    scene bg_factory with Fade(0.2,0.4,0.3)
    qian "刚才竟然被她吓到，还差点发出哭声……我难堪又气闷，连在角落里也不自在。\n手指用力地揉了把脸，我才重新聚集起精神。"
    qian "这是个很大的房间，许多机器整齐排列，每一台前站着一个穿相同制服的员工。她们手上忙着动作，眼神却明显在我身上飘忽。\n看来刚刚动静不小……我攥紧衣角，有些不适。"
    show jun at char_left with easeinleft
    unknown "你还好吗？"
    show qianimg shirt sad at char_right with easeinright
    qian_speaking "啊……你……我……"
    unknown "嘘，别这么大声音。会被骂的。"

    hide qianimg shirt sad
    show qianimg shirt o at char_right
    qian_speaking "呃，嗯……怎么了？"
    unknown "这个地方，你的机器设置错了。\n对了，你还好吗？"

    hide qianimg shirt o
    show qianimg shirt still at char_right
    qian "没事了，谢谢……"
    unknown "你没事就好啦，快工作吧。"
    hide jun

    scene bg_factory1 with fade
    show qianimg shirt still at char_right with easeinright
    qian "半小时的午餐时间。果冻般的压缩食品放在面前，毫无生机，从塑胶袋中被挤进嘴巴。\n浓烈又做作的香精甜味冲上脑门，让我差点直接吐出来。"
    qian "数道视线再次打在我身上——最近，我竟然无比熟悉这种感觉——我不由得掐紧了手指。\n噗嗤，半流质物体溢出塑料袋，糊在桌上。"
    show jun at char_left with easeinleft
    jun_speaking "别这样，食堂还得自己打扫……"
    qian_speaking "哦，嗯……"
    qian "君和坐在我旁边，和工作时的位置一样——我现在已经知道她的名字。\n她扬起手里的袋子，推了推眼镜，冲我露齿一笑。"
    
    hide jun
    show jun_smile at char_left
    jun_speaking "我这边是A2型香气，味道淡一点，要不要跟你换？"
    qian_speaking "不用了……"
    qian "毕竟都一样难吃——我顿了顿，还是没有说出口。\n君和是最近事故以来对我最好的人，至少对她我不想说难听的话。"

    hide qianimg shirt still
    show qianimg shirt o at char_right
    qian_speaking "你在干嘛？"
    qian "休息时间很短，我好不容易抑制住吐的欲望，把那几袋“果冻”塞入腹中。正在收拾东西时，发现君和正在对着便携屏幕缓慢打字。她几乎是一帧一帧移动手指，看着让人着急。"
    jun_speaking "啊……我在写日记。很快的，不会赶不上之后的工作。你要等我一会吗？"
    qian_speaking "可以啊……你真有兴致，在这种地方还有心情写日记。"
    jun_speaking "嗯，那个，算是一点点爱好。\n不过，这里也没什么不好的啊，很干净整洁。"
    qian "这也算吗……她显得有些赧然，我却因为想起一些事情而没有继续回应。\n以前，黄女士也很喜欢在家写日记的……\n不，不能再想了。"
    qian_speaking "那你怎么不用终端？那个打字快一点吧。"

    hide jun_smile
    show jun at char_left
    jun_speaking "诶，那个……"
    qian_speaking "你该不会是忘带了吧？"
    jun_speaking "是，是啊。今天有点忙忘了。"
    qian_speaking "没终端都买不了东西，很不方便的。"
    jun_speaking "没事啦……有人帮我的，谢谢你提醒我。"
    qian_speaking "好吧，那你下次可别忘了。\n……"
    qian "为了逃避胡思乱想，我转移的话题突兀而生硬。但君和似乎没有在意，仍然不紧不慢地继续手上动作，以及笑着回应我的话。\n我莫名感到一丝羞愧，止住了继续询问的话头。"

    hide jun
    show jun_smile at char_left
    jun_speaking "那明天见了，拜拜。"

    hide qianimg shirt o
    show qianimg shirt smile at char_right
    qian_speaking "嗯……好。"
    hide jun_smile
    qian "君和习以为常，我却没有习惯这样的打招呼……仿佛我彻底属于这里一般。\n过去几天，我像度过一个世纪，糟糕的环境令人焦躁，看不到出口。"
    
    hide qianimg shirt smile
    show qianimg shirt still at char_right
    qian "……\n……那之后呢？我应该……"

    menu:
        "【保持专注】":
            jump q1_1_1
        "【彻底放松】":
            jump q1_1_2
    

    return


label q1_1_1:
    qian "不行……就算这地方是这样，我必须认真起来。这不是真的为了工作，只是为了不让我被这个地方完全腐蚀。\n我要保持冷静，保持清醒……"

    scene bg_road02 with fade
    unknown "你有没有想过如何快速赚钱？"
    unknown "最新出的特效药，特别好用！"
    unknown "喂！需不需要借钱啊？这里有很方便的途径哦！"

    show qianimg shirt still at char_mid with dissolve
    qian_speaking "……"
    qian "我逐渐熟练地避开在居民区凑上来打广告的人，讲那些嘈杂的声音撇在脑后。\n……\n脑子里突兀地响起先前那个女人说的话。"

    scene bg_road01 with fade
    show bg_mem
    thin_speaking "他们能有一万种办法从你手里掏钱，不光掏钱还受苦，好好珍惜还不用担心这些事的时候吧。"
    
    scene bg_road02 with fade
    show qianimg shirt still at char_mid
    qian "……\n……只是这样而已。"


    scene bg_ele with Fade(1,1,1,color="#ffffff")
    qian "小窗外的景色直线上升，不断在我的视野里掠过。模糊的深黑色的背景逐渐被稀释，越来越淡，最后变成淡淡的蓝白。"
    qian "很久不见了，甚至有些恍若隔世……这完全不一样的风景。"
    qian "……"

    scene bg_factory with fade
    show bg_mem
    show boss at char_mid with dissolve
    boss_speaking "这儿的负责人呢？不在工作岗位上是都死了吗？"
    unknown "您昨天刚开除……"
    boss_speaking "……\n都是没用的东西，走了就走了吧。\n那边的过来。"

    show qianimg shirt still at char_right with easeinright
    qian "我被指着鼻子，只好停下手中的工作。"
    boss_speaking "你去负责这件事，做不好也一起走人。\n记清楚订单信息，这是A层的事情，一定要尽快把问题解决，不能出差错。"
    qian_speaking "……嗯。"

    scene bg_office_6 with fade
    show bg_mem
    stf_speaking "姓名编号，五官指纹。\n申请原因？逗留时间？机构编号？\n通行证绑定终端，不能替换。"
    qian "回答一系列问题后，我被全身上下检查一遍，终于能够进入前往A层的通道。\n——于是，我再次看到这番场景，并不是因为幸运而“重逢”。"
    
    scene bg_ele with fade
    qian "但的确久违了，广阔的天顶，轻巧的空气，以及如画一般明亮活力的颜色。\n荆棘之城的A层。"
    show qianimg shirt still at char_mid with dissolve
    qian "……"

    scene bg_city0 with Fade(0.5,0.5,0,color="#747474")
    qian "A层禁止居民以外的人使用个人大型机器，我从公共交通上下来，跟着电子光屏上的路线往前走，平坦而坚实的道路让我一时有些难以习惯。"
    qian "和D层不同，这一路上几乎没有遇到任何人，人口密度低得像我空空荡荡的胃部。\n但事实并非如此，A层人虽少，但在寸土寸金的荆棘之城远远不可能是这种程度。"
    qian "大概是因为信号标记。\n我曾经的终端机上——有A层特殊标识的终端机上——会显示进入A层的外来人的位置。而居民十分自然地，充满默契地远离那些人。"
    
    show qianimg shirt still at char_mid with dissolve
    qian "也就是现在的我。"
    qian "微疼的触感让我回过神，是手指不自觉地用力按在终端的背面，刻着城市印章的地方。\n坚韧，勇敢，一直以来，那是这座城市带给我们的信念，如它的历史一般熠熠生辉。"
    qian "但与此同时，我第一次意识到，它也为每个人种下标签，就像城市印章一样，根深蒂固，如影随形。"
    
    scene bg_cafe0 with fade
    unknown "你好，现在不是营业时间~咦？\n嗯……你好？"
    qian_speaking "……你好。"
    
    
    show cg_chi00 at cg0 with dissolve
    window hide
    pause(1)
    window show
    qian "纯黑色、精心整理的头发垂在额角和颈后，身上柔软细腻的布料分为一层层，点缀有精致蝴蝶结，并不是现在的流行，却无比精致。"
    show cg_chi01 at cg0 
    qian "一双水蓝色的明亮眼睛看着我，乍一眼让我看得失了神，直到对方再次出声。"

    scene bg_cafe0 with fade
    show qianimg shirt o at char_left with easeinleft
    show chiimg at char_right with easeinright
    qian_speaking "抱歉，关于您提交的订单，这边有……"
    qian "我把核对的信息报出来，并提出相应的解释。\n对方似乎还没理解，只是十分专注地看着我，好像这就是此刻世界上最重要的事情。"
    unknown "噢，原来是这个问题。你好厉害啊，这么快就知道了，谢谢你！"
    qian "面上没有显示，我的心里却不自觉飘飘然起来——而后，下一秒就重新下坠。"
    
    hide qianimg shirt o
    show qianimg shirt close at char_left
    qian_speaking "呃……！"
    
    hide chiimg
    show chiimg sadask at char_right
    unknown "怎么了？！你没事吧？"
    qian "动作不熟练，手上的力气一个不稳，锋利坚硬的零件划伤我的手掌，很快渗出鲜红的血液。"
    
    hide qianimg shirt close
    show qianimg shirt still at char_left
    qian_speaking "没……不小心扎到了而已。"

    hide chiimg sadask
    show chiimg at char_right
    unknown "啊，你都闭眼睛了，一定是很疼吧？对不起，你别担心……我会帮你的！"
    qian_speaking "不，没事……"
    qian "我有些慌张地挥手，声音却很弱——说来好笑，宋女士和黄女士都是生物方面的专业研究人员，家里到处都是相关资料，偶尔还会做点小实验，但我竟然很怕血。"
    qian "不过，怎么能麻烦其他人……正当我这么想的时候，这位A层的少女很快去而复返。\n她在后侧方微倾身体，轻飘的发丝垂下，在我的后颈上震颤，手腕被人抓起来，有什么柔软的东西贴上我的皮肤。"
    
    show cg_hand00 at cg0 with dissolve
    window hide
    pause(0.6)
    show cg_hand01 at cg0 with dissolve
    pause(0.6)
    show cg_hand02 at cg0 with dissolve
    pause(0.6)

    window show
    qian "而后，那个小小的、失控的缝隙被抚平了。"

    scene bg_cafe0 with fade
    show chiimg closesmile at char_right with dissolve 
    unknown "好了，现在应该没事啦！"
    show qianimg shirt o at char_left with dissolve
    qian_speaking "……"

    hide chiimg closesmile
    show chiimg at char_right
    unknown "怎么了？你还是很难受吗……？是，是我做得很差吗？"
    qian_speaking "……\n不是！呃，那个，谢谢你。\n麻烦你了……我真的没事了。"

    unknown "那就好！对了，你觉得我处理得怎么样，会不会有点不舒服？啊，手法是不是比较粗糙？"
    qian_speaking "……啊？没有，真的很好。"
    
    hide chiimg 
    show chiimg laugh at char_right
    unknown "真的？太好了！谢谢你，我在家练习过很多，但还没试过对真人包扎呢，真可惜不能说你是我的第一个患者。"
    
    hide qianimg shirt o
    show qianimg shirt smile at char_left
    qian_speaking "是我谢谢你……什么患者？"

    hide chiimg laugh
    show chiimg warm at char_right
    unknown "我不能做医生呀。\n虽然很可惜，不过这次能够帮到你，我已经很开心啦。"
    
    hide qianimg shirt smile
    show qianimg shirt o at char_left
    qian_speaking "啊……"
    unknown "直到现在，她语气稍稍低沉下来时，我才意识到先前一直被她调动着情绪，以至于我忘了本来要说的话。"
    
    hide qianimg shirt o
    show qianimg shirt still at char_left
    qian_speaking "谢谢你，抱歉，这是我的失误，不好意思还麻烦到你了。那个……订单问题已经解决，以后如果还有问题可以随时联系公司。"
    qian "我很快让自己的情绪平静下来，止住了即将脱缰的话题讨论。\n我小心地避开她收回手臂，掌心用力，伤口反射出疼痛，让我口齿间发出的声音变得清晰。"
    
    hide chiimg warm
    show chiimg at char_right
    unknown "对不起哦，是我让你受伤了。\n那你就要走了吗？要不要喝一杯什么再走？"
    qian "不知道是不是错觉，她的表情浮上失落……大概是错觉。因为她很快就又笑起来，朝着我挥了挥手。"
    qian "我再次摇头，抬起手在终端机的屏幕上点了几下。\n投影屏打开，上面清晰地显示着我的“通行许可”。而此刻，我的剩余停留时间几乎见底。"
    unknown "咦，原来是这样……那你要是下次再来A层，来找我聊天吧！你能看到我的通讯信息吗，我先发给你……对了，我叫迟玉！"
    qian_speaking "好。"
    qian "迟玉的情绪如此生动，显得我更加局促。\n她的情绪太过生动，以至于我差点以为那不是善意的礼貌，而是真实的热情；以至于我差点以为我还是A层的居民，而不是“那些人”中的一员。"
    
    
    show cg_chi10 at cg0 with dissolve
    window hide
    pause(0.3)

    window show
    chi_speaking "拜拜~"
    qian_speaking "……\n……"


    scene bg_factory1 with Fade(1,1,0.3)
    na "……"
    qian "君和消失了。"
    qian "在一成不变的日程里，这件事显得尤其突兀。\n说消失不太准确，只是她突然停止了工作，没有通知，而我也再没有收到她的任何消息。"
    show qianimg shirt still at char_mid
    qian "这事的确没有特地通知我的必要，但我总觉得似乎有些奇怪……"

    menu:
        "【尝试问其他人】":
            qian "尽管我认识君和不久，但她最初的和善对我意义很大……无论她如何看待我，我还是希望能够了解到她的情况……"
            qian "我对自己的人际关系有数，大部分人看到我就退避三舍，但只是问问应该没事……"
            qian "然而尝试询问后，除了被拒绝，我只得到“好像去A区工作了”这样似是而非的结论，似乎没人知道具体是什么。"
            qian "……\n可能只是我想太多吧，其实并没有什么特别的。"
        "【算了】":
            qian "算了……对方既然没有说，大概是不想让我知道吧，毕竟我之前给她的印象也许不算好。\n我叹了口气，不知为何有些沮丧，希望尽快把这件事抛至脑后。"
    
    qian "……"
    qian "……\n不过，无论我在意与否，似乎都没有什么区别。现在的我如此无能，只是被困在这个混乱而陌生的地方罢了。"
    scene bg_black with fade
    qian "人的适应性——或者说求生欲——真是极强，我无比真切地体会到这一点。\n刚到D层的时候，我以为我根本没法在这种地方活下去，但现在看来也不过如此。"
    qian "简陋狭窄的房间只有摇曳的暗光，我出神地抬起头，正好看到挂在门口的衣服。\n沾过各种脏污，睡衣进行过粗暴的清洗后仍然坚挺着浅层的柔软绒毛。\n我唯一从过去留下来的东西。"
    
    show cg_cloth at cg0 with fade
    window hide
    pause(1)
    window show
    qian "垂得齐整的布料像风干的实体，埋葬不为人知的事。\n每每看到它，我的心脏都会停跳一拍，而现在，好像连这样的感觉都要趋于麻木了。"
    qian "荆棘之城……我似乎头一回认识这座城市。\n并不是那样完美，明朗，温暖。"

    jump q2_1

image cg_qian1:
    "images/cg/cg_qian10.jpg"
    0.1
    "images/cg/cg_qian11.jpg"
    0.1
    repeat


label q1_1_2:
    qian "总之……我并没有认真的打算，我又不是真来这种地方工作的。\n随便应付一下，只要撑到家里有消息的时候就行了。"
    qian "随便混混日子并不难，不过是相似的流程，每一天都一样。"

    scene bg_black with fade
    qian "……\n但事情却没有符合我的期待。\n没有……没有，什么都没有。"
    qian "我没有等来管理局的通知，也没有任何回到原本生活的办法，甚至，连之前有过的，宋女士她们的消息，也再没有收到过了。"
    qian_speaking "……"
    window hide
    show cg_qian1 at cg0 with fade
    pause
    window show
    qian "我蹲坐在房间的角落，手指重复着“打开终端，划过消息，关闭终端”的动作。"
    qian "所谓的工作没有技术含量，只有繁重和忙碌，塞满我的生活。除了死白色的宽敞工厂，我没有兴致也没有时间再拥有其他。"
    qian "不知道从什么时候开始，我的思维似乎也已经变慢、停滞，完全融入D层的死水。"
    qian "……她们怎么样了？我没有多余的精力去思考，但还有什么比在这里要更差的？\n嗯，只要如果过得比我好就够了……"
    qian "我再次下意识地活动手指：打开终端，划过寥寥无几的每条消息，关闭终端，打开终端，划过……"
    qian "房间里冒出微弱荧光，不断闪烁，忽明忽暗，重复往返。"

    # 【Ending：死寂】
    $ persistent.text = 1
    $ persistent.ending[0] = 1
    return
