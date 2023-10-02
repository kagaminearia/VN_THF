label q1_3:
    scene bg_road05 with Fade(0.3,0.2,0.4)
    qian "沿路牌往前，道路逐渐出现不同的分岔，而后，最近的路口挂着巨大的显示屏：D-230，居民区。"
    qian "不太信任管制局，可其他地方又好到哪里去。\n昏暗的环境仿佛滋生鬼魅，时不时的窸窣声从角落传来，让我心生退意，胸口也憋闷得要窒息。"
    qian "好，难受……不安和疲惫越发堆积，直到眼皮越来越重，腿也抬不起来，不得不停靠在布满灰尘的墙角。\n为什么，会这样……"

    scene bg_black with Fade(0.4,0,0.4)
    unknown "怎么又到清理垃圾的时候了啊，真麻烦。"
    unknown "就是啊，那些垃圾不能自行滚出去吗，浪费我们城市宝贵的资源啊。"
    unknown "啊你这人真够恶劣的，想什么呢，哈哈哈哈……"
    scene bg_chaos0 with vpunch
    qian "……好像，有什么……声音……好吵……\n可是，动不了，连眼睛都睁不开……"
    unknown "喂，这还有一个！拿袋子来！"
    scene bg_chaos1 with hpunch
    qian "等等，有人碰我……啊！放开……！呃……"
    unknown "这家伙还在动，你过来搭把手！"
    unknown "好好，别叫了来了——"

    scene bg_black with hpunch
    qian "臭，好臭……\n……啊……！"
    scene bg_pit0 with hpunch
    show liquid0 with dissolve
    qian "我猛地睁开眼睛，有什么液体从睫毛上落下来，黏腻、湿热、恶臭，让我差点再度晕过去。\n这是哪……"
    qian "像是陷入沼泽，泥泞脏污，只是其中的“淤泥”是更加复杂的东西：黑灰色的大塑胶袋，扯烂的金属和电线，辨认不出形状的固态物。杂乱无章地堆叠积压在一起，渗出腐烂的气息。"
    qian "我的眼皮开始疯狂打架，身体也不受控制地颤抖起来。"
    qian "怎么，这里到底是……啊……！"
    scene bg_pit1 with hpunch
    na "轰隆——"
    qian "巨大的声响打断了我的思考。\n而后，头顶的黑色天花板快速降落，随着砰的一声，剥夺了我视野里的一切光线。"
    qian "“地面”开始剧烈晃动，周围的垃圾一股脑地摔下来，将我挤得喘不过气，而后又因摇晃在我身上碾压。"
    scene bg_black with my_shake
    horr "痛，好痛……\n好痛好痛好痛好痛……"
    # scene bg_black with hpunch
    horr "每一块可能的皮肤和肌肉都在拉伸，向不同方向撕扯，每一寸神经都在啸叫，发出震耳欲聋的冲击声。"
    # scene bg_black with hpunch
    horr "我控制不了身体，睁不开眼，找不到合适的姿势，无论怎么做都痛得流泪，像整个人被扔进高速旋转的洗衣机，撞得头破血流。"
    # scene bg_black with hpunch
    horr "直到时间都失去意义，疼痛和耳边的轰鸣都没有停止，我的精神像在荆棘刺中打滚，变成千疮百孔的破烂。"
    scene bg_black with hpunch
    qian "疼，疼痛……"

    scene bg_black with Fade(1,0,1)
    unknown "你也来捡垃圾啊？"
    unknown "是啊，万一有点什么，也是点收入……我去，这里好像有个活人？！"
    qian "好像有什么声音靠近，耳鸣使得它模模糊糊，但我还是用尽全力驱动上半身的肌肉，向有声音的地方挪动。"
    
    qian_speaking "救，呕……救我……"
    show liquid0 with dissolve
    qian "刚一开口，腹部就一阵痉挛，而后只有混合的胆汁和粘液从嘴角溢出，发出和周围一样的酸臭味。"

    scene bg_black with Fade(1,0,1)
    qian_speaking "救，救我……啊……！\n……嗯？……"
    qian "我的身体条件反射地剧烈打颤，但并没有迎来熟悉的撕裂感，只剩淡淡的疼痛，在身体里轻柔地融化。"
    qian "啊……"
    scene bg_liroom0 with Fade(1,0.5,1,color="#fff")
    qian "我这才敢睁开眼睛。四周并不是臭气熏天的垃圾堆，只是一个无人的房间。\n这算……得救了吗？"
    qian "我悬着心仔细观察房间：一眼望去，地面和墙壁光秃秃的，室内没有窗户，一扇小门关得严实，低矮的天花板挂着两点摇晃的火光——少见的明火。至于其他……"
    na "吱呀——"
    qian "……谁？"
    window hide
    show cg_li00 at cg0 with dissolve
    pause(1.5)
    window show
    unknown "醒了？"
    qian_speaking "啊，呃，嗯……"
    unknown "……"
    qian "……\n不认识的女人站在面前，身着长到脚踝的黑色披风。她一动不动，只是默默地看着，视线仿佛要看穿我。"
    qian_speaking "……这是哪里？你是谁？是，是你救了我吗？"
    qian "终于，我忍受不了这样的气氛和沉默，努力让自己的喉咙发出声音。刚开始有些困难，但说到后面，却几乎有些逼问的急迫。"
    scene bg_liroom0 with Fade(0.4,0.5,0.3)
    show liimg at char_right with easeinright
    unknown "你对救你的人是这个态度吗。"
    show qianimg sad at char_left with easeinleft
    qian_speaking "啊，呃，对不起，所以，真的是你救了我……但是，到底发生了什么……那个，你需要我做什么吗？"
    hide qianimg
    show qianimg at char_left 
    qian "事到如今，发生那么多事情之后……我总不会还在天真地相信她只是因为善良才救我。"
    unknown "是想，可是你看起来没什么用。"
    hide qianimg
    show qianimg still at char_left 
    qian_speaking "什……！"
    hide liimg
    show liimg o at char_right
    unknown "说说你吧。你叫什么，怎么会出现在那里的？"
    qian "为什么反倒先问我……\n说到先前的事情，我下意识绷紧了身体，那刺骨的疼痛仍然让我心有余悸。"

    menu:
        "【说实话】":
            jump q1_3_1
        "【蒙骗过去】":
            jump q1_3_2


label q1_3_1:
    scene bg_liroom0 with fade
    qian "现在的情况我是完全的劣势，哪怕一时说谎也不会有太大改变，万一被看穿可能更加危险……"
    qian "能救下我的人，说不定很厉害，还是全部告诉她吧……"
    show qianimg still at char_left with dissolve
    qian_speaking "我叫时茜，从A层来到D层，因为……"
    scene bg_liroom0 with fade
    show qianimg o at char_left  
    qian_speaking "之后……就是这样。对了，可以看终……我的终端呢？"
    show liimg o at char_right with dissolve
    unknown "你是说这个吗？"
    hide qianimg
    show qianimg shout at char_left  
    qian_speaking "怎么在你那里！"
    hide liimg
    show liimg smile at char_right
    unknown "不清楚底细的人，当然要好好检查一遍啊，不然怎么知道要不要救你？"
    hide qianimg
    show qianimg at char_left 
    qian_speaking "你……那你看都看过了，为什么还要问我……"
    hide liimg
    show liimg laugh at char_right
    unknown "看你会不会说出点新东西啊，总要多点信息来源吧。"
    hide qianimg
    show qianimg still at char_left 
    qian "是为了看我有没有说谎吧……真够狡猾。但，至少这说明我实话实说是正确的……也许。"
    qian_speaking "我知道的就这些了……"
    unknown "这样啊，你也不容易嘛。"
    qian_speaking "是，是啊……"
    unknown "他们做这么恶劣的事情，就没想过偷偷回去？"
    hide qianimg
    show qianimg at char_left 
    qian_speaking "怎么可能啊，管制局的人难道是白拿钱的吗。"
    hide liimg
    show liimg smile at char_right
    unknown "你都没试过，就觉得不可能了？"
    hide qianimg
    show qianimg shock at char_left 
    qian_speaking "哪有你说的那么容易！"
    hide qianimg
    show qianimg still at char_left 
    qian "……\n我大吼出声后才惊觉自己的失态，急急地扼住胸口将要迸发的郁气。"
    unknown "……"
    scene bg_liroom0 with fade
    show liimg ask at char_right with dissolve
    unknown "所以，管……那些人真的很厉害，完全没有漏洞？你们那个所谓的系统真的很可靠吗，到处都是？从人下手呢，没有偷懒的人吗？"
    show qianimg sad at char_right with dissolve
    qian_speaking "不，不知道……其实我没有在D层待过很久，但也有听说好像现在管理很混乱……但是，但是要回A层绝对不可能的，上层的管理很严格的。"
    hide liimg
    show liimg o at char_right
    unknown "这样啊，你怎么一副要死不活的样子？"
    qian_speaking "有吗……"
    hide liimg
    show liimg close at char_right
    unknown "算了，你再休息会，待会把你知道的所有关于D层的消息都跟我讲讲。"
    qian_speaking "哦，好……"

    scene cg_soup at cg0 with fade
    qian_speaking "这是什么……？"
    unknown "吃的，怕你说得太累把自己累死了，补充点体力。"
    qian_speaking "……哦……"
    unknown "不吃拉倒，别浪费粮食。"
    qian "总感觉吃了之后才会死……我硬生生憋住了这句话。\n不过，这发出奇怪气味的东西真的能吃吗……我一狠心，屏住呼吸将碗里的东西倒进喉咙。"
    show blur with vpunch
    qian_speaking "呕……咳，咳咳……"
    unknown "行了，不爱吃别吃。"
    qian_speaking "咳，呃，好……谢谢……"

    scene bg_liroom0 with fade
    show liimg o at char_right with dissolve
    unknown "继续说吧，你知道的事。"
    show qianimg o at char_left with dissolve
    qian_speaking "……你到底是做什么的？"
    hide liimg
    show liimg ask at char_right 
    unknown "这重要吗？对你来说，我是救了你的命的人，你只需要知道这个就够了。"
    hide qianimg
    show qianimg at char_left
    qian_speaking "……\n你不是D层人吧。你都已经知道我是刚来D层没多久的，却还是追着我问各种基础问题。"
    hide liimg
    show liimg at char_right 
    unknown "……"
    qian_speaking "说到D层的时候你总会有奇怪的卡顿，虽然这在自然对话中很常见，却很不像你的说话方式。"
    qian_speaking "但你又尤其在意和上层之间的通道，而且仅仅是A层，为什么？如果你不是D层人，为什么需要这么费尽心思？"
    hide qianimg
    show qianimg still at char_left
    qian_speaking "难道你……"
    hide qianimg
    show qianimg shock at char_left
    qian "！"
    hide qianimg
    hide liimg
    window hide
    show cg_li10 at cg0 with dissolve
    pause(1.5)
    window show
    qian "和我一样？\n这句话我没能说出来，因为面前的人突然毫无预兆地凑近，带起的疾风和危险感让我浑身发毛。"
    qian_speaking "……"
    show cg_li11 at cg0 with dissolve
    unknown "感觉你知道的有点多，是不是该把你杀了？"
    qian_speaking "喂……！"
    unknown "嗯……"
    show cg_li11 at cg0 with dissolve
    unknown "行了，开玩笑的。"
    scene bg_liroom0 with fade
    show liimg smile at char_right with dissolve
    show qianimg still at char_left with dissolve
    qian_speaking "……你到底什么意思？"
    unknown "夸你聪明啊，对了，那就认识一下吧，我叫黎沙。"
    qian "我不聪明就不跟我说了吗……好恶劣的人。"
    hide liimg
    show liimg laugh at char_right
    li_speaking "至于我是哪里人……嗯，这个可能有点难回答。"
    hide qianimg
    show qianimg at char_left with dissolve
    qian_speaking "直接说不就完了？"
    li_speaking "我说了，你信吗？"
    menu:
        "【信】":
            qian_speaking "会……我相信你。"
            qian "我十分确认地给出我的答复。我觉得……她是可信的，毕竟她看上去也没有很坏，似乎……没有什么理由骗我吧？"
            li_speaking "……好吧。"
            qian "见我似乎没有其他反应，黎沙顿了顿，似乎有点惊讶，但随后又叹了口气，恢复原来的笑容。"
        "【不信】":
            qian_speaking "……谁知道呢……我现在也没办法下结论啊。"
            qian "我的手指用力到有些发白。这样对她说话，实在显得有些不识抬举，可也确实是因为我真心想相信她，而不只是随口说说。"
            qian "然而黎沙完全没有要生气的样子，只是有些揶揄地笑了笑。"
            li_speaking "嗯，挺好。"
            qian_speaking "喂……"

    hide liimg
    show liimg smile at char_mid
    li_speaking "我还是直接带你去看吧，带你看一下我是哪里人。"
    qian "……什么意思？\n我无法理解，在巨大的困惑中被她手臂抓着向外走。"
    hide qianimg with easeoutleft
    hide liimg with easeoutleft
    
    scene bg_black with fade
    qian_speaking "咳咳！"
    qian "一股有些呛人的味道弥漫鼻尖，我忍不住剧烈咳嗽起来。好一会后，我才睁开眼睛，看见打开的门后向外的地方，黎沙所说的场景。"
    
    scene bg_sand3 with fade
    qian "视野里是粗糙的暗黄色，像有一层浓烟盖在画面上，看不真切。"
    qian "远处有淡淡微光，但整体基调仍然阴沉。近处的地面并不平坦，三三两两的房屋散落在各处，隆起的小丘上有轻卷起的浅层尘土。大大小小的裂缝漫布，凹凸不平。"
    qian "沙，还是沙。\n满目皆是一片黄沙。\n这样的景象，我只在书中见过对应的描述。"
    show qianimg shock at char_left with dissolve
    qian_speaking "这是……"
    qian "我的牙齿不受控制地用力，把空气咬碎。\n无法理解，无法想象，也不敢深入思考。"
    qian "荆棘之城里没有这样的地方，没有这样的天气，所有的东西都是静止的，平和的，不变的。\n但，那，现在这是……"
    show liimg ask at char_right with dissolve
    li_speaking "吓到了？"
    qian_speaking "不，不是……但，这是哪……"
    hide liimg
    show liimg at char_right
    li_speaking "城外啊。"
    qian_speaking "……啊？"
    scene bg_sand3 with fade
    qian "她轻松吐出的几个字如同惊雷炸在我的头顶，一时间连视线都有些恍惚。\n是我想的那个“城外”吗？"
    show liimg o at char_right with dissolve
    li_speaking "是啊，就是被你们城市遗弃的地方。"
    show qianimg shout at char_left with dissolve
    qian_speaking "什，什么……这到底是什么意思？"
    hide liimg
    show liimg laugh at char_right
    li_speaking "就是你想的那个城外啊，你们城里人不是总说想见识的吗。"
    hide qianimg
    show qianimg shock at char_left
    qian_speaking "但，但是……城外不是这样的……城外怎么会是这样……"
    qian "从开门后，我的大脑就有些混乱，面对突如其来的庞大信息，简直快要过载了。这和我一直以来对“城外”的认知完全不一样，完全，不一样啊……"
    hide liimg
    show liimg smile at char_right
    li_speaking "是不是觉得很奇怪？"
    qian_speaking "啊，啊啊……"
    li_speaking "城外怎么不是美好的地方？城外的人怎么没有害死你们，把你们逼在荆棘之城那个保护罩里？"
    hide liimg
    show liimg laugh at char_right
    li_speaking "你们可怜，你们悲惨。你们被剥夺，你们受尽苦难，只能在笼子里度过一生……是这样吗？"
    qian_speaking "……难道不是吗……"
    qian "事到如今，我的话毫无说服力，连我自己也感到迷茫。可是……我一直以来学到的知识，都是这么告诉我的。"
    scene bg_black with fade
    qian "因为曾经的战争，战败的一方被迫圈地，不知道真实世界的模样，不知道真正的日夜与四季。\n应该，就是这样的……眼前的景象，却完全超出我的认知。"
    qian_speaking "……我……咳，咳咳咳……"
    qian "喉咙烧得灼痛，我止不住地咳嗽，被黎沙拽着往里走。她重新关上门之后，才感觉呼吸道没那么难受了。"
    scene bg_liroom0 with fade
    show liimg o at char_right with easeinright
    li_speaking "好点了没，再喝点水？"
    show qianimg sad at char_left with dissolve
    qian_speaking "不用了，咳……谢谢你……"
    hide liimg
    show liimg at char_right
    li_speaking "嗯。"
    qian_speaking "……\n那个……"
    li_speaking "怎么了？"
    hide qianimg
    show qianimg still at char_left
    qian "我有点受不了这仿佛要下葬的尴尬气氛，可我也有急切想要知道的事，因而也只好硬着头皮开口了……"
    qian_speaking "所以……到底发生了什么事？我是怎么到城外的，还有城外……"
    hide liimg
    show liimg close at char_right
    li_speaking "啧……真麻烦。"
    hide liimg
    show liimg at char_right
    li_speaking "那时的战争，你们城里人才是打赢的一方，不，应该说，是打赢的那些人自己建了城，把其他人挡在外边。然后，一直都是这样啰。"
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "……啊？怎么……为什么啊？……非得这样吗？……"
    li_speaking "资源啊资源……你看这外面的环境是什么样，以前就因为这样才有战争的，现在外面更严重了。\n"
    li_speaking "哎，那帮人自己圈了块地，在里面过得爽快，最后还非说自己是受害者，这真是比不了。"
    hide qianimg
    show qianimg still at char_left
    qian_speaking "……"
    hide liimg
    show liimg ask at char_right
    li_speaking "对了，你说被扔到什么垃圾堆，那估计是真的。这里也有几个垃圾坑，城里人把所有生产垃圾和脏东西扔下来……全让城外解决。"
    horr "呼——呼——"
    li_speaking "这么说来，你能在死人堆里活下来，还真是……"
    horr "呼——呼——呼——"
    hide liimg
    show liimg still at char_right
    li_speaking "等等——我看一下。"
    qian_speaking "……啊。"
    qian "我有些呆愣，好一会才反应过来她在跟我说话，以及，逐渐靠近的，轰鸣般的呼啸声。"
    li_speaking "先不说了快过来。"
    qian_speaking "……啊？啊，诶——\n啊啊——！"
    hide liimg with easeoutright
    hide qianimg with easeoutright
    window hide
    show bg_white with Dissolve(0.1) 
    pause(0.1)
    show bg_storm with Dissolve(0.1)
    pause(0.5)

    scene bg_black with Fade(0.5,0.5,0.5,color="#fff")
    show qianimg still at char_left with dissolve
    qian "好吵……"
    show liimg still at char_right with dissolve
    li_speaking "最近天气变化越来越快了，真够烦的……不知道这次又要死多少人。"
    qian "出口关闭得严严实实，但还是能听见那仿佛要把地上一切卷走的呼啸声音。以及碰撞声，挤压声，还有夹杂在风中的呼喊声。"
    hide liimg
    show liimg o at char_right 
    li_speaking "哦，你不知道这是什么是吧。以后听到这个声音记得跑，不要待在地面上，沙暴很危险。"
    qian_speaking "以后……"
    show blur with hpunch
    li_speaking "你说什么？我听不清——喂，你这是哭了吗？没事吧？是不是污染物进眼睛了？"
    qian_speaking "没，没有……"
    qian "……我哭了吗？我不知道。\n但她看过来时，我条件反射地偏移视线，低下头，而后，面前的地上出现了一滴滴水渍。"
    qian "……我怎么哭了？我不知道。只是，一种莫名的感情堵在喉口，硌得我难受不已。\n意识到这点后，愈发难以控制。\n不要……我不想，这样……"
    qian_speaking "没，对……不起……呜……嗯……"
    li_speaking "……\n唉。"
    qian_speaking "？！"
    li_speaking "你哭什么啊……真受不了，我还没来得及哭吧。"
    qian_speaking "……对不，起……"
    li_speaking "唉……算了，爱哭哭，这里也没有别的事做。"
    qian_speaking "……"
    qian "好在，她现在看不到我的表情。\n声音止不住，我自暴自弃地不再控制。"
    qian_speaking "呜，呜啊……呜呜……"
    qian "过多的信息让我的认知完全崩塌，颠覆的故事，对现状的不忿不安，对城外的恐惧夹着愧疚，头顶的风暴声与无数矛盾的思绪挟住我，令我无法呼吸。"
    hide blur with dissolve
    qian_speaking "……呜……"

    scene bg_black with fade
    li_speaking "醒醒，醒醒！"
    scene bg_black with fade
    show qianimg shock at char_left with easeinbottom
    qian_speaking "啊……啊？！"
    show liimg o at char_right with easeinright
    li_speaking "我说你啊，自己哭到睡着就算了，能不能别妨碍别人啊。"
    hide qianimg
    show qianimg sad at char_left
    qian_speaking "什么……啊，那个！对，对不起！\n——哇啊！"
    qian "我急忙和黎沙拉开距离，而后——头顶撞到了天花板。\n好矮啊……哦，对，这里是地下室……"
    hide liimg
    show liimg close at char_right 
    li_speaking "……\n走吧，出去了。"
    qian_speaking "嗯，嗯……"
    qian "总觉得她似乎欲言又止……唉，我都做了些什么事啊……"
    scene bg_sand0 with fade
    qian_speaking "……\n……"
    qian "这就是，沙暴吗……"
    show liimg o at char_right with easeinright
    li_speaking "你站着干嘛呢？把披风穿好，过来搭把手。"
    show qianimg o at char_left with easeinleft
    qian_speaking "好的……！"
    scene bg_sand0 with fade
    qian "阴冷的风带着尘土吹过脸颊，引发淡淡的刺痛。我接过黎沙从地下搬出来的工具箱，把它们搬到墙根旁边。"
    qian "……对，是墙根，因为四周的墙壁都已经不成形状，只剩挤压的材料和巨大的空洞。放眼望去，四处皆是倒塌的东西，包括人。"
    show qianimg sad at char_left with dissolve
    show liimg at char_right with dissolve
    show sand0 with dissolve
    qian_speaking "那些人……不去帮忙吗？"
    li_speaking "怎么帮？你去帮吗？"
    qian_speaking "呃，我……"
    li_speaking "哪里帮得过来。\n还不如先帮帮我自己。"
    qian_speaking "……"
    qian "怎么会这样……\n我呆站在原地，只有风声在胸口回荡。"
    hide liimg with dissolve

    scene bg_liroom0 with fade
    show dark with dissolve
    li_speaking "还没睡？你不累吗。"
    qian_speaking "呃，累……但是睡不着。"
    li_speaking "不舒服还是吓到了？不管怎么样，你还是快习惯了吧，这儿可没你们那过得舒坦。"
    qian_speaking "……我知道。"
    qian "我吐出一口气，望向低矮的天花板——多亏科技发展，建一个简单的平板房子不需要多久。"
    qian "然而我又很快想到，说不定也正因为科技，我才会沦落于此吧……\n我有些不自然地挪动身子，效果甚微。床不大，只能和黎沙挤在一起。"
    window hide
    show cg_li20 at cg0 with dissolve
    pause(1.5)
    window show
    qian_speaking "你们……一直都是这样吗？"
    li_speaking "哪样？"
    qian_speaking "就是，像这样的事情，天气……"
    li_speaking "嗯，差不多吧。不过近期越来越频繁了。\n我小的时候……大概是每年都有两三次，现在有时候两个月就得来一下子。"
    li_speaking "照这么一边污染一边开发，谁知道之后会怎样……哎，一想到就真是受不了你们。"
    qian_speaking "对不起……"
    li_speaking "你有什么可对不起的。"
    qian_speaking "……不知道……\n……\n我怨恨死了，为什么我非要遇到这种事……可是没想到会遇到你，你们这样的……我觉得，很不舒服……"
    qian_speaking "但是，但是我明明没有做错任何事……"
    li_speaking "……\n所以说啊，你说什么对不起。"
    qian_speaking "……我只是想不通。"
    li_speaking "想不通就算了。你也不过是个被欺骗的蠢货罢了。"
    qian_speaking "……\n好吧。\n你这算在安慰人吗？"
    li_speaking "你觉得像吗？"
    qian_speaking "不太像。"
    li_speaking "……你还真回答……我服了。\n像不像都无所谓啦，睡吧。"
    qian_speaking "嗯。"
    qian "我的情绪竟然惊人地平静下来。\n虽然还有太多我搞不明白的事……就算知道是在逃避……但现在，还是先睡觉吧。"
    jump q2_3


label q1_3_2: #ending here
    scene bg_liroom0 with fade
    qian "现在的情况对我来说太过危险，如果全部如实告诉她，说不定会更危险……"
    qian "虽然这么想，短时间内我也想不出什么好的说辞，只好含糊其辞，快速带过。"
    show qianimg still at char_left with dissolve
    qian_speaking "就是这样……我只是到D层后迷路了，后来不知道发生了什么。"
    show liimg o at char_right with dissolve
    unknown "只是这样？你确定吗？"
    qian_speaking "是，是啊……"
    unknown "……"
    qian "她紧紧盯着我，似乎已经看穿我的想法。\n但我还是屏住呼吸，坚持我那摇摇欲坠的谎言。"
    hide liimg
    show liimg close at char_right
    unknown "……知道了。"
    hide qianimg
    show qianimg o at char_left 
    hide liimg with easeoutright
    qian_speaking "我……诶？\n你不问……等等，你就走了吗？！"
    qian "砰。回答我的只有无情的关门声音。\n……又被留下了。"
    

    qian_speaking "到底是怎么回事……说起来，好吵……"
    hide qianimg
    show qianimg shock at char_left with hpunch
    qian_speaking "啊……？！"
    scene bg_liroom0 with vpunch
    qian "床似乎在摇晃，我吓了一跳，这才从纷乱的思绪中醒过来，意识到周身巨大的轰鸣声响。"
    show sand0 with my_shake
    qian_speaking "什么情况……呜——"
    qian "我慢吞吞地下床，正要看个究竟，却被扑面而来的风浪掀翻在地。"
    show blur with dissolve
    qian_speaking "那……咳……那是，什么……"
    qian "沙，还是沙。\n狂乱摇曳的尘沙占据了我的全部视线。它席卷所有东西，不留任何逃脱的余地。"
    qian "我拼命地撑起身体，试图在粗粝的地上找到一个安定点。"
    qian "但是没有。"
    qian "逃不掉……"
    qian "视野里什么也不剩了，然后，一切都被吞噬。"
    scene bg_black with fade

    # 【Ending：风沙】
    $ persistent.ending[14] = 1
    
    return
