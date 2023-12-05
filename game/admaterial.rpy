# scenes for advertisement movies

label material:
    scene bg_prolo_01 with dissolve
    show qianimg shock at char_mid
    qian "……\n那不是梦……。"

    scene bg_office_4 with dissolve
    show qianimg still at char_mid
    qian "突然的失重感席卷全身，地面晃动，它正在下降。\n这不是普通的房间，而是——"

    scene bg_cross with dissolve
    qian "我现在……\n能去哪里呢……该去哪里呢？"

    window hide
    $ quick_menu = False
    scene bg_road01 with dissolve
    pause(0.5)
    scene bg_road02 with dissolve
    pause(0.5)
    scene bg_road03 with dissolve
    pause(0.5)
    scene bg_road04 with dissolve
    pause(0.5)
    scene bg_road05 with dissolve
    pause
    
    window show
    scene bg_factory with dissolve
    show qianimg shirt closecalm at char_mid
    pause

    scene bg_cafe0 with dissolve
    show qianimg shirt closecalm at char_mid
    pause

    scene bg_city0 with dissolve
    show qianimg shirt closecalm at char_mid
    pause

    scene bg_bar0 with dissolve
    show qianimg pajama closecalm at char_mid
    pause

    scene bg_yingroom0 with dissolve
    show qianimg pajama closecalm at char_mid
    pause

    scene bg_corridor with dissolve
    show qianimg pajama closecalm at char_mid
    pause

    scene bg_liroom0 with dissolve
    show qianimg pajama closecalm at char_mid
    pause

    scene bg_workplace with dissolve
    show qianimg coat closecalm at char_mid
    pause

    scene bg_ele with dissolve
    show qianimg black closecalm at char_mid
    pause

    scene bg_black with dissolve
    show qianimg pajama closecalm at char_mid
    pause
    hide qianimg
    show qianimg at char_mid
    pause
    show qianimg pajama still at large1
    pause

    window hide
    hide qianimg
    show titletext at mid with zoomin
    pause
    