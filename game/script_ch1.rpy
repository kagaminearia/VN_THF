# 游戏在此开始。

label ch1:
    scene black_bg with Fade(0.5,0.5,0.5,color="#fff")
    qian "荆棘之城是一座竖直发展的城市，自上而下分为A，B，C，D层。在这其中，D层位于城市最底部，被那些游手好闲、不学无术的人占据着，藏匿着许多肮脏与恶意。"
    qian "但……这些也只是我之前在书上了解的D层信息。我从来没有想过自己有一天会来这个地方。"
    scene bg_road01 with Fade(0.1,0.4,0.1)
    show bfem_0r at char_right with dissolve
    show qian_worry01 at char_left with dissolve
    bfem_speaking "失去城市身份的人，之后在D层生活。\n具体信息会发到终端，个人数据会做相应调整。"
    qian_speaking "等，等等……我家人呢？她们怎么样了？"
    hide qian_worry01
    show qian_think0 at char_left with dissolve
    qian "我已经对自己的处境不抱幻想，只希望至少能取得和家人的联系。\n但……还是没有回应，只有令人绝望的沉默。"
    qian "短短一天，这已经是我不知道多少次说出这句话，无奈又无力。\n大概是之前喊得太厉害，我的嗓子已经哑了，说话时喉咙里止不住地冒出血腥味，惹得我再次干呕起来。"
    scene bg_road01 with Fade(0.5,0.5,0.5)
    show qian_think0 at char_mid with dissolve
    qian "等我回过神，先前围在四周押住我的人都已不在。\n只剩下星星点点的亮光的黑暗里，我攥紧衣服的下摆，下意识地往后退，无所适从。"
    hide qian_think0
    show qian_worry01 at char_left with dissolve
    qian "……\n刚才的动静不小，但不知道是不是管制局太显眼，并没有人靠近。现在也是，我能感受到有些陌生的目光扫过，又很快离开。"
    qian "……\n……"
    qian "肌肉还在隐隐作痛，脚下的地板变得又硬又硌，刺得我皮肤生疼。\n我轻轻吸了一口气，毫无防备被扔到完全陌生的环境，茫然和恐慌逐渐爬上我的身体，完全覆盖住我的神经。"
    qian "滴，没设置过的终端机发出默认的响声。颤抖的手指点开终端机——原本空荡荡，只有我的个人信息——此刻收件箱却多了一个数字。我打开后，震惊地发现这是宋女士发来的消息。"
    scene black_bg with Fade(0.1,0.1,0.1)
    red "【收件人：T25648"
    red "宝宝：\n很抱歉因为工作连累了你。我们还需要一段时间，等到所有事情都结束就会没事的。\n只是委屈你了，管制局可能会很忙，但必要的东西会安排好。你多注意一下，不会有问题。"
    red "我们相信你在D层也能努力过好，等我们回去。\n爱你的 母亲和妈妈】"
    scene black_bg with Fade(0.1,0.1,0.1)
    show qian_worry01 at char_mid with dissolve
    qian "……\n……"
    qian "以前我绝对不会想过，这样普通又简单的话竟然会让人有想流泪的冲动。\n我甚至无法仔细阅读那些文字，只是看到寄件人的编号，就已经几乎控制不住颤抖的手指。"
    hide qian_worry1
    show qian_close2 at char_mid
    qian "半晌，我收回终端机，深深地吐出一口气。"
    hide qian_close2
    show qian_see0 at char_mid
    qian "宋女士和黄女士没说错……我还有她们，我还要等着她们。\n只要这样想着……就算已经不是原来的生活，我也必须要在这里生存下去。"
    scene bg_cross with Fade(0.2,0.5,0.2)
    qian "……\n放话很容易，但我似乎第一步就遇到了问题。"
    qian "眼前，像是供电不足的指示牌在空地的岔路前一闪一闪，上面是歪歪扭扭的文字：\n通向——“管制局”，“黑街”，“230居民区”。"
    qian "我现在……\n能去哪里呢……该去哪里呢？"

    menu:
        "【管制局】":
            jump q1_1
        "【黑街】":
            "wait for q1.2"
        "【230居民区】":
            jump q1_3


    return


