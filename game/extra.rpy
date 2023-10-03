define ending_1 = "ENDING: 死寂" # ending lists
define ending_2 = "ENDING: 安心" 
define ending_3 = "ENDING: 突刺" # python index starts at 0
define ending_4 = "ENDING: 麻痹"
define ending_5 = "ENDING: 可惜"
define ending_6 = "ENDING: 紧急"
define ending_7 = "ENDING: 绽放"
define ending_8 = "ENDING: 晕眩"
define ending_9 = "ENDING: 美梦"
define ending_10 = "ENDING: 窒息"
define ending_11= "ENDING: 惊疑"
define ending_12 = "ENDING: 秘密"
define ending_13 = "ENDING: 逃离"
define ending_14 = "ENDING: 荆棘"
define ending_15 = "ENDING: 风沙"
define ending_16 = "ENDING: 空荡"
define ending_17 = "ENDING: 噩梦"
define ending_18 = "ENDING: 沉默"
define ending_19 = "ENDING: 陌生"
define ending_20 = "ENDING: 尘埃"

define endings = [
"ENDING: 死寂",
"ENDING: 安心",
"ENDING: 突刺",
"ENDING: 麻痹",
"ENDING: 可惜",
"ENDING: 紧急",
"ENDING: 绽放",
"ENDING: 晕眩",
"ENDING: 美梦",
"ENDING: 窒息",
"ENDING: 惊疑",
"ENDING: 秘密",
"ENDING: 逃离",
"ENDING: 荆棘",
"ENDING: 风沙",
"ENDING: 空荡",
"ENDING: 噩梦",
"ENDING: 沉默",
"ENDING: 陌生",
"ENDING: 尘埃",]



## extra screens
screen extra_navi():
    key "mouseup_3" action Return()
    hbox:
        style_prefix "navigation"
        xalign 0.5
        yalign 0.95
        spacing 60
        textbutton _("返回") action Return()
        # textbutton _("画廊") action ShowMenu("gallary")
        textbutton _("结局列表") action ShowMenu("ending")
        textbutton _("概览路线") action ShowMenu("outline")
        textbutton _("制作名单") action ShowMenu("credits")


screen gallary():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi



screen ending():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi

    hbox:
        xalign 0.5
        yalign 0.4

        grid 5 4:
            for i in range(20): 
                if persistent.ending[i] == 1:
                    # add im.Scale(f"gui/ending/ending{i+1}.jpg",180,180)
                    imagebutton:
                        idle im.Scale(f"gui/ending/ending{i+1}.jpg",180,180)
                        hover im.Scale(f"gui/ending/ending{i+1}.jpg",180,180)
                        action NullAction()
                        tooltip endings[i]
                else:
                    add im.Scale("gui/ending/locked_end.jpg",180,180)

            spacing 15
        
    
    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            hbox:
                xalign 0.5
                text tooltip size 25            


screen outline():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi
    add im.Scale("gui/routes/routeimg.png",1920,1080)
    for i in range(20): 
        if persistent.ending[i] == 1:
            add im.Scale(f"gui/routes/routeimg{i+1}.png",1920,1080)


screen credits():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi
    vbox:
        xalign 0.1
        yalign 0.1
        spacing 18
        vbox:
            text _("剧本·美术·程序") size 40
            text _("可食用蓝墨水") size 25
        vbox:
            text _("技术帮助") size 40
            text _("akagi") size 25
        vbox:
            text _("测试") size 40
            text _("akagi · HydrogenRb · 可食用蓝墨水") size 25



screen ending_title(number):
    if 0 <= number <= 6:
        add "gui/ending/ending_chi.jpg"
    elif 7 <= number <= 14:
        add "gui/ending/ending_ying.jpg"
    elif 15 <= number <= 19:
        add "gui/ending/ending_li.jpg"

    if number == 6 or number == 13 or number == 19:
        hbox:
            xalign 0.5
            yalign 0.5
            text endings[number] size 100 color "#780707"
            
    else:
        hbox:
            xalign 0.5
            yalign 0.5
            text endings[number] size 100