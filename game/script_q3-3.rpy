label q3_3:
    scene bg_bigroom with Fade(0.2,0.2,0.2)
    show dark
    qian "不行，绝不能停止在这个地方……并不是“只是生育”这么算的……被圈养在这个地方，没有选择的资格，无论未来会被做什么事都是有可能的。"
    show qianimg white shout mask at char_left with dissolve
    qian_speaking "做吧。"
    show liimg white close at char_right with dissolve
    li_speaking "嗯，好。"
    hide qianimg
    show qianimg white still mask at char_left
    qian "第一步是先把值班的人引到房间里。深夜人少，我们完全能够制服。然后，等到清晨……"
    
    scene bg_bigroom with Fade(0.2,0.2,0.2)
    show liimg white ask at char_left with easeinright
    li_speaking "有人在吗？喂？"
    qian "黎沙轻轻拍着大门，好一会后，不耐烦的声音传进来。"
    place_holder "怎么不睡？干什么？"
    li_speaking "那，那个……我可能旧伤犯了，腰特别疼，疼得我睡不着……"
    place_holder "忍着。赶紧回去睡。"
    li_speaking "……"
    show qianimg white sad mask at char_right with easeinright
    qian "不行，必须得说服她……我朝她对口型。"

    jump q3_3_temp


label q3_3_temp:
    menu:
        "【影响别人睡觉】":
            li_speaking "我这样疼着，也会影响别人睡觉的，这样不好……"
            place_holder "不会影响，回去。"
            li_speaking "……"
            hide qianimg
            show qianimg white still mask at char_right
            qian "……\n看来还是得换个别的说法。"
            jump q3_3_temp
        "【套近乎】":
            li_speaking "大家都是城外来的，稍微理解一下嘛……你也知道，有时候真的很疼。"
            place_holder "什么城外？"
            hide qianimg
            show qianimg white still mask at char_right
            qian "我和黎沙都愣住了，完全没想过会是这个回答。"
            place_holder "别说有的没的，回去。"
            qian "虽然很在意，但现在这不是重点……还是想办法说服她吧。"
            jump q3_3_temp
        "【影响身体状态】":
            jump q3_3_0


label q3_3_0: # ending here
    li_speaking "太疼了……这样之后也会影响性交和生育的……"
    qian "吱呀——\n门被推开一条缝隙。"
    scene bg_bigroom with shake
    place_holder "你过来，我帮你看——呃——"
    qian "我猛地绕到她背后，一只手捂住她的嘴，另一只手用力卡住她的喉咙，扼住多余的声音。"
    qian_speaking "你快点……"
    li_speaking "哈……！"
    qian "艰难地调整角度后，我留出一个空挡，黎沙就在这时一记手刀。\n啪，怀里的人软了下来。我轻轻关上门，把她放在地上。"
    li_speaking "没别的东西，就这张卡，应该是用来识别的，给你。"
    qian_speaking "行。她……把她放角落那边吧，到时候不容易被踩到。\n……唉，这真是。"

    scene bg_bigroom with fade
    show dark with dissolve
    show liimg white o at char_right with dissolve
    show qianimg white mask at char_left with dissolve
    li_speaking "害怕吗？"
    qian_speaking "是啊，我以前可是很遵纪守法的。"
    hide liimg
    show liimg white laugh at char_right
    li_speaking "那你遵纪守法，怎么到这儿来了？\n再说做都做完了，你现在感慨也没用。"
    hide qianimg
    show qianimg white o mask at char_left
    qian_speaking "喂……"
    hide liimg
    show liimg white smile at char_right
    li_speaking "嗨，我这不是在安慰你吗。"
    hide qianimg
    show qianimg white closecalm mask at char_left
    qian_speaking "有这么安慰的吗……"
    qian "被她一打断，我的心情倒是明快了些，也能说点轻松的话。尽管事情还没有结束。"
    hide qianimg
    show qianimg white mask at char_left
    qian_speaking "之后……就等着早上其他人来了。"
    hide liimg
    show liimg white at char_right
    li_speaking "嗯。"
    hide liimg
    show liimg white o at char_right
    li_speaking "盯着我干嘛？"
    hide qianimg
    show qianimg white o mask at char_left
    qian_speaking "啊，没……"
    qian "我有些尴尬地移开视线。竟然一不小心看得入神了……撩起的宽大衣摆下，是数不清的绷带和蔓延的疤痕。"
    qian "……"
    scene cg_li60 at cg0 with fade
    show bg_mem
    qian_speaking "你说要做准备，到底能准备什么？这是？"
    qian "黎沙拿出一条条纱布，把蓝灰色的粉末一层层夹在其中。"
    li_speaking "用来制造晶矿石的原石，反复摩擦后会在一定时间内爆炸，形成大量有毒粉尘。"
    qian_speaking "就是空气中到处飘的那些吗。"
    li_speaking "嗯……在城里大概会有用，如果要做一些不那么友好的事。"
    qian_speaking "带进去不会被发现吗？"
    li_speaking "有危害的工作都是城外做的，以前的人还了解一些，现在的城里人只知道做好的晶矿石，根本检查不出原石……"
    li_speaking "只要不被看到就可以。衣服可能会换，但缠在伤口上的绷带应该不会。\n你的眼睛……也可以。她们要检查最多是掀开，之后保护伤口还是可以绑回去。"
    qian_speaking "那你……"
    li_speaking "谁身上没点伤啊，这个就安心吧。这个是最简单的部分了，剩下的都是赌博。"
    scene bg_bigroom with fade
    show dark with dissolve
    qian "……"
    show qianimg white o mask at char_left with dissolve
    qian_speaking "……\n我不会让你死掉的。"
    show liimg white laugh at char_right with dissolve
    li_speaking "嗯？怎么，轮到你来安慰我了吗，还挺新鲜……"
    hide qianimg
    show qianimg white still mask at char_left
    qian_speaking "我是说真的。\n虽然没什么说服力，但，就算……我不会让你死在我前面的。"
    hide liimg
    show liimg white ask at char_right
    li_speaking "……\n哈？你确实没在安慰人，谁要是这样被你安慰，真是……"
    hide qianimg
    show qianimg white sad mask at char_left
    qian_speaking "……"
    hide liimg
    show liimg white smile at char_right
    li_speaking "好啦，我知道的。\n我之前是犹豫了，因为害怕。不过……我相信你，也相信自己的判断。"
    hide qianimg
    show qianimg white smile mask at char_left
    qian_speaking "好。"

    scene bg_bigroom with fade
    show dark with dissolve
    unknown "……还有……房间……那……"
    qian "我贴在靠门的墙壁上，终于捕捉到由远及近的声音，断断续续。"
    qian_speaking "……快来了。"
    li_speaking "嗯。\n你的手在发抖，停不下来，没问题？"
    qian_speaking "没……没事。"
    li_speaking "对了，我教你一个不会紧张的办法吧。"
    qian_speaking "啊？什么……？"
    window hide
    show cg_li70 at cg0 with dissolve
    pause(1.5)
    window show
    qian "黎沙忽然凑近，对着我狡黠一笑，让我摸不着头绪。而后，我整个人愣住了。"
    window hide
    show cg_li71 at cg0 with dissolve
    pause(1.5)
    window show
    qian_speaking "……\n……"
    li_speaking "……\n……"
    scene bg_bigroom with fade
    show dark with dissolve
    qian_speaking "这算哪门子的办法！"
    li_speaking "嘘……好了，快点准备好。"
    qian "……"
    qian "……我瞪了她一眼，用生硬的语气掩盖心跳的声音。而后，我好不容易才重新收拢精神，贴紧墙壁。"
    unknown "这边……没人……怎么……问题……"
    qian "脚步声越来越近，已经到了门口。——要过来了。"
    "吱呀——"
    unknown "喂，人呢？怎么没人叫这个房间？"
    unknown "什么？怎么了？"
    unknown "喂，过来搭把手，开个灯。"
    qian "好几个人凑到门口，准备进来……就现在！"
    show sand0 with vpunch
    "嘭！！！"
    unknown "这什么！喂！！"
    unknown "啊——咳，咳咳！！叫，其他人，来！"
    unknown "哇啊！！谁踩我！"
    qian "大量的烟尘在房间里爆开，一瞬间让我想起那个神奇的时刻——我在城外遇见了黎沙。\n不过，现在可不是想这些的时候……"
    qian "巨大的声响把房间里的其他人都吵醒了，我看不清，但这里一时间陷入大量的混乱。"
    qian_speaking "喂，用水试试！"
    unknown "对，对！把应急开关打开！"
    "呲——噗——嘭——！"
    unknown "喂，喂！咳咳……！"
    qian "我夹着声音在吵闹中吼了一嘴，在嘈杂中没有被其他人识破。而后无数的小水珠落下，与尘土结合反应，迸发出更大的爆炸。"
    window hide
    show cg_li80 at cg0 with dissolve
    pause(1.5)
    window show
    qian_speaking "咳……哈……"
    li_speaking "你还好吗？"
    qian_speaking "没事……"
    li_speaking "我把外面也引爆了，就算有监控也看不清。快走吧。"
    qian_speaking "嗯，咳……好。"
    qian "好在我有了些抗性，才没有在这浓度过高的沙尘中晕倒。\n这里的动静很快就把其他人也吸引过来，我们在慌乱的脚步声中悄悄跑出了房间。"
    scene bg_bigroom with fade
    show sand0 with dissolve
    li_speaking "快过来，这边——"
    
    scene bg_labfloor with fade
    show sand0 with dissolve
    show liimg white ask at char_right with dissolve
    li_speaking "小心……你怎么了？"
    show qianimg white o mask at char_left with dissolve
    qian_speaking "……我要去楼上。"
    li_speaking "啊？！不是说先出去的吗……留在这太危险了，等把事情闹大，外面的人找来再说吧。"
    hide qianimg
    show qianimg white closecalm mask at char_left
    pause(0.8)
    hide qianimg
    show qianimg white closecalm blind at char_left
    qian_speaking "你出去吧，这边的……我把剩下的都给你。"
    qian "我说着解开眼罩，多余的光线让视野一瞬间有点恍惚，但很快又重新聚焦，定格在近在咫尺的黎沙身上。"
    hide liimg
    show liimg white still at char_right
    li_speaking "……我知道了。\n你……我们外面见。"
    hide qianimg
    show qianimg white smile blind at char_left
    qian_speaking "好啊。"
    hide liimg with easeoutright
    hide qianimg with easeoutleft
    qian "整栋楼都陷入了慌乱，到处是吵架和闹腾的声音。我依照脑海里的记忆，朝着地图上的方位快速移动。"
    
    scene bg_labfloor with Fade(0.2,0.2,0.2,color="#fff")
    show sand0 with dissolve
    qian_speaking "没有。"
    
    scene bg_lab1 with Fade(0.2,0.2,0.2,color="#fff")
    show sand0 with dissolve
    qian_speaking "没有。"
    scene bg_lab2 with Fade(0.2,0.2,0.2,color="#fff")
    show sand0 with dissolve
    qian_speaking "没有……"
    scene bg_lab3 with Fade(0.2,0.2,0.2,color="#fff")
    show sand0 with dissolve
    qian "该说运气好还是坏呢……门口大开，不需要刷卡，里面的人也跑空了。但即使这里是最高级的实验室，也没有留下任何家人的痕迹。"
    qian "负责人是不认识的名字，除了我看不懂的仪器和图表，什么都没有。不，等等……内侧还有一扇门，标着“记忆实验室”。"
    qian_speaking "……\n这是……！"
    scene bg_lab0 with Fade(0.2,0.2,0.2,color="#fff")
    stop music fadeout 0.5
    $ renpy.music.play(music.dust, channel = "music", loop = True, fadein = 0.5)
    show sand0 with dissolve
    qian "我无法用言语形容看到的场景，因为是现实，比任何奇幻小说都来得诡异。"
    qian "无数个玻璃容器中放着漂浮的大脑，每个大脑……每个培养皿上都贴有标签，分别是编号，实验失败和成功次数，以及器官损耗度。"
    qian "一种恶心的不适感和呕吐感涌上来，我忍着它们，继续向里，直到尽头的最后两个玻璃柜。"
    scene cg_brain0 at cg0 with Fade(0.5,0.5,0.5,color="#fff")
    pause(1.5)
    qian "它们并排放置，标签上的字样和其他都不同。"
    show blur with vpunch
    qian_speaking "……哈……啊……"
    qian "视线开始失去焦点，呼吸也变得急促。耳边出现轰鸣声，无法平静。\n我……我……"
    qian "好晕……好难受……好想吐……\n头很痛，胃部也像被人大力捶打，几乎马上就要吐出来。"
    qian "怎么办……我……"
    scene bg_white with dissolve
    li_speaking "时茜！！"
    li_speaking "时茜……听得见吗？你怎么了？还好吗？"
    scene bg_brainblur at cg0 with vpunch
    show dark
    show qianimg white shock blind at char_left with dissolve
    qian_speaking "嗯……啊？黎沙？你，你怎么在这……？！"
    show liimg white still at char_mid with dissolve
    li_speaking "我不在这，你怎么办？！\n我还特地抢了一把枪过来，还好这里没别人……"
    hide qianimg
    show qianimg white still blind at char_left 
    qian_speaking "……"
    qian "我无法反驳——事实上，听到她的声音我才回过神，仿佛唯一的锚点，让我找回了真实存在的感觉。"
    qian "没有精力分心，我用尽全身力气止住身体的颤抖。手指已经发红，把黎沙的衣服都印出汗渍。"
    qian_speaking "对不起弄疼你了。"
    hide liimg
    show liimg white ask at char_mid
    li_speaking "我没事啊，问题是你，到底怎么了？"
    qian_speaking "没事，只是有点晕……你怎么没出去？"
    li_speaking "啊，外面已经闹大了，我不知道这是哪，但是人越来越多，城外的事情应该瞒不住了。"
    qian_speaking "……\n那就好。"
    qian "至少，有些东西被改变了……"
    li_speaking "所以现在该担心的就是你。"
    li_speaking "这里是你要找的地方吗，怎么这么恶心……人死都死了，大脑还得被人拿来利用……"

    hide liimg
    show liimg white o at char_mid
    hide qianimg
    show qianimg white shock blind at char_left
    li_speaking "我不太认字啊，这字写的是黄吗？"

    hide qianimg
    show qianimg white still blind at char_left 
    qian_speaking "……"
    qian "又来了，那种恶心得想吐的感觉。"
    qian_speaking "我……是……是啊。"
    qian_speaking "这上面贴的是名字。两个都是……都是我，我妈妈的名字。"

    hide liimg
    show liimg white still at char_mid
    li_speaking "你说什么？！"
    li_speaking "你，你的意思是……\n那你打算怎么……总，总不能一直留在这……"

    hide qianimg
    show qianimg white shock blind at char_left
    qian_speaking "对，对，不能一直留在这……我，我得……我要……"
    qian_speaking "我要救她们，我……啊……不，不行……这也不行……我，那……怎么办……！"
    unknown "哔——"
    $ renpy.sound.play(audio.buzz, channel = "sound", relative_volume = 0.25)
    qian "我的手胡乱地在控制台和屏幕上触碰按键，却只有持续的密码错误警告。"
    unknown "哔——\n系统将在90秒内启动外部销毁程序，输入正确密码即可取消。"

    hide qianimg
    show qianimg white shock blind at char_left with hpunch
    qian_speaking "怎，怎么办……不，不行……"
    stop sound

    scene cg_brain0 at cg0 with shake
    $ renpy.sound.play(audio.loud_sound, channel = "sound", relative_volume = 1.25)
    qian "一声巨响，面前的玻璃柜开始下降，地板，墙壁和天花板都有红光闪烁。"
    li_speaking "什么啊……这是说待会这个房间会炸吗？然后，这个实验装置会被保护好……"
    show blur with shake
    qian_speaking "怎么办，怎么办……我，必须……啊……我必须做点……怎么办……"
    horr "怎么办，怎么办……"
    hide blur with dissolve
    li_speaking "喂！醒醒！时茜！！"
    qian_speaking "啊，我……对不起……我，该怎么办……？我……"
    li_speaking "……对不起。\n但是，我们要出去了……"
    qian_speaking "我知道，我知道的……！我……"
    qian "理智告诉我，被保护起来的玻璃柜，也许会在以后成为重要的证据。"
    qian "可是，可是……这么大的一个实验基地，肯定不缺证据吧……找到有力的证据是那些管制局的人该做的事情吧……！"
    
    qian_speaking "至少在最后，让我保留一些私心吧……只是我作为家人……怎么能，怎么能让她们在死后也得不到安宁呢……！"
    li_speaking "你这，是……"
    qian "我向面前的人伸出手，而后手腕被人捧起，掌心放入了一个沉甸甸的物品。\n是黎沙说她刚刚抢来的枪。"
    
    
    qian "我……"
    show blur with hpunch
    horr "我……"
    $ renpy.sound.play(audio.buzz, channel = "sound", loop = True)
    "哔——哔——"
    hide blur 
    show cg_shoot at cg0 with shake
    qian "只能这样了……"
    "哔——哔——"
    qian "真没用，我……"
    hide cg_shoot
    show cg_shoot at cg0 with dissolve
    "哔——哔——"
    li_speaking "时茜，快点……！"
    hide cg_shoot with hpunch
    qian_speaking "啊……"
    li_speaking "我不想强迫你，但是你已经下定决心了吧！这件事只能你来做！"
    "哔——哔——"
    show cg_shoot at cg0 with vpunch
    qian_speaking "我知道，我……"
    show blur with dissolve
    qian "脸上很湿，不知道是汗水还是别的什么。\n我甩了甩头，努力重新将视线对焦。"
    hide blur with dissolve
    "哔——哔——"
    qian "所以……我努力坚持到现在，就是为了看到这样一个结局啊。"
    qian_speaking "……\n对不起。"
    menu:
        "【射击】":
            jump q3_3_0_1
        "【射击】":
            jump q3_3_0_1
        "【射击】":
            jump q3_3_0_1
        "【射击】":
            jump q3_3_0_1



label q3_3_0_1:
    stop music
    horr "……再見……"
    window hide
    $ renpy.sound.play(audio.gun_shot, channel = "sound")
    #$ renpy.sound.play(audio.glass, channel = "sound", relative_volume = 0.5)
    "砰！！"
    stop sound
    show bg_white with dissolve
    pause(0.5)
    $ renpy.music.play(audio.glass, channel = "music", loop = False, fadein = 0.1)
    $ renpy.sound.play(audio.glass_crack, channel = "sound")
    show cg_brain1 at cg0 with dissolve
    pause(0.3)
    show cg_brain2 at cg0 with dissolve
    pause(0.3)
    show cg_brain3 at cg0 with dissolve
    pause(0.3)
    show cg_brain4 at cg0 with dissolve
    pause(0.3)
    show cg_brain5 at cg0 with dissolve
    pause(1)
    scene bg_black with Fade(0.5,0.5,0.5)
    $ renpy.sound.play(audio.buzz, channel = "sound", fadeout = 0.5, relative_volume = 0.25)
    "……"
    scene bg_white with Fade(1,1,1,color="#fff")
    

    # 【Ending：尘埃】
    window hide
    stop sound
    show screen ending_title(number=19) with Fade(0.5,0.5,0.5)
    pause
    $ persistent.ending[19] = 1
    return

