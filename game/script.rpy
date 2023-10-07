# 游戏在此开始。

# set persistent values
default persistent.text = 0
default persistent.ending = [0]*20

# define fade behaviors
define fadehold = Fade(0.5, 1.0, 0.5)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# define sound effects
define audio.vibrations_1 = "audio/sound_effect/vibrations_1.wav"
define audio.vibrations_2 = "audio/sound_effect/vibrations_2.wav"
define audio.click = "audio/sound_effect/click.mp3"
define audio.ring = "<from 0 to 3.5>audio/sound_effect/phone_ring.mp3"
define audio.talking_people = "audio/sound_effect/talking_people.mp3"
define audio.owl = "audio/sound_effect/owl.mp3"
define audio.night_walk = "audio/sound_effect/night_walk.mp3"
define audio.dizzy = "<from 0 to 20>audio/sound_effect/dizzy.mp3"
define audio.heartbeat = "audio/sound_effect/heartbeat.mp3"
define audio.glass = "audio/sound_effect/glass.mp3"
define audio.current = "<from 0 to 36>audio/sound_effect/current.mp3"
define audio.elevator = "audio/sound_effect/elevator.mp3"

# define backgroun music
define music.orange_memory = "audio/bgm/orange_memory.mp3"
define music.dream = "audio/bgm/qimei.mp3"
define music.darkcity = "<from 0 to 100>audio/bgm/darkcity.mp3"
define music.horror = "audio/bgm/horror.mp3"
define music.interrogate = "<from 0.1 to 21>audio/bgm/interrogate.mp3"
define music.area_d = "audio/bgm/area_d.mp3"

label start:
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    # window hide
    $ quick_menu = False

    scene bg_badge at cg0 with dissolve
    show na1 at cg0 with dissolve
    pause
    hide na1 with dissolve
    show na2 at cg0 with dissolve
    pause
    hide na2 with dissolve
    pause
    stop music fadeout 1.0

    scene bg_black at cg0 with fade
    $ renpy.sound.play(audio.vibrations_1, channel = "sound", loop = True, relative_volume = 1.5)
    pause 2.0
    window show
    $ quick_menu = True
    unknown "……醒醒……起来……注意——"
    stop sound fadeout 1.0

    scene bg_black at cg0 with fade
    $ renpy.sound.play(audio.vibrations_2, channel = "sound", loop = True, relative_volume = 1.5)
    pause 2.0
    
    # TODO: bottomside doesnt work
    show qianimg closecalm at ease(center, offscreenbottom, 2)
    qian "有什么东西，好吵……\n无边的黑暗似乎在震动，扰得人不清净。是因为最近总觉得有人在盯着我吗？连梦里也不安生……"
    stop sound fadeout 1.0

    hide qianimg closecalm
    show qianimg shock at char_mid
    qian "——啊！"

    hide qianimg shock
    show qianimg pajama_red shock at large with dissolve
    qian "我倏地睁开眼睛，视线还很朦胧，于是一道鲜红色的光线格外显眼，带领我走到它的终点，指着我的心脏。"
    $ renpy.music.play(music.horror, channel = "music", loop = True, relative_volume = 0.6)
    
    show qianimg pajama_red shock at char_mid 
    qian "……\n那不是梦……。"

    scene bg_prolo_01 with fade
    $ renpy.sound.play(audio.heartbeat, channel = "sound", loop = True)
    hide qianimg pajama_red shock
    show qianimg sad at char_mid
    qian "我混沌的脑海顿时清醒，眼睛也适应了微弱的光线。\n几个装束严实的人站在床边，我的四周，把我紧紧围住。"
    show stick
    qian "他们在说什么，被面罩遮住，我听不真切。\n相同的黑色着装，挺拔绷直的身姿，若隐若现的标识……"
    qian "这是城市管制局的人，而且，还是最高级别的执行队。\n……我怎么会和她们扯上关系？"
    
    hide qianimg sad
    show qianimg shout at char_mid
    qian_speaking "你……你们要做什么？"
    qian "我想让自己的语气显得冷静，但嘴唇却不受控地颤抖。\n不行，冷静……她们是根据规定，不会乱来的。"
    show bfem_0r at char_right with easeinright
    bfem_speaking "时茜小姐，你被逮捕了。"
    stop sound
    stop music
    qian "我刚刚才建立起的心理防线马上破碎。"
    qian_speaking "……什么？你们弄错了吧！\n别开玩笑了！"
    hide qianimg 
    show qianimg shock at char_mid
    qian_speaking "别过来！喂，肯定是有什么误会的地方！怎么可能！等——"
    na "——！"
    show bfem_0l at char_left with easeinleft
    qian "两个人靠近，我剧烈挣扎起来，却没有用，在用力的拉扯中从床上摔倒在地。\n好痛……我几乎瞬间就冒出了眼泪，在挺直的身板前显得狼狈又讽刺。"
    qian "没有人理会这点，我被拖住，床边的东西因为磕绊而掉在地上，我却没办法把它们拿起来，只能踉跄着往外走。"
    
    hide qianimg 
    show qianimg shout at char_mid
    qian_speaking "喂，等等……等等啊！"
    hide bfem_0l with easeoutleft 
    pause(0.1)
    hide bfem_0r with easeoutright 
    pause(0.1)
    hide qian_shocked0 with fade 

    scene bg_office_0 with fade
    show qianimg sad at char_left with dissolve
    $ renpy.sound.play(audio.current, channel = "sound", loop = True, relative_volume = 0.4, fadeout = 1.0)
    qian "这里是管制局。\n巨大的顶灯不知疲倦地射出明亮的白色光线，刺眼到让人眼睛生疼。我穿着睡衣站在角落的一间房间中央，有一种无所适从的局促。"
    qian "……为什么……我无声地吸了一口气，压抑着翻涌的情绪，看向离我最近的人。"
    hide qianimg sad

    show qianimg shout at char_left
    qian_speaking "到底发生了什么？没有说明吗？"
    qian "等待的十几个小时过去，我无比疲惫，声音发紧，从嗓子里挤出来，听着有些尖锐。她却毫无所觉，只是瞥过来一眼，而后像习以为常地转过头，无视。"
    qian "我呆呆地站在原地，像个傻子。\n……感觉，糟透了。"
    stop sound

    scene black with fadehold
    scene bg_office_1 with fade
    show qianimg sad at char_left
    show bfem_0r at char_right with dissolve
    $ renpy.music.play(music.interrogate, channel = "music", loop = True, fadein = 2.0, fadeout = 1.0)
    bfem_speaking "我问你答，懂吗？"
    qian_speaking "……为什么？你们还没回答我的问题。"
    bfem_speaking "我问，你答。"
    qian "她加重语气，令我下意识缩了缩肩膀。压迫……那种令人不舒服的感觉清晰地裹在我身上。\n于是我顿了顿，还是绷紧声音说，好的。"
    
    scene bg_office_1 with fade
    show qianimg still at char_left
    show bfem_0r at char_right
    bfem_speaking "你了解过你家人的工作吗？"

    hide qianimg still
    show qianimg o at char_left
    qian_speaking "在研究所做研究，关于生物科学……其他的我也不知道，她们不能说。"
    bfem_speaking "除了登记的，家里还有别的房间吗？"
    qian_speaking "为什么这也要问——我没有，我的房间里没有……别的，不知道。"
    
    hide qianimg o
    show qianimg sad at char_left
    qian "问题越来越多，配合刺目的灯光，让我头晕脑胀，到最后已经变成下意识作答，无法思考。\n但即使是这样……我也没能问出任何东西。"
    bfem_speaking "拿着。"
    hide qianimg sad
    
    show qianimg still at char_left
    qian_speaking "好的……啊，什么？"
    qian "我依旧是下意识回应，说完才发现并不是在问问题，而是有东西被递过来。\n个人终端机，荆棘之城的统一装置，正面屏幕，反面刻着城市印章。但……并不是我原来的那个。"
    qian "为……不，我已经发现了，就算询问也不会有人回答。\n屏幕亮起，这个全新的终端上面正显示着我的名字，以及一条带有鲜红色标签的消息。"
    
    hide qianimg still
    hide bfem_0r
    na "通知：\n因编号T19957及编号T20234涉及S级禁令，编号T25648作为直接血缘关系，将被剥夺一切原有城市权利。"
    show qianimg shock at char_mid
    qian "等等，什么意思……\n我机械性地点亮屏幕，打开消息，读完信息的时候才后知后觉，似乎有什么很重要的事情。"
    qian "怎么可能？钟女士和黄女士都是单纯的工作狂，谁犯错都不可能是她们犯错。\n况且，S级禁令，那基本上意味着能够动摇整个城市的危险。"
    qian "我不明白。\n我不明白……为什么？"

    hide qianimg shock
    show bfem_0r at char_mid with dissolve
    bfem_speaking "看完了吗？走吧。"

    show qianimg shout at char_mid
    qian_speaking "什么？不，等等，我不懂……喂！\n你，你们不能这样……给我一个解释啊！为什么？！"
    
    hide qianimg shout
    show qianimg close at char_mid
    qian_speaking "……唔！好痛，痛……啊啊！"
    stop music

    scene bg_office_1
    scene bg_office_2 with fade
    qian "好疼。我感觉身体像是快要散架了。\n头疼，肩膀疼，脚疼，被控制住住的手腕也疼。"
    qian "和之前一样，几个高大女人围着我，手拿武器，仿佛我罪大恶极。\n可我明明只是在家里睡觉，一无所知。只是在睡觉而已，醒来却发生这些事情。\n还有钟女士和黄女士，不知道她们怎么样了……"
    scene bg_office_3 with Fade(0.1,0.2,0.1)
    qian "我全身上下只有一套居家睡衣和崭新的终端，身体被控制住，被拉着往外走。\n我死死咬住嘴唇，避免让眼泪流下来，显得更加狼狈不堪。"
    scene bg_office_4 with Fade(0.1,0.3,0.1)
    qian "四周皆是单色墙壁，泛着淡淡的金属冷光。被一身黑的人包围的我，显得格外刺眼。\n空间里弥漫着窒息的沉默，我尽力习惯，可不安和恐慌仍然无法消除。"
    qian "究竟发生了什么……我应该怎么办？\n信息太少，我甚至不知道所谓的禁令到底是什么，但……就算知道了也无能为力。"
    
    scene black with fadehold
    $ renpy.sound.play(audio.elevator, channel = "sound")
    scene bg_office_4 with Fade(0.1,0.3,0.1)
    with vpunch
    "————"
    pause
    qian "突然的失重感席卷全身，地面晃动，它正在下降。\n这不是普通的房间，而是——"
    
    show qianimg sad at char_mid with dissolve
    qian "速度，时间，我回忆起相似的数据。\n城市里的“竖直电梯”连接不同的区域，而现在，自然是从A区下行。\n……我到底要被带去哪里？"
    qian "……\n……"
    stop sound

    scene bg_road02 with Fade(0.5,0.5,0.5)
    qian "……\n……"
    qian "头顶的光线微弱，只有时时闪烁的凌乱灯牌。"
    scene bg_road01 with Fade(0.1,0.2,0.1)
    qian "狭窄而崎岖的小道四通八达，毫无章法。"
    scene bg_road03 with Fade(0.1,0.2,0.1)
    qian "充斥淡淡难闻味道和肮脏颗粒的空气。"

    show qianimg sad at char_mid with dissolve
    qian_speaking "怎么会……这是……"

    hide qianimg sad
    show qianimg still at char_mid with dissolve
    qian "心里一直以来的隐约预感终于成真。\n我当然知道这个地方。\n尽管没有来过，但曾经在书本、视频和记录里，看到过它的身影……"
    hide qianimg still
    "荆棘之城的最底端\nD层"
    
    scene bg_black with Fade(0.5,0.5,0.5,color="#fff")
    $ renpy.music.play(music.area_d, channel = "music", loop = True, fadein = 1.0, fadeout = 1.0)
    qian "荆棘之城是一座竖直发展的城市，自上而下分为A，B，C，D层。在这其中，D层位于城市最底部，被那些游手好闲、不学无术的人占据着，藏匿着许多肮脏与恶意。"
    qian "荆棘之城是这座城市的名字，它于数百年前建成，是我们最后的城市。那时候，战争失败的人们——我们的祖先——被迫失去原来的土地，只能在有限的空间里苟且偷生。"
    qian "防护罩切断了整个城市与外界的联系，将我们困在牢笼之中，没有丰富的资源，只有匮乏的生活。"
    qian "而D层，又是这座城市最为匮乏的地方……"
    qian "但……这些也只是我之前在书上了解的D层信息。我从来没有想过自己有一天会来这里。"

    scene bg_road01 with Fade(0.1,0.4,0.1)
    show bfem_0r at char_right with dissolve
    show qianimg sad at char_left with dissolve
    bfem_speaking "失去城市身份的人，之后在D层生活。\n具体信息会发到终端，个人数据会做相应调整。"
    qian_speaking "等，等等……我家人呢？她们怎么样了？"
    hide qianimg sad

    show qianimg still at char_left with dissolve
    qian "我已经对自己的处境不抱幻想，只希望至少能取得和家人的联系。\n但……还是没有回应，只有令人绝望的沉默。"
    qian "短短一天，这已经是我不知道多少次说出这句话，无奈又无力。\n大概是之前喊得太厉害，我的嗓子已经哑了，说话时喉咙里止不住地冒出血腥味，惹得我再次干呕起来。"
    
    scene bg_road03 with Fade(0.1,0.2,0.1)
    show qianimg sad at char_mid with dissolve
    qian "等我回过神，先前围在四周押住我的人都已不在。\n只剩下星星点点的亮光的黑暗里，我攥紧衣服的下摆，下意识地往后退，无所适从。"
    
    hide qianimg sad
    show qianimg closesad at char_left with dissolve
    qian "……\n刚才的动静不小，但不知道是不是管制局太显眼，并没有人靠近。现在也是，我能感受到有些陌生的目光扫过，又很快离开。"
    qian "……\n……"
    qian "肌肉还在隐隐作痛，脚下的地板变得又硬又硌，刺得我皮肤生疼。\n我轻轻吸了一口气，毫无防备被扔到完全陌生的环境，茫然和恐慌逐渐爬上我的身体，完全覆盖住我的神经。"
    $ renpy.music.set_pause(True, channel = "music")
    $ renpy.sound.queue([audio.ring,], channel = "sound")
    qian "滴，没设置过的终端机发出默认的响声。颤抖的手指点开终端机——原本空荡荡，只有我的个人信息——此刻收件箱却多了一个数字。我打开后，震惊地发现这是钟女士发来的消息。"
    
    scene bg_black with Fade(0.1,0.1,0.1)
    na1 "来信人：T20234"
    na1 "宝宝：\n很抱歉因为工作连累了你。我们还需要一段时间，等到所有事情都结束就会没事的。\n只是委屈你了，管制局可能会很忙，但必要的东西会安排好。你多注意一下，不会有问题。"
    na1 "我们相信你在D层也能努力过好，等我们回去。\n钟 & 黄】"
    stop sound

    $ renpy.music.set_pause(False, channel = "music")
    scene bg_black with Fade(0.1,0.1,0.1)
    show qianimg sad at char_mid with dissolve
    qian "……\n……"
    qian "以前我绝对不会想过，这样普通又简单的话竟然会让人有想流泪的冲动。\n我甚至无法仔细阅读那些文字，只是看到编号，就已经几乎控制不住颤抖的手指。"
    hide qianimg sad
    show qianimg still at char_mid
    qian "半晌，我收回终端机，深深地吐出一口气。"
    qian "钟女士和黄女士没说错……我还有她们，我还要等着她们。\n只要这样想着……就算已经不是原来的生活，我也必须要在这里生存下去。"
    hide qianimg still
    scene bg_cross with Fade(0.2,0.5,0.2)
    qian "……\n放话很容易，但我似乎第一步就遇到了问题。"
    qian "眼前，像是供电不足的指示牌在空地的岔路前一闪一闪，上面是歪歪扭扭的文字：\n通向——“管制局”，“黑街”，“230居民区”。"
    qian "我现在……\n能去哪里呢……该去哪里呢？"

    menu:
        "【管制局】":
            $ renpy.sound.play(audio.click, channel = "sound", loop = False)
            jump q1_1
        "【黑街】":
            $ renpy.sound.play(audio.click, channel = "sound", loop = False)
            jump q1_2
        "【230居民区】" if persistent.ending[6] == 1 and persistent.ending[13] == 1:
            $ renpy.sound.play(audio.click, channel = "sound", loop = False)
            jump q1_3
    
