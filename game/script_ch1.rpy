# 游戏在此开始。

label ch1:
    scene black_bg
    qian "荆棘之城是一座竖直发展的城市，自上而下分为A，B，C，D层。在这其中，D层位于城市最底部，被那些游手好闲、不学无术的人占据着，藏匿着许多肮脏与恶意。"
    qian "但……这些也只是我之前在书上了解的D层信息。我从来没有想过自己有一天会来这个地方。"
    scene bg_D01 with Fade(0.5,0.5,0.5)
    show bfem_0r at char_right with dissolve
    show qian_worry01 at char_left with dissolve
    bfem_speaking "失去城市身份的人，之后在D层生活。\n具体信息会发到终端，个人数据会做相应调整。"
    qian_speaking "等，等等……我家人呢？她们怎么样了？"
    hide qian_worry01
    show qian_think0 at char_left with dissolve
    qian "我已经对自己的处境不抱幻想，只希望至少能取得和家人的联系。\n但……还是没有回应，只有令人绝望的沉默。"
    qian "短短一天，这已经是我不知道多少次说出这句话，无奈又无力。\n大概是之前喊得太厉害，我的嗓子已经哑了，说话时喉咙里止不住地冒出血腥味，惹得我再次干呕起来。"
    scene bg_D01 with Fade(0.5,0.5,0.5)
    show qian_think0 at char_mid with dissolve
    qian "等我回过神，先前围在四周押住我的人都已不在。\n只剩下星星点点的亮光的黑暗里，我攥紧衣服的下摆，下意识地往后退，无所适从。"
    hide qian_think0
    show qian_worry01 at char_left with dissolve
    qian "……\n刚才的动静不小，但不知道是不是管制局太显眼，并没有人靠近。现在也是，我能感受到有些陌生的目光扫过，又很快离开。"
    qian "……\n……"
    qian "肌肉还在隐隐作痛，脚下的地板变得又硬又硌，刺得我皮肤生疼。\n我轻轻吸了一口气，毫无防备被扔到完全陌生的环境，茫然和恐慌逐渐爬上我的身体，完全覆盖住我的神经。"
    qian "滴，没设置过的终端机发出默认的响声。颤抖的手指点开终端机——原本空荡荡，只有我的个人信息——此刻收件箱却多了一个数字。我打开后，震惊地发现这是宋女士发来的消息。"
    scene black_bg with Fade(0.1,0.1,0.1)
    
    return





transform char_mid:
    zoom 0.25
    xalign 0.5
    yalign 0.27

transform char_left:
    zoom 0.25
    xalign 0.2
    yalign 0.27

transform char_right:
    zoom 0.25
    xalign 0.8
    yalign 0.27

transform large:
    xalign 0.5
    yalign 0.85